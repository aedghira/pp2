"""
PhoneBook — Practice 7 + Practice 8 + TSIS 1
Полное консольное приложение с PostgreSQL
"""

import csv
import json
import os
import sys
from datetime import datetime

import psycopg2
from connection import get_conn

# ════════════════════════════════════════════════════════════
#  ИНИЦИАЛИЗАЦИЯ БД
# ════════════════════════════════════════════════════════════

def init_db(conn):
    """Создаёт таблицы и загружает SQL-функции/процедуры."""
    cur = conn.cursor()

    # читаем и выполняем schema.sql
    base = os.path.dirname(os.path.abspath(__file__))
    for fname in ("schema.sql", "procedures.sql"):
        path = os.path.join(base, fname)
        if os.path.exists(path):
            with open(path) as f:
                cur.execute(f.read())

    conn.commit()
    cur.close()
    print("✅ База данных инициализирована.")


# ════════════════════════════════════════════════════════════
#  ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ════════════════════════════════════════════════════════════

def _print_table(rows, headers):
    if not rows:
        print("  (нет данных)")
        return
    widths = [max(len(str(h)), max(len(str(r[i] or "")) for r in rows))
              for i, h in enumerate(headers)]
    line = "+-" + "-+-".join("-" * w for w in widths) + "-+"
    fmt  = "| " + " | ".join(f"{{:<{w}}}" for w in widths) + " |"
    print(line)
    print(fmt.format(*headers))
    print(line)
    for row in rows:
        print(fmt.format(*[str(v or "") for v in row]))
    print(line)


def _input(prompt, default=None):
    val = input(prompt).strip()
    return val if val else default


# ════════════════════════════════════════════════════════════
#  PRACTICE 7 — CRUD
# ════════════════════════════════════════════════════════════

# ── Вставка из CSV ──────────────────────────────────────────
def import_csv(conn, path="contacts.csv"):
    """Practice 7 + TSIS 1: поддерживает email, birthday, group, type."""
    if not os.path.exists(path):
        print(f"⚠  Файл {path} не найден.")
        return

    cur = conn.cursor()
    inserted = 0
    skipped  = 0

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name     = row.get("name", "").strip()
            phone    = row.get("phone", "").strip()
            ptype    = row.get("type", "mobile").strip() or "mobile"
            email    = row.get("email", "").strip() or None
            birthday = row.get("birthday", "").strip() or None
            group    = row.get("group", "Other").strip() or "Other"

            if not name or not phone:
                skipped += 1
                continue

            # группа
            cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT(name) DO NOTHING", (group,))
            cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
            gid = cur.fetchone()[0]

            # контакт
            cur.execute("""
                INSERT INTO contacts(name, email, birthday, group_id)
                VALUES(%s, %s, %s, %s)
                ON CONFLICT(name) DO UPDATE
                    SET email    = EXCLUDED.email,
                        birthday = EXCLUDED.birthday,
                        group_id = EXCLUDED.group_id
                RETURNING id
            """, (name, email, birthday, gid))
            cid = cur.fetchone()[0]

            # телефон
            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES(%s, %s, %s)
                ON CONFLICT DO NOTHING
            """, (cid, phone, ptype))

            inserted += 1

    conn.commit()
    cur.close()
    print(f"✅ CSV импорт: добавлено {inserted}, пропущено {skipped}.")


# ── Добавить из консоли ─────────────────────────────────────
def add_from_console(conn):
    """Practice 7: ввод нового контакта вручную."""
    print("\n── Добавить контакт ──")
    name  = _input("Имя: ")
    if not name:
        print("⚠  Имя обязательно.")
        return

    phone = _input("Телефон: ")
    ptype = _input("Тип телефона (home/work/mobile) [mobile]: ", "mobile")
    email = _input("Email (Enter — пропустить): ") or None
    bday  = _input("День рождения (YYYY-MM-DD, Enter — пропустить): ") or None

    print("Группы: Family / Work / Friend / Other")
    group = _input("Группа [Other]: ", "Other")

    cur = conn.cursor()

    cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT(name) DO NOTHING", (group,))
    cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
    gid = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES(%s,%s,%s,%s)
        ON CONFLICT(name) DO UPDATE
            SET email=EXCLUDED.email, birthday=EXCLUDED.birthday, group_id=EXCLUDED.group_id
        RETURNING id
    """, (name, email, bday, gid))
    cid = cur.fetchone()[0]

    if phone:
        cur.execute("""
            INSERT INTO phones(contact_id, phone, type)
            VALUES(%s,%s,%s) ON CONFLICT DO NOTHING
        """, (cid, phone, ptype))

    conn.commit()
    cur.close()
    print(f"✅ Контакт '{name}' сохранён.")


# ── Обновить имя или телефон ────────────────────────────────
def update_contact(conn):
    """Practice 7: изменить имя или телефон."""
    print("\n── Обновить контакт ──")
    name = _input("Имя контакта: ")
    if not name:
        return

    cur = conn.cursor()
    cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
    row = cur.fetchone()
    if not row:
        print(f"⚠  Контакт '{name}' не найден.")
        cur.close()
        return
    cid = row[0]

    print("1. Изменить имя")
    print("2. Изменить телефон")
    print("3. Изменить email")
    print("4. Изменить день рождения")
    ch = _input("Выбор: ")

    if ch == "1":
        new_name = _input("Новое имя: ")
        if new_name:
            cur.execute("UPDATE contacts SET name=%s WHERE id=%s", (new_name, cid))
            print(f"✅ Имя изменено на '{new_name}'.")

    elif ch == "2":
        cur.execute("SELECT phone, type FROM phones WHERE contact_id=%s", (cid,))
        phones = cur.fetchall()
        if phones:
            print("Текущие телефоны:")
            for i, (p, t) in enumerate(phones, 1):
                print(f"  {i}. {p} ({t})")
            old = _input("Старый телефон (для замены): ")
            new_phone = _input("Новый телефон: ")
            if old and new_phone:
                cur.execute("UPDATE phones SET phone=%s WHERE contact_id=%s AND phone=%s",
                            (new_phone, cid, old))
                print("✅ Телефон обновлён.")
        else:
            new_phone = _input("Добавить телефон: ")
            ptype = _input("Тип (home/work/mobile) [mobile]: ", "mobile")
            if new_phone:
                cur.execute("INSERT INTO phones(contact_id,phone,type) VALUES(%s,%s,%s)",
                            (cid, new_phone, ptype))
                print("✅ Телефон добавлен.")

    elif ch == "3":
        new_email = _input("Новый email: ")
        cur.execute("UPDATE contacts SET email=%s WHERE id=%s", (new_email or None, cid))
        print("✅ Email обновлён.")

    elif ch == "4":
        new_bday = _input("Новая дата (YYYY-MM-DD): ")
        cur.execute("UPDATE contacts SET birthday=%s WHERE id=%s", (new_bday or None, cid))
        print("✅ День рождения обновлён.")

    conn.commit()
    cur.close()


# ── Удаление ────────────────────────────────────────────────
def delete_contact(conn):
    """Practice 7 + 8: удалить по имени или телефону через процедуру."""
    print("\n── Удалить контакт ──")
    print("1. По имени")
    print("2. По номеру телефона")
    ch = _input("Выбор: ")

    cur = conn.cursor()
    if ch == "1":
        name = _input("Имя: ")
        if name:
            cur.execute("CALL delete_contact(p_name => %s)", (name,))
            print(f"✅ Контакт '{name}' удалён.")
    elif ch == "2":
        phone = _input("Телефон: ")
        if phone:
            cur.execute("CALL delete_contact(p_phone => %s)", (phone,))
            print(f"✅ Контакт с телефоном '{phone}' удалён.")

    conn.commit()
    cur.close()


# ════════════════════════════════════════════════════════════
#  PRACTICE 8 — ФУНКЦИИ И ПРОЦЕДУРЫ
# ════════════════════════════════════════════════════════════

# ── Upsert через процедуру ──────────────────────────────────
def upsert_contact(conn):
    """Practice 8: вставить или обновить через процедуру БД."""
    print("\n── Upsert контакт ──")
    name  = _input("Имя: ")
    phone = _input("Телефон: ")
    ptype = _input("Тип (home/work/mobile) [mobile]: ", "mobile")

    if not name or not phone:
        print("⚠  Имя и телефон обязательны.")
        return

    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s, %s)", (name, phone, ptype))
    conn.commit()
    cur.close()
    print(f"✅ Контакт '{name}' — upsert выполнен.")


# ── Массовая вставка ────────────────────────────────────────
def bulk_insert(conn):
    """Practice 8: массовая вставка через процедуру БД."""
    print("\n── Массовая вставка (формат: Имя,Телефон на каждой строке, пустая строка — конец) ──")
    names, phones = [], []

    while True:
        line = input("  > ").strip()
        if not line:
            break
        parts = line.split(",")
        if len(parts) >= 2:
            names.append(parts[0].strip())
            phones.append(parts[1].strip())
        else:
            print("  ⚠  Формат: Имя,Телефон")

    if not names:
        return

    cur = conn.cursor()
    cur.execute("CALL bulk_insert_contacts(%s::varchar[], %s::varchar[], NULL)",
                (names, phones))
    # OUT параметр
    conn.commit()
    cur.close()
    print(f"✅ Обработано {len(names)} записей.")


# ── Поиск по паттерну (функция БД) ──────────────────────────
def search_by_pattern(conn):
    """Practice 8 + TSIS 1: поиск через функцию search_contacts."""
    query = _input("\nПоиск (имя / email / телефон): ")
    if not query:
        return

    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (query,))
    rows = cur.fetchall()
    cur.close()

    _print_table(rows, ["ID", "Имя", "Email", "Дата рожд.", "Группа", "Телефон", "Тип"])


# ── Пагинация (функция БД) ──────────────────────────────────
def paginated_view(conn):
    """Practice 8 + TSIS 1: навигация по страницам."""
    limit  = 5
    offset = 0

    while True:
        cur = conn.cursor()
        cur.execute("SELECT * FROM get_contacts_page(%s, %s)", (limit, offset))
        rows = cur.fetchall()
        cur.close()

        print(f"\n── Страница {offset // limit + 1} (записи {offset+1}–{offset+len(rows)}) ──")
        _print_table(rows, ["ID", "Имя", "Email", "Дата рожд.", "Группа", "Телефоны"])

        if not rows:
            print("  Больше записей нет.")
        print("  [n] следующая  [p] предыдущая  [q] выход")
        cmd = _input("  > ", "").lower()

        if cmd == "n":
            if len(rows) == limit:
                offset += limit
            else:
                print("  Вы на последней странице.")
        elif cmd == "p":
            offset = max(0, offset - limit)
        elif cmd == "q":
            break


# ════════════════════════════════════════════════════════════
#  TSIS 1 — РАСШИРЕННЫЕ ФУНКЦИИ
# ════════════════════════════════════════════════════════════

# ── Фильтр по группе ────────────────────────────────────────
def filter_by_group(conn):
    """TSIS 1: показать контакты одной группы."""
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM groups ORDER BY name")
    groups = cur.fetchall()
    print("\nДоступные группы:")
    for gid, gname in groups:
        print(f"  {gid}. {gname}")

    choice = _input("Номер группы: ")
    try:
        gid = int(choice)
    except ValueError:
        cur.close()
        return

    sort_field = _input("Сортировка (name/birthday/created) [name]: ", "name")
    allowed    = {"name": "c.name", "birthday": "c.birthday", "created": "c.created_at"}
    order_col  = allowed.get(sort_field, "c.name")

    cur.execute(f"""
        SELECT c.id, c.name, c.email, c.birthday, g.name AS grp,
               STRING_AGG(ph.phone || '(' || COALESCE(ph.type,'?') || ')', ', ') AS phones
        FROM contacts c
        LEFT JOIN groups g  ON g.id  = c.group_id
        LEFT JOIN phones ph ON ph.contact_id = c.id
        WHERE c.group_id = %s
        GROUP BY c.id, c.name, c.email, c.birthday, g.name, c.created_at
        ORDER BY {order_col}
    """, (gid,))
    rows = cur.fetchall()
    cur.close()

    _print_table(rows, ["ID", "Имя", "Email", "Дата рожд.", "Группа", "Телефоны"])


# ── Поиск по email ──────────────────────────────────────────
def search_by_email(conn):
    """TSIS 1: поиск по части email."""
    query = _input("\nEmail (часть): ")
    if not query:
        return

    cur = conn.cursor()
    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name,
               STRING_AGG(ph.phone, ', ')
        FROM contacts c
        LEFT JOIN groups g  ON g.id  = c.group_id
        LEFT JOIN phones ph ON ph.contact_id = c.id
        WHERE c.email ILIKE %s
        GROUP BY c.id, c.name, c.email, c.birthday, g.name
        ORDER BY c.name
    """, (f"%{query}%",))
    rows = cur.fetchall()
    cur.close()
    _print_table(rows, ["ID", "Имя", "Email", "Дата рожд.", "Группа", "Телефоны"])


# ── Добавить телефон к контакту ─────────────────────────────
def add_phone(conn):
    """TSIS 1: добавить телефон через процедуру add_phone."""
    print("\n── Добавить телефон ──")
    name  = _input("Имя контакта: ")
    phone = _input("Новый телефон: ")
    ptype = _input("Тип (home/work/mobile) [mobile]: ", "mobile")

    if not name or not phone:
        return

    cur = conn.cursor()
    try:
        cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
        conn.commit()
        print(f"✅ Телефон {phone} добавлен к '{name}'.")
    except psycopg2.errors.RaiseException as e:
        conn.rollback()
        print(f"⚠  {e}")
    finally:
        cur.close()


# ── Переместить в группу ────────────────────────────────────
def move_to_group(conn):
    """TSIS 1: переместить контакт в группу через процедуру."""
    print("\n── Переместить в группу ──")
    name  = _input("Имя контакта: ")
    group = _input("Группа (существующая или новая): ")

    if not name or not group:
        return

    cur = conn.cursor()
    try:
        cur.execute("CALL move_to_group(%s, %s)", (name, group))
        conn.commit()
        print(f"✅ '{name}' перемещён в группу '{group}'.")
    except psycopg2.errors.RaiseException as e:
        conn.rollback()
        print(f"⚠  {e}")
    finally:
        cur.close()


# ── Экспорт в JSON ──────────────────────────────────────────
def export_json(conn):
    """TSIS 1: экспорт всех контактов в JSON."""
    cur = conn.cursor()
    cur.execute("""
        SELECT c.id, c.name, c.email,
               c.birthday::TEXT, g.name AS grp, c.created_at::TEXT,
               COALESCE(
                   JSON_AGG(JSON_BUILD_OBJECT('phone', ph.phone, 'type', ph.type))
                   FILTER (WHERE ph.id IS NOT NULL), '[]'
               ) AS phones
        FROM contacts c
        LEFT JOIN groups g  ON g.id  = c.group_id
        LEFT JOIN phones ph ON ph.contact_id = c.id
        GROUP BY c.id, c.name, c.email, c.birthday, g.name, c.created_at
        ORDER BY c.name
    """)
    rows = cur.fetchall()
    cur.close()

    data = []
    for row in rows:
        data.append({
            "id":         row[0],
            "name":       row[1],
            "email":      row[2],
            "birthday":   row[3],
            "group":      row[4],
            "created_at": row[5],
            "phones":     row[6],
        })

    path = _input("Имя файла [contacts_export.json]: ", "contacts_export.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Экспортировано {len(data)} контактов → {path}")


# ── Импорт из JSON ──────────────────────────────────────────
def import_json(conn):
    """TSIS 1: импорт из JSON с обработкой дубликатов."""
    path = _input("Путь к JSON-файлу: ")
    if not path or not os.path.exists(path):
        print("⚠  Файл не найден.")
        return

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    cur = conn.cursor()
    inserted = skipped = overwritten = 0

    for entry in data:
        name = entry.get("name", "").strip()
        if not name:
            continue

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        exists = cur.fetchone()

        if exists:
            action = _input(f"  '{name}' уже есть. (s)кип / (o)верврайт [s]: ", "s").lower()
            if action != "o":
                skipped += 1
                continue
            # удаляем старый
            cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
            overwritten += 1

        # группа
        group = entry.get("group", "Other") or "Other"
        cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT(name) DO NOTHING", (group,))
        cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
        gid = cur.fetchone()[0]

        # контакт
        cur.execute("""
            INSERT INTO contacts(name, email, birthday, group_id)
            VALUES(%s,%s,%s,%s) RETURNING id
        """, (name, entry.get("email"), entry.get("birthday"), gid))
        cid = cur.fetchone()[0]

        # телефоны
        for ph in entry.get("phones", []):
            if ph.get("phone"):
                cur.execute("""
                    INSERT INTO phones(contact_id, phone, type)
                    VALUES(%s,%s,%s) ON CONFLICT DO NOTHING
                """, (cid, ph["phone"], ph.get("type", "mobile")))

        inserted += 1

    conn.commit()
    cur.close()
    print(f"✅ Импорт: добавлено {inserted}, перезаписано {overwritten}, пропущено {skipped}.")


# ════════════════════════════════════════════════════════════
#  ГЛАВНОЕ МЕНЮ
# ════════════════════════════════════════════════════════════

MENU = """

╔══════════════════════════════════════════╗
║           📖 PHONEBOOK MENU             
╠══════════════════════════════════════════╣
║  1.  Import from CSV                    ║
║  2.  Add contact (console)              ║
║  3.  Update contact                     ║
║  4.  Delete contact                     ║
╠══════════════════════════════════════════╣
║  5.  Upsert contact (procedure)         ║
║  6.  Bulk insert (procedure)            ║
║  7.  Pattern search (function)          ║
║  8.  Paginated view (function)          ║
╠══════════════════════════════════════════╣
║  9.  Filter by group                    ║
║  10. Search by email                    ║
║  11. Add phone to contact               ║
║  12. Move to group                      ║
║  13. Export to JSON                     ║
║  14. Import from JSON                   ║
╠══════════════════════════════════════════╣
║  0.  Exit                               ║
╚══════════════════════════════════════════╝
"""

def main():
    conn = None
    try:
        conn = get_conn()
        init_db(conn)
    except Exception as e:
        print(f"❌ Ошибка подключения к БД: {e}")
        sys.exit(1)

    actions = {
        "1":  lambda: import_csv(conn),
        "2":  lambda: add_from_console(conn),
        "3":  lambda: update_contact(conn),
        "4":  lambda: delete_contact(conn),
        "5":  lambda: upsert_contact(conn),
        "6":  lambda: bulk_insert(conn),
        "7":  lambda: search_by_pattern(conn),
        "8":  lambda: paginated_view(conn),
        "9":  lambda: filter_by_group(conn),
        "10": lambda: search_by_email(conn),
        "11": lambda: add_phone(conn),
        "12": lambda: move_to_group(conn),
        "13": lambda: export_json(conn),
        "14": lambda: import_json(conn),
    }

    while True:
        print(MENU)
        choice = _input("Выбор: ", "")

        if choice == "0":
            print("До свидания!")
            break

        action = actions.get(choice)
        if action:
            try:
                action()
            except Exception as e:
                conn.rollback()
                print(f"❌ Ошибка: {e}")
        else:
            print("⚠  Неверный выбор.")

    if conn:
        conn.close()


if __name__ == "__main__":
    main()