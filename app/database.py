import psycopg2
from psycopg2 import pool

DB_HOST = 'db'
DB_PORT = 5432
DB_NAME = 'shopboard_db'
DB_USER = 'dashboard_admin'
DB_PASSWORD = 'dash_pwd123'

_db_pool = None

def get_pool():
    global _db_pool
    if _db_pool is None:
        _db_pool = psycopg2.pool.SimpleConnectionPool(1, 10,
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD)
    return _db_pool

def get_connection():
    pool = get_pool()
    return pool.getconn()

def put_connection(conn):
    pool = get_pool()
    pool.putconn(conn)
