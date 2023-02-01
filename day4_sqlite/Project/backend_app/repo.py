import sqlite3 as sql

conn = sql.connect("cinema-db")
conn.execute("PRAGMA foreign_keys = 1 ")
cursor = conn.cursor()

def creatingTable():
    sql_file = open("cinema.sql")
    sql_string = sql_file.read()
    # print(sql_string)
    # Running our sql command using our cursor
    cursor.executescript(sql_string)

# Reading data
def selectQuery(query):
    return cursor.execute(query).fetchall()

# Manipulating data
def dataQuery(query):
    cursor.execute(query)
    return True

def commitChanges():
    conn.commit()