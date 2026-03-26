import csv
import os
from datetime import datetime
from connect import db


class PhoneBook:
    """Main PhoneBook application class"""
    
    def __init__(self):
        """Initialize application and database connection"""
        self.initialize_database()
    
    def initialize_database(self):
        """Initialize database connection and create tables"""
        if db.connect():
            db.create_table()
        else:
            print("Failed to connect to database. Exiting...")
            exit(1)
    
    def insert_from_csv(self, csv_file_path):
        """
        Insert data from CSV file
        
        CSV format: first_name,last_name,phone_number,email
        """
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
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)  # Skip header row
                
                inserted = 0
                updated = 0
                
                for row in csv_reader:
                    if len(row) >= 3:
                        first_name = row[0].strip()
                        last_name = row[1].strip() if len(row) > 1 and row[1].strip() else None
                        phone_number = row[2].strip()
                        email = row[3].strip() if len(row) > 3 and row[3].strip() else None
                        
                        db.execute_query(insert_query, 
                                       (first_name, last_name, phone_number, email))
                        result = db.fetch_one()
                        
                        if result:
                            inserted += 1
                        else:
                            updated += 1
                
                db.commit()
                print(f"✓ Successfully processed: {inserted} new, {updated} updated contacts")
                return True
                
        except Exception as e:
            print(f"✗ Error importing CSV: {e}")
            db.rollback()
            return False
    
    def insert_from_console(self):
        """Insert new contact from console input"""
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
        if confirm != 'y':
            print("Operation cancelled")
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
        
        if db.execute_query(insert_query, (first_name, last_name, phone_number, email)):
            result = db.fetch_one()
            db.commit()
            print(f"✓ Contact added successfully with ID: {result['id']}")
            return True
        
        return False
    
    def update_contact(self):
        """Update contact information"""
        print("\n=== Update Contact ===\n")
        
        
        search_term = input("Enter phone number or name to search: ").strip()
        contacts = self.search_contacts(search_term)
        
        if not contacts:
            print("✗ No contacts found")
            return False
        
        
        self.display_contacts(contacts)
        try:
            choice = int(input("\nSelect contact number to update (0 - cancel): "))
            if choice == 0:
                return False
            contact = contacts[choice - 1]
        except (ValueError, IndexError):
            print("✗ Invalid selection")
            return False
        
        print(f"\nUpdating contact: {contact['first_name']} {contact['last_name'] or ''}")
        print("Leave field empty to keep current value\n")
        
        
        new_first_name = input(f"New first name [{contact['first_name']}]: ").strip()
        new_phone = input(f"New phone number [{contact['phone_number']}]: ").strip()
        
        
        updates = []
        params = []
        
        if new_first_name:
            updates.append("first_name = %s")
            params.append(new_first_name)
        
        if new_phone:
            
            check_query = "SELECT id FROM phonebook WHERE phone_number = %s AND id != %s"
            db.execute_query(check_query, (new_phone, contact['id']))
            if db.fetch_one():
                print(f"✗ Phone number {new_phone} is already used by another contact")
                return False
            updates.append("phone_number = %s")
            params.append(new_phone)
        
        if not updates:
            print("No changes made")
            return False
        
        updates.append("updated_at = CURRENT_TIMESTAMP")
        params.append(contact['id'])
        
        
        update_query = f"UPDATE phonebook SET {', '.join(updates)} WHERE id = %s"
        
        if db.execute_query(update_query, params):
            db.commit()
            print("✓ Contact updated successfully")
            return True
        
        return False
    
    def search_contacts(self, search_term):
        """Search contacts by name or phone number"""
        search_query = """
        SELECT id, first_name, last_name, phone_number, email, created_at
        FROM phonebook
        WHERE first_name ILIKE %s 
           OR last_name ILIKE %s 
           OR phone_number ILIKE %s
        ORDER BY first_name, last_name
        """
        
        search_pattern = f"%{search_term}%"
        
        if db.execute_query(search_query, (search_pattern, search_pattern, search_pattern)):
            results = db.fetch_all()
            return list(results)
        return []
    
    def query_contacts(self):
        """Query contacts with different filters"""
        print("\n=== Search Contacts ===\n")
        print("1. Search by name")
        print("2. Search by full phone number")
        print("3. Search by phone prefix")
        print("4. Show all contacts")
        print("5. Back to main menu")
        
        choice = input("\nSelect search type (1-5): ").strip()
        
        if choice == '1':
            name = input("Enter name to search: ").strip()
            contacts = self.search_contacts(name)
            self.display_contacts(contacts)
        
        elif choice == '2':
            phone = input("Enter phone number: ").strip()
            query = "SELECT * FROM phonebook WHERE phone_number = %s"
            if db.execute_query(query, (phone,)):
                contacts = db.fetch_all()
                self.display_contacts(contacts)
        
        elif choice == '3':
            prefix = input("Enter phone prefix (e.g., +7, 8, 777): ").strip()
            query = "SELECT * FROM phonebook WHERE phone_number LIKE %s"
            if db.execute_query(query, (f"{prefix}%",)):
                contacts = db.fetch_all()
                self.display_contacts(contacts)
        
        elif choice == '4':
            query = "SELECT * FROM phonebook ORDER BY first_name"
            if db.execute_query(query):
                contacts = db.fetch_all()
                self.display_contacts(contacts)
        
        elif choice == '5':
            return
        
        else:
            print("✗ Invalid selection")
    
    def delete_contact(self):
        """Delete a contact by name or phone number"""
        print("\n=== Delete Contact ===\n")
        
      
        search_term = input("Enter phone number or name to delete: ").strip()
        contacts = self.search_contacts(search_term)
        
        if not contacts:
            print("✗ No contacts found")
            return False
        
      
        self.display_contacts(contacts)
        try:
            choice = int(input("\nSelect contact number to delete (0 - cancel): "))
            if choice == 0:
                return False
            contact = contacts[choice - 1]
        except (ValueError, IndexError):
            print("✗ Invalid selection")
            return False
        
      
        confirm = input(f"\nDelete contact {contact['first_name']} {contact['last_name'] or ''}? (y/n): ").strip().lower()
        
        if confirm == 'y':
            delete_query = "DELETE FROM phonebook WHERE id = %s"
            if db.execute_query(delete_query, (contact['id'],)):
                db.commit()
                print("✓ Contact deleted successfully")
                return True
        else:
            print("Deletion cancelled")
        
        return False
    
    def display_contacts(self, contacts):
        """Display contacts in a formatted table"""
        if not contacts:
            print("\nNo contacts found.")
            return
        
        print("\n" + "=" * 100)
        print(f"{'ID':<5} {'First Name':<20} {'Last Name':<20} {'Phone Number':<15} {'Email':<30}")
        print("=" * 100)
        
        for contact in contacts:
            print(f"{contact['id']:<5} "
                  f"{contact['first_name']:<20} "
                  f"{contact['last_name'] or '-':<20} "
                  f"{contact['phone_number']:<15} "
                  f"{contact.get('email') or '-':<30}")
        
        print("=" * 100)
        print(f"Total: {len(contacts)} contacts\n")
    
    def main_menu(self):
        """Display main menu and handle user input"""
        while True:
            print("\n" + "=" * 50)
            print("📞 PHONEBOOK APPLICATION")
            print("=" * 50)
            print("1. Import from CSV file")
            print("2. Add new contact")
            print("3. Update contact")
            print("4. Search contacts")
            print("5. Delete contact")
            print("6. Exit")
            print("=" * 50)
            
            choice = input("\nSelect action (1-6): ").strip()
            
            if choice == '1':
                csv_path = input("Enter CSV file path: ").strip()
                self.insert_from_csv(csv_path)
            
            elif choice == '2':
                self.insert_from_console()
            
            elif choice == '3':
                self.update_contact()
            
            elif choice == '4':
                self.query_contacts()
            
            elif choice == '5':
                self.delete_contact()
            
            elif choice == '6':
                print("\nGoodbye!")
                db.disconnect()
                break
            
            else:
                print("✗ Invalid choice. Please select 1-6")


def main():
    """Application entry point"""
    app = PhoneBook()
    app.main_menu()


if __name__ == "__main__":
    main()