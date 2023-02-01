import sqlite3 as sql

conn = sql.connect("Zoo-db")
conn.execute("PRAGMA foreign_keys = 1 ")
cursor = conn.cursor()

def creating_table():
    sql_file = open("zoo.sql")
    sql_string = sql_file.read()
    # print(sql_string)
    # Running our sql command using our cursor
    cursor.executescript(sql_string)

# Reading data
def select_query(query):
    return cursor.execute(query).fetchall()

# Manipulating data
def data_query(query):
    cursor.execute(query)
    return True

def commit_changes():
    conn.commit()

