import sqlite3

def database():
    return sqlite3.connect("Connection/sqlite3.db")

def get(query):
    conn = database()
    cursor = conn.cursor()
    cursor.execute(query)#f"SELECT * FROM {tabla}"
    result = cursor.fetchall()
    conn.close()
    return result