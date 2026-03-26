"""
Database configuration for PhoneBook application
"""


DB_CONFIG = {
    'host': 'localhost',          
    'port': 5432,               
    'database': 'phonebook_db',
    'user': 'postgres',           
    'password': 'your_password'  
}

APP_CONFIG = {
    'csv_encoding': 'utf-8',      
    'date_format': '%Y-%m-%d %H:%M:%S',
    'max_name_length': 100,
    'max_phone_length': 20
}