import csv
import os
from connect import db


class PhoneBook:
    """Main PhoneBook application class with automatic database setup"""

    def __init__(self):
        """Initialize application and setup database objects"""
        if db.connect():
            self.setup_database()
        else:
            print("Failed to connect to database. Exiting...")
            exit(1)

    # ------------------------------------------------------------------
    # Автоматическое создание всех необходимых объектов БД
    # ------------------------------------------------------------------
    def setup_database(self):
        """Create tables, triggers, functions, procedures if they don't exist"""
        db.execute_query("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100),
                phone_number VARCHAR(20) NOT NULL UNIQUE,
                email VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        db.execute_query("""
            CREATE OR REPLACE FUNCTION update_updated_at_column()
            RETURNS TRIGGER AS $$
            BEGIN
                NEW.updated_at = CURRENT_TIMESTAMP;
                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;
        """)

        db.execute_query("DROP TRIGGER IF EXISTS trigger_update_phonebook_updated_at ON phonebook;")
        db.execute_query("""
            CREATE TRIGGER trigger_update_phonebook_updated_at
            BEFORE UPDATE ON phonebook
            FOR EACH ROW
            EXECUTE FUNCTION update_updated_at_column();
        """)

        db.execute_query("""
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
                SELECT id INTO existing_id
                FROM phonebook
                WHERE first_name = p_first_name 
                  AND (last_name = p_last_name OR (last_name IS NULL AND p_last_name IS NULL))
                LIMIT 1;

                IF existing_id IS NOT NULL THEN
                    SELECT id INTO conflict_phone_id
                    FROM phonebook
                    WHERE phone_number = p_phone AND id != existing_id;
                    IF conflict_phone_id IS NOT NULL THEN
                        RAISE EXCEPTION 'Phone number % already belongs to another contact (ID %)', p_phone, conflict_phone_id;
                    END IF;

                    UPDATE phonebook
                    SET phone_number = p_phone,
                        email = COALESCE(p_email, email),
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = existing_id;
                ELSE
                    INSERT INTO phonebook (first_name, last_name, phone_number, email)
                    VALUES (p_first_name, p_last_name, p_phone, p_email);
                END IF;
            END;
            $$;
        """)

        db.execute_query("""
            CREATE OR REPLACE FUNCTION search_contacts_pattern(search_pattern TEXT)
            RETURNS TABLE(
                id INT,
                first_name VARCHAR,
                last_name VARCHAR,
                phone_number VARCHAR,
                email VARCHAR,
                created_at TIMESTAMP
            ) AS $$
            BEGIN
                RETURN QUERY
                SELECT p.id, p.first_name, p.last_name, p.phone_number, p.email, p.created_at
                FROM phonebook p
                WHERE p.first_name ILIKE '%' || search_pattern || '%'
                   OR p.last_name ILIKE '%' || search_pattern || '%'
                   OR p.phone_number ILIKE '%' || search_pattern || '%'
                ORDER BY p.first_name, p.last_name;
            END;
            $$ LANGUAGE plpgsql;
        """)

        db.execute_query("""
            CREATE OR REPLACE FUNCTION get_contacts_paginated(limit_val INT, offset_val INT)
            RETURNS TABLE(
                id INT,
                first_name VARCHAR,
                last_name VARCHAR,
                phone_number VARCHAR,
                email VARCHAR,
                created_at TIMESTAMP
            ) AS $$
            BEGIN
                RETURN QUERY
                SELECT p.id, p.first_name, p.last_name, p.phone_number, p.email, p.created_at
                FROM phonebook p
                ORDER BY p.first_name, p.last_name
                LIMIT limit_val
                OFFSET offset_val;
            END;
            $$ LANGUAGE plpgsql;
        """)

        db.execute_query("""
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
        """)

        db.commit()
        print("✓ Database setup completed (tables, functions, procedures)")

    # ------------------------------------------------------------------
    # Импорт из CSV
    # ------------------------------------------------------------------
    def insert_from_csv(self, csv_file_path):
        if not os.path.exists(csv_file_path):
            print(f"✗ File {csv_file_path} not found")
            return False

        insert_query = """
        INSERT INTO phonebook (first_name, last_name, phone_number, email)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (phone_number) DO UPDATE SET
            first_name = EXCLUDED.first_name,
            last_name = EXCLUDED.last_name,
            email = EXCLUDED.email,
            updated_at = CURRENT_TIMESTAMP
        RETURNING id
        """
        try:
            with open(csv_file_path, "r", encoding="utf-8") as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                inserted = 0
                updated = 0
                for row in csv_reader:
                    if len(row) >= 3:
                        first_name = row[0].strip()
                        last_name = row[1].strip() if len(row) > 1 and row[1].strip() else None
                        phone_number = row[2].strip()
                        email = row[3].strip() if len(row) > 3 and row[3].strip() else None
                        db.execute_query(insert_query, (first_name, last_name, phone_number, email))
                        result = db.fetch_one()
                        if result:
                            inserted += 1
                        else:
                            updated += 1
                db.commit()
                print(f"✓ CSV processed: {inserted} new, {updated} updated")
                return True
        except Exception as e:
            print(f"✗ CSV error: {e}")
            db.rollback()
            return False

    # ------------------------------------------------------------------
    # Добавление одного контакта
    # ------------------------------------------------------------------
    def insert_from_console(self):
        print("\n=== Add New Contact ===\n")
        first_name = input("First name: ").strip()
        if not first_name:
            print("✗ First name required")
            return False
        last_name = input("Last name (optional): ").strip() or None
        phone_number = input("Phone number: ").strip()
        if not phone_number:
            print("✗ Phone number required")
            return False
        email = input("Email (optional): ").strip() or None

        print("\n--- Review ---")
        print(f"Name: {first_name} {last_name or ''}")
        print(f"Phone: {phone_number}")
        print(f"Email: {email or '-'}")
        if input("\nSave? (y/n): ").strip().lower() != 'y':
            print("Cancelled")
            return False

        try:
            db.execute_query("CALL insert_or_update_user(%s, %s, %s, %s)",
                             (first_name, last_name, phone_number, email))
            db.commit()
            print("✓ Contact saved")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            db.rollback()
            return False

    # ------------------------------------------------------------------
    # Обновление контакта
    # ------------------------------------------------------------------
    def update_contact(self):
        print("\n=== Update Contact ===\n")
        search_term = input("Enter phone or name: ").strip()
        contacts = self.search_contacts(search_term)
        if not contacts:
            print("✗ No contacts found")
            return False

        self.display_contacts(contacts)
        try:
            choice = int(input("\nSelect number (0 - cancel): "))
            if choice == 0:
                return False
            contact = contacts[choice - 1]
        except (ValueError, IndexError):
            print("✗ Invalid selection")
            return False

        print(f"\nUpdating {contact['first_name']} {contact['last_name'] or ''}")
        new_first = input(f"New first name [{contact['first_name']}]: ").strip()
        new_phone = input(f"New phone [{contact['phone_number']}]: ").strip()

        updates = []
        params = []
        if new_first:
            updates.append("first_name = %s")
            params.append(new_first)
        if new_phone:
            db.execute_query("SELECT id FROM phonebook WHERE phone_number = %s AND id != %s",
                             (new_phone, contact['id']))
            if db.fetch_one():
                print(f"✗ Phone {new_phone} already used")
                return False
            updates.append("phone_number = %s")
            params.append(new_phone)

        if not updates:
            print("No changes")
            return False

        updates.append("updated_at = CURRENT_TIMESTAMP")
        params.append(contact['id'])
        query = f"UPDATE phonebook SET {', '.join(updates)} WHERE id = %s"
        if db.execute_query(query, params):
            db.commit()
            print("✓ Contact updated")
            return True
        return False

    # ------------------------------------------------------------------
    # Поиск через функцию
    # ------------------------------------------------------------------
    def search_contacts(self, search_term):
        query = "SELECT * FROM search_contacts_pattern(%s)"
        if db.execute_query(query, (search_term,)):
            return list(db.fetch_all())
        return []

    # ------------------------------------------------------------------
    # Меню поиска
    # ------------------------------------------------------------------
    def query_contacts(self):
        print("\n=== Search ===\n")
        print("1. By name/phone (pattern)")
        print("2. By full phone")
        print("3. By prefix")
        print("4. Show all")
        print("5. Back")
        choice = input("\nChoice: ").strip()
        if choice == "1":
            pattern = input("Pattern: ").strip()
            self.display_contacts(self.search_contacts(pattern))
        elif choice == "2":
            phone = input("Phone: ").strip()
            db.execute_query("SELECT * FROM phonebook WHERE phone_number = %s", (phone,))
            self.display_contacts(db.fetch_all())
        elif choice == "3":
            prefix = input("Prefix: ").strip()
            db.execute_query("SELECT * FROM phonebook WHERE phone_number LIKE %s", (f"{prefix}%",))
            self.display_contacts(db.fetch_all())
        elif choice == "4":
            db.execute_query("SELECT * FROM phonebook ORDER BY first_name")
            self.display_contacts(db.fetch_all())
        elif choice == "5":
            return
        else:
            print("✗ Invalid")

    # ------------------------------------------------------------------
    # Удаление через процедуру
    # ------------------------------------------------------------------
    def delete_contact(self):
        print("\n=== Delete Contact ===\n")
        identifier = input("Enter phone or name: ").strip()
        if not identifier:
            return False
        contacts = self.search_contacts(identifier)
        if not contacts:
            print("✗ No contacts")
            return False
        self.display_contacts(contacts)
        if input(f"\nDelete all matching? (y/n): ").strip().lower() == 'y':
            try:
                db.execute_query("CALL delete_contact_by_username_or_phone(%s)", (identifier,))
                db.commit()
                print("✓ Deleted")
                return True
            except Exception as e:
                print(f"✗ Error: {e}")
                db.rollback()
        else:
            print("Cancelled")
        return False

    # ------------------------------------------------------------------
    # Пагинация через функцию
    # ------------------------------------------------------------------
    def paginated_view(self):
        try:
            limit = int(input("Records per page (default 10): ") or "10")
            page = int(input("Page number: "))
            offset = (page - 1) * limit
            query = "SELECT * FROM get_contacts_paginated(%s, %s)"
            if db.execute_query(query, (limit, offset)):
                self.display_contacts(db.fetch_all())
            else:
                print("✗ Failed")
        except ValueError:
            print("✗ Invalid number")

    # ------------------------------------------------------------------
    # МАССОВАЯ ВСТАВКА с интерактивным вводом
    # ------------------------------------------------------------------
    def input_contacts_for_bulk(self):
        """Интерактивный ввод списка контактов для массовой вставки"""
        print("\n=== Bulk Insert: Enter contacts ===\n")
        print("Enter contact data in format: first_name, last_name, phone, email")
        print("Last name and email are optional (press Enter to skip)")
        print("Leave first_name empty to finish input.\n")

        contacts = []
        count = 1
        while True:
            print(f"--- Contact #{count} ---")
            first = input("First name: ").strip()
            if not first:
                if count == 1:
                    print("No contacts entered.")
                break

            last = input("Last name (optional): ").strip() or None
            phone = input("Phone number: ").strip()
            if not phone:
                print("Phone number is required. Contact skipped.")
                continue
            email = input("Email (optional): ").strip() or None

            contacts.append((first, last, phone, email))
            count += 1
            print()  # empty line

        if contacts:
            print(f"\nCollected {len(contacts)} contacts. Processing...")
            self.bulk_insert_from_list(contacts)
        else:
            print("No contacts to insert.")

    def bulk_insert_from_list(self, users_list):
        """
        users_list: список кортежей (first_name, last_name, phone, email)
        """
        if not users_list:
            return

        from psycopg2.extras import execute_values

        # 1. Создаём временные таблицы
        try:
            db.execute_query("""
                CREATE TEMP TABLE bulk_input (
                    first_name VARCHAR,
                    last_name VARCHAR,
                    phone_number VARCHAR,
                    email VARCHAR
                );
            """)
            db.execute_query("""
                CREATE TEMP TABLE bulk_errors (
                    first_name VARCHAR,
                    last_name VARCHAR,
                    phone_number VARCHAR,
                    email VARCHAR,
                    error_reason TEXT
                );
            """)
        except Exception as e:
            print(f"✗ Failed to create temp tables: {e}")
            return

        # 2. Вставляем данные через execute_values
        insert_sql = "INSERT INTO bulk_input (first_name, last_name, phone_number, email) VALUES %s"
        data = [(u[0], u[1], u[2], u[3]) for u in users_list]

        try:
            cur = db.conn.cursor()
            execute_values(cur, insert_sql, data)
            db.conn.commit()
        except Exception as e:
            print(f"✗ Failed to insert into temp table: {e}")
            db.rollback()
            return

        # 3. Обрабатываем записи
        process_sql = """
        DO $$
        DECLARE
            r RECORD;
            phone_valid BOOLEAN;
        BEGIN
            FOR r IN SELECT * FROM bulk_input LOOP
                phone_valid := (r.phone_number ~ '^[+\-0-9\(\)\s]+$' AND length(r.phone_number) BETWEEN 5 AND 20);
                IF NOT phone_valid THEN
                    INSERT INTO bulk_errors (first_name, last_name, phone_number, email, error_reason)
                    VALUES (r.first_name, r.last_name, r.phone_number, r.email, 'Invalid phone number format');
                ELSE
                    BEGIN
                        CALL insert_or_update_user(r.first_name, r.last_name, r.phone_number, r.email);
                    EXCEPTION WHEN OTHERS THEN
                        INSERT INTO bulk_errors (first_name, last_name, phone_number, email, error_reason)
                        VALUES (r.first_name, r.last_name, r.phone_number, r.email, SQLERRM);
                    END;
                END IF;
            END LOOP;
        END;
        $$;
        SELECT * FROM bulk_errors;
        """
        try:
            db.execute_query(process_sql)
            errors = db.fetch_all()
            db.commit()
        except Exception as e:
            print(f"✗ Error during bulk processing: {e}")
            db.rollback()
            return

        if errors:
            print("\n⚠️ Some records were not inserted/updated:")
            for err in errors:
                print(f"  {err['first_name']} {err['last_name'] or ''} | {err['phone_number']} | Error: {err['error_reason']}")
        else:
            print("✓ All records processed successfully.")

    # ------------------------------------------------------------------
    # Отображение таблицы
    # ------------------------------------------------------------------
    def display_contacts(self, contacts):
        if not contacts:
            print("\nNo contacts found.")
            return
        print("\n" + "=" * 100)
        print(f"{'ID':<5} {'First Name':<20} {'Last Name':<20} {'Phone Number':<15} {'Email':<30}")
        print("=" * 100)
        for c in contacts:
            print(f"{c['id']:<5} {c['first_name']:<20} {c['last_name'] or '-':<20} {c['phone_number']:<15} {c.get('email') or '-':<30}")
        print("=" * 100)
        print(f"Total: {len(contacts)} contacts\n")

    # ------------------------------------------------------------------
    # Главное меню
    # ------------------------------------------------------------------
    def main_menu(self):
        while True:
            print("\n" + "=" * 50)
            print("📞 PHONEBOOK APPLICATION")
            print("=" * 50)
            print("1. Import from CSV")
            print("2. Add new contact")
            print("3. Update contact")
            print("4. Search contacts")
            print("5. Delete contact")
            print("6. Paginated view")
            print("7. Bulk insert from list (interactive input)")
            print("8. Exit")
            print("=" * 50)
            choice = input("\nSelect (1-8): ").strip()
            if choice == "1":
                path = input("CSV path: ").strip()
                self.insert_from_csv(path)
            elif choice == "2":
                self.insert_from_console()
            elif choice == "3":
                self.update_contact()
            elif choice == "4":
                self.query_contacts()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                self.paginated_view()
            elif choice == "7":
                self.input_contacts_for_bulk()
            elif choice == "8":
                print("\nGoodbye!")
                db.disconnect()
                break
            else:
                print("✗ Invalid choice")


def main():
    app = PhoneBook()
    app.main_menu()


if __name__ == "__main__":
    main()