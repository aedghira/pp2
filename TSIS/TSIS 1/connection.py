import psycopg2
from config import DB_CONFIG

def get_conn():
    return psycopg2.connect(**DB_CONFIG)

def get_cursor(conn):
    return conn.cursor()