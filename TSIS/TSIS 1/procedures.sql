-- ============================================================
-- PhoneBook — Functions & Stored Procedures
-- Practice 8 + TSIS 1
-- ============================================================


-- ────────────────────────────────────────────────────────────
-- 1. ФУНКЦИЯ: поиск контактов по паттерну (имя / телефон / email)
--    Practice 8 + расширена в TSIS 1 (все поля + все телефоны)
-- ────────────────────────────────────────────────────────────
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(
    id       INT,
    name     VARCHAR,
    email    VARCHAR,
    birthday DATE,
    grp      VARCHAR,
    phone    VARCHAR,
    ptype    VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT
        c.id,
        c.name,
        c.email,
        c.birthday,
        g.name      AS grp,
        ph.phone,
        ph.type     AS ptype
    FROM contacts c
    LEFT JOIN groups g  ON g.id  = c.group_id
    LEFT JOIN phones ph ON ph.contact_id = c.id
    WHERE c.name  ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR ph.phone ILIKE '%' || p_query || '%'
    ORDER BY c.name;
END;
$$ LANGUAGE plpgsql;


-- ────────────────────────────────────────────────────────────
-- 2. ФУНКЦИЯ: пагинация контактов
--    Practice 8
-- ────────────────────────────────────────────────────────────
CREATE OR REPLACE FUNCTION get_contacts_page(
    p_limit  INT DEFAULT 10,
    p_offset INT DEFAULT 0
)
RETURNS TABLE(
    id       INT,
    name     VARCHAR,
    email    VARCHAR,
    birthday DATE,
    grp      VARCHAR,
    phones   TEXT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.name,
        c.email,
        c.birthday,
        g.name AS grp,
        STRING_AGG(ph.phone || '(' || COALESCE(ph.type,'?') || ')', ', ') AS phones
    FROM contacts c
    LEFT JOIN groups g  ON g.id  = c.group_id
    LEFT JOIN phones ph ON ph.contact_id = c.id
    GROUP BY c.id, c.name, c.email, c.birthday, g.name
    ORDER BY c.name
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;


-- ────────────────────────────────────────────────────────────
-- 3. ПРОЦЕДУРА: upsert контакта (вставка или обновление телефона)
--    Practice 8
-- ────────────────────────────────────────────────────────────
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name  VARCHAR,
    p_phone VARCHAR,
    p_type  VARCHAR DEFAULT 'mobile'
)
LANGUAGE plpgsql AS $$
DECLARE
    v_id INT;
BEGIN
    -- получаем или создаём контакт
    SELECT id INTO v_id FROM contacts WHERE name = p_name;

    IF NOT FOUND THEN
        INSERT INTO contacts(name) VALUES(p_name) RETURNING id INTO v_id;
    END IF;

    -- проверяем телефон
    IF NOT EXISTS (SELECT 1 FROM phones WHERE contact_id = v_id AND phone = p_phone) THEN
        INSERT INTO phones(contact_id, phone, type) VALUES(v_id, p_phone, p_type);
    ELSE
        UPDATE phones SET type = p_type
        WHERE contact_id = v_id AND phone = p_phone;
    END IF;
END;
$$;


-- ────────────────────────────────────────────────────────────
-- 4. ПРОЦЕДУРА: массовая вставка контактов со списка
--    Practice 8 — валидация телефонов, возврат некорректных
-- ────────────────────────────────────────────────────────────
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    p_names   VARCHAR[],
    p_phones  VARCHAR[],
    OUT bad_entries TEXT
)
LANGUAGE plpgsql AS $$
DECLARE
    i        INT;
    v_name   VARCHAR;
    v_phone  VARCHAR;
    v_id     INT;
    v_bad    TEXT := '';
BEGIN
    FOR i IN 1 .. array_length(p_names, 1) LOOP
        v_name  := p_names[i];
        v_phone := p_phones[i];

        -- валидация: телефон должен содержать только цифры, +, -, пробелы и быть длиной 7-15
        IF v_phone !~ '^[+0-9\-\s]{7,15}$' THEN
            v_bad := v_bad || v_name || ':' || v_phone || '; ';
            CONTINUE;
        END IF;

        SELECT id INTO v_id FROM contacts WHERE name = v_name;
        IF NOT FOUND THEN
            INSERT INTO contacts(name) VALUES(v_name) RETURNING id INTO v_id;
        END IF;

        IF NOT EXISTS (SELECT 1 FROM phones WHERE contact_id = v_id AND phone = v_phone) THEN
            INSERT INTO phones(contact_id, phone, type) VALUES(v_id, v_phone, 'mobile');
        END IF;
    END LOOP;

    bad_entries := CASE WHEN v_bad = '' THEN 'none' ELSE v_bad END;
END;
$$;


-- ────────────────────────────────────────────────────────────
-- 5. ПРОЦЕДУРА: удаление по имени или телефону
--    Practice 8
-- ────────────────────────────────────────────────────────────
CREATE OR REPLACE PROCEDURE delete_contact(
    p_name  VARCHAR DEFAULT NULL,
    p_phone VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name IS NOT NULL THEN
        DELETE FROM contacts WHERE name = p_name;
    ELSIF p_phone IS NOT NULL THEN
        DELETE FROM contacts
        WHERE id IN (
            SELECT contact_id FROM phones WHERE phone = p_phone
        );
    END IF;
END;
$$;


-- ────────────────────────────────────────────────────────────
-- 6. ПРОЦЕДУРА: добавить телефон к существующему контакту
--    TSIS 1
-- ────────────────────────────────────────────────────────────
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone        VARCHAR,
    p_type         VARCHAR DEFAULT 'mobile'
)
LANGUAGE plpgsql AS $$
DECLARE
    v_id INT;
BEGIN
    SELECT id INTO v_id FROM contacts WHERE name = p_contact_name;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Контакт "%" не найден', p_contact_name;
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES(v_id, p_phone, p_type)
    ON CONFLICT DO NOTHING;
END;
$$;


-- ────────────────────────────────────────────────────────────
-- 7. ПРОЦЕДУРА: переместить контакт в группу
--    TSIS 1 (создаёт группу если нет)
-- ────────────────────────────────────────────────────────────
CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name   VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    v_gid INT;
    v_cid INT;
BEGIN
    -- создаём группу если не существует
    INSERT INTO groups(name) VALUES(p_group_name)
    ON CONFLICT (name) DO NOTHING;

    SELECT id INTO v_gid FROM groups WHERE name = p_group_name;
    SELECT id INTO v_cid FROM contacts WHERE name = p_contact_name;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Контакт "%" не найден', p_contact_name;
    END IF;

    UPDATE contacts SET group_id = v_gid WHERE id = v_cid;
END;
$$;