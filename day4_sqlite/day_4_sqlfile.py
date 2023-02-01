import sqlite3 as sql                   # Sqlite is an embedded local DB, that is installed in Python by default

                                        # Creating a connection object, by running the connect() function
conn = sql.connect("Zoo-db")            # If this file doesn't exist, create it. If it does, connect to it

cursor = conn.cursor()                   # Making a cursor running the cursor() function that belongs to our conn object
conn.execute("PRAGMA foreign_keys = 1")


""" =================== CREATE TABLE ====================== """
def create_table():
    sql_file = open("zoo.sql")            # Reading our sql file
    sql_string = sql_file.read()
    # print(sql_string)
    cursor.executescript(sql_string)  # Running our sql command using our cursor
# create_table()
print(cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())          # reading the tables in the db


# Create, Read, Update, Delete

""" =================== INSERT SINGLE VALUES TO MULTIPLE TABLES (single) ====================== """

def addData():
    query = "INSERT INTO <table name> (field_1, field_2, field_3) VALUES ('value_1', value_2, value_3);"
    enclosures_query = "INSERT INTO enclosures " \
                       "(enclosure_name,enclosure_area, no_of_animals,wild_type)" \
                       "VALUES ('Yellow Zone', 500, 30, false);"
    animals_query = "INSERT INTO animals " \
                    "(enclosure_id, animal_name, trophic_level, life_span) " \
                    "VALUES (4, 'Gorilla','Herbivores', 40);"

    cursor.execute(enclosures_query)
    cursor.execute(animals_query)
    select_query = "SELECT * FROM enclosures"                       # Reading data from DBs, SELECT * what columns to see,
    print(cursor.execute(select_query).fetchall())                  # cursor selects the data, fetchAll() imports it to python
    print(cursor.execute("SELECT * FROM animals").fetchall())

addData()


""" =================== ADD VALUES TO SINGLE TABLE (enclosures) ====================== """

def add_data_enclosures():
    # query = "INSERT INTO <table name> (field_1, field_2, field_3) VALUES ('value_1', value_2, value_3);"
    enclosures_query = "INSERT INTO enclosures " \
                       "(enclosure_name,enclosure_area, no_of_animals,wild_type)" \
                       "VALUES ('Yellow Zone', 500, 30, false);"
    cursor.execute(enclosures_query)
    return True
add_data_enclosures()



""" =================== ADD VALUES TO SINGLE TABLE (animals) ====================== """
def add_data_animals():
    # query = "INSERT INTO <table name> (field_1, field_2, field_3) VALUES ('value_1', value_2, value_3);"
    animals_query = "INSERT INTO animals " \
                    "(enclosure_id, animal_name, trophic_level, life_span) " \
                    "VALUES (2, 'Gorilla','Herbivores', 40),;"
    cursor.execute(animals_query)
    return True
add_data_animals()


# Exercise - Implement a function that gets an animal by animal id (pass in id)

print(read_all_data("SELECT * FROM animals WHERE animal_id < 4"))




# Create a function that gets all records from one condition the user can set (pass in field and value)
# Saves your changes to the DB


""" =================== READ DATA  ====================== """
def read_all_data(table_animals):
    select_query = f"SELECT * FROM {table_animals}"
    return cursor.execute(select_query).fetchall()

def read_animals():
    animal_id = input("Please choose ID: ")
    query = f"SELECT * FROM enclosures WHERE animal_id = {animal_id}"
    return read_all_query(query)

print(read_all_data("enclosures"))
print(read_all_data("animals"))

""" =================== READ ALL ENCLOSURE NAME ===================== """

def read_all_enclosure_name(enclosure_name):
    query = f"SELECT * FROM enclosures WHERE enclosure ='{enclosure_name}'"
    return read_all_query(query)
print(read_all_enclosure_name("enclosures"))


""" =================== READ ALL ENCLOSURES ===================== """
def read_all_enclosures():
    query = "SELECT * FROM enclosures"
    return read_all_query(query)
print(read_all_enclosures())



""" =================== READ ALL ANIMALS ===================== """
def read_all_animals():
    query = "SELECT * FROM animals"
    return read_all_query(query)
print(read_all_animals())



""" =================== COMMON FOR ALL QUERIES ===================== """
def read_all_query(query):                      # Read all data to print in the console
    return cursor.execute(query).fetchall()

def data_query(query):          # Creating the data query whilw you want the database to execute some function
    cursor.execute(query)
    return True





""" =================== UPDATE ========================== """
def update_animal_name(animal_id, animal_name):
    # Every animal name will be updated to the new name, what can I do to choose a animal to update
    query = f"UPDATE enclosures SET animal_name = '{animal_name}' WHERE animal_id = {animal_id}"
    return data_query(query)
# print(update_animal_name(sxj))




""" =================== DELETE ========================== """
def delete_animal_id(animal_id):
    query = f"DELETE FROM animals where animal_id = {animal_id}"
    return data_query(query)
# print(delete_animal_id(5))


print(read_all_data("enclosures"))
print(read_all_data("animals"))

conn.commit()
