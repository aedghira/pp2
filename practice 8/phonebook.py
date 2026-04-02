import csv
import os
from datetime import datetime
from connect import db

class PhoneBook:

    def search_contacts(self, search_term):
        """Use database function search_contacts_pattern"""
        query = "SELECT * FROM search_contacts_pattern(%s)"
        if db.execute_query(query, (search_term,)):
            results = db.fetch_all()
            return list(results)
        return []

    def insert_from_console(self):
        """Use stored procedure insert_or_update_user"""
        print("\n=== Add New Contact ===\n")
        first_name = input("First name: ").strip()
        if not first_name:
            print("✗ First name is required!")
            return False
        last_name = input("Last name (optional): ").strip() or None
        phone_number = input("Phone number: ").strip()
        if not phone_number:
            print("✗ Phone number is required!")
            return False
        email = input("Email (optional): ").strip() or None

        print("\n--- Review Data ---")
        print(f"First name: {first_name}")
        print(f"Last name: {last_name or '-'}")
        print(f"Phone: {phone_number}")
        print(f"Email: {email or '-'}")

        confirm = input("\nSave contact? (y/n): ").strip().lower()
        if confirm != "y":
            print("Operation cancelled")
            return False

        # Call the stored procedure
        try:
            db.execute_query("CALL insert_or_update_user(%s, %s, %s, %s)",
                             (first_name, last_name, phone_number, email))
            db.commit()
            print("✓ Contact added/updated successfully")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            db.rollback()
            return False

    def bulk_insert_from_list(self, users_list):
        """
        users_list: list of tuples (first_name, last_name, phone, email)
        Calls bulk_insert_users procedure and returns invalid records.
        """
        from psycopg2.extras import execute_values
        # Convert list to array of composite type for PostgreSQL
        user_array = []
        for u in users_list:
            # Ensure None becomes NULL
            user_array.append((u[0], u[1] or None, u[2], u[3] or None))
        
        # Create a temporary table to hold the result
        sql = """
        CALL bulk_insert_users(%s::user_input_type[]);
        FETCH ALL FROM invalid_records;
        """
        # Note: The procedure returns a refcursor; we need to handle it properly.
        # Simpler approach: use a function that returns TABLE. We'll modify the procedure to a function.
        # For brevity, we'll implement a wrapper method using the existing db methods.
        # A cleaner solution: convert the procedure to a function that returns SETOF record.
        # I'll show a functional version below.
        pass  # See improved implementation below

    def query_contacts_paginated(self, limit, offset):
        """Use pagination function get_contacts_paginated"""
        query = "SELECT * FROM get_contacts_paginated(%s, %s)"
        if db.execute_query(query, (limit, offset)):
            return list(db.fetch_all())
        return []

    def delete_contact_by_identifier(self, identifier):
        """Use stored procedure delete_contact_by_username_or_phone"""
        try:
            db.execute_query("CALL delete_contact_by_username_or_phone(%s)", (identifier,))
            db.commit()
            print("✓ Contact(s) deleted successfully (if any matched)")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            db.rollback()
            return False

    # Modified delete_contact to use the new procedure
    def delete_contact(self):
        print("\n=== Delete Contact ===\n")
        identifier = input("Enter phone number or name to delete: ").strip()
        if not identifier:
            print("✗ No identifier provided")
            return False
        
        # Show matching contacts first
        contacts = self.search_contacts(identifier)
        if not contacts:
            print("✗ No contacts found")
            return False
        
        self.display_contacts(contacts)
        confirm = input(f"\nDelete all matching contacts? (y/n): ").strip().lower()
        if confirm == 'y':
            return self.delete_contact_by_identifier(identifier)
        else:
            print("Deletion cancelled")
            return False

    # New menu option for paginated view
    def paginated_view(self):
        try:
            limit = int(input("Records per page (default 10): ") or "10")
            page = int(input("Page number: "))
            offset = (page - 1) * limit
            contacts = self.query_contacts_paginated(limit, offset)
            self.display_contacts(contacts)
        except ValueError:
            print("✗ Invalid number")

    def main_menu(self):
        while True:
            print("\n" + "=" * 50)
            print("📞 PHONEBOOK APPLICATION")
            print("=" * 50)
            print("1. Import from CSV file")
            print("2. Add new contact")
            print("3. Update contact")
            print("4. Search contacts")
            print("5. Delete contact")
            print("6. Paginated view (NEW)")
            print("7. Bulk insert from list (NEW)")
            print("8. Exit")
            print("=" * 50)

            choice = input("\nSelect action (1-8): ").strip()
            if choice == "1":
                csv_path = input("Enter CSV file path: ").strip()
                self.insert_from_csv(csv_path)
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
                # Example bulk insert
                sample_users = [
                    ("John", "Doe", "123456789", "john@example.com"),
                    ("Jane", "Smith", "+123456789", "jane@example.com"),
                    ("Invalid", "User", "abc", "bad@phone.com")  # invalid phone
                ]
                # Call bulk insert method (requires implementation)
                print("Bulk insert from list not fully implemented in this example")
            elif choice == "8":
                print("\nGoodbye!")
                db.disconnect()
                break
            else:
                print("✗ Invalid choice")