-- Helper type for bulk insertion (composite type)
CREATE TYPE user_input_type AS (
    first_name VARCHAR,
    last_name VARCHAR,
    phone_number VARCHAR,
    email VARCHAR
);

-- Procedure 1: Insert or update a single user by name (first+last) and phone
-- If a user with the same first_name and last_name exists, update their phone number.
-- If the new phone number already belongs to another contact, raise an exception.
CREATE OR REPLACE PROCEDURE insert_or_update_user(
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_phone VARCHAR,
    p_email VARCHAR DEFAULT NULL
) LANGUAGE plpgsql AS $$
DECLARE
    existing_id INT;
    conflict_phone_id INT;
BEGIN
    -- Check if a contact with the same first_name and last_name exists
    SELECT id INTO existing_id
    FROM phonebook
    WHERE first_name = p_first_name AND (last_name = p_last_name OR (last_name IS NULL AND p_last_name IS NULL))
    LIMIT 1;

    IF existing_id IS NOT NULL THEN
        -- Check if the new phone is already used by another contact
        SELECT id INTO conflict_phone_id
        FROM phonebook
        WHERE phone_number = p_phone AND id != existing_id;
        IF conflict_phone_id IS NOT NULL THEN
            RAISE EXCEPTION 'Phone number % already belongs to another contact (ID %)', p_phone, conflict_phone_id;
        END IF;

        -- Update phone number (and email if provided)
        UPDATE phonebook
        SET phone_number = p_phone,
            email = COALESCE(p_email, email),
            updated_at = CURRENT_TIMESTAMP
        WHERE id = existing_id;
    ELSE
        -- Insert new contact
        INSERT INTO phonebook (first_name, last_name, phone_number, email)
        VALUES (p_first_name, p_last_name, p_phone, p_email);
    END IF;
END;
$$;

-- Procedure 2: Bulk insert/update many users from a list (array of user_input_type)
-- Validates phone number format (simple regex: must contain only digits, spaces, '+', '-', parentheses)
-- Returns a table of invalid records (original data + error reason)
CREATE OR REPLACE PROCEDURE bulk_insert_users(
    users user_input_type[],
    INOUT invalid_records TABLE (first_name VARCHAR, last_name VARCHAR, phone_number VARCHAR, email VARCHAR, error_reason TEXT)
) LANGUAGE plpgsql AS $$
DECLARE
    u user_input_type;
    phone_valid BOOLEAN;
BEGIN
    -- Create temporary table to collect invalid records
    CREATE TEMP TABLE temp_invalid (
        first_name VARCHAR,
        last_name VARCHAR,
        phone_number VARCHAR,
        email VARCHAR,
        error_reason TEXT
    ) ON COMMIT DROP;

    FOREACH u IN ARRAY users LOOP
        -- Validate phone number: allow digits, spaces, +, -, parentheses; length between 5 and 20
        phone_valid := (u.phone_number ~ '^[+\-0-9\(\)\s]+$' AND length(u.phone_number) BETWEEN 5 AND 20);

        IF NOT phone_valid THEN
            INSERT INTO temp_invalid VALUES (u.first_name, u.last_name, u.phone_number, u.email, 'Invalid phone number format');
        ELSE
            -- Try to insert/update using the single-user procedure; catch exceptions
            BEGIN
                CALL insert_or_update_user(u.first_name, u.last_name, u.phone_number, u.email);
            EXCEPTION WHEN OTHERS THEN
                INSERT INTO temp_invalid VALUES (u.first_name, u.last_name, u.phone_number, u.email, SQLERRM);
            END;
        END IF;
    END LOOP;

    -- Return the invalid records
    RETURN QUERY SELECT * FROM temp_invalid;
END;
$$;

-- Procedure 3: Delete contact by username (first or last name) or phone number
CREATE OR REPLACE PROCEDURE delete_contact_by_username_or_phone(identifier TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = identifier
       OR last_name = identifier
       OR phone_number = identifier;
    
    IF NOT FOUND THEN
        RAISE NOTICE 'No contact found matching "%"', identifier;
    END IF;
END;
$$;