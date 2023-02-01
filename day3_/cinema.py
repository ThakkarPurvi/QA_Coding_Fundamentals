import sqlite3 as sql

conn = sql.connect("cinema-db")

conn.execute("PRAGMA foreign_keys = 1")

cursor = conn.cursor()


def creatingTable():
    sql_file = open("cinema.sql")
    sql_string = sql_file.read()
    # print(sql_string)
    # Running our sql command using our cursor
    cursor.executescript(sql_string)


# creatingTable()

def insertMovie():
    movie_title = input("Please enter movie title: ")
    movie_query = f"INSERT INTO movies (movie_title, genre, third_dimension_film) VALUES ('{movie_title}', 'HOR', true);"
    cursor.execute(movie_query)
    return True


def insertTicket(movie_id):
    ticket_query = f"INSERT INTO tickets (movie_id, number_tickets, ticket_name) VALUES ({movie_id}, 5, 'Wesley Snipes');"
    cursor.execute(ticket_query)
    return True


# Reading data
def selectQuery(query):
    return cursor.execute(query).fetchall()


# Changing / manipulating data
def dataQuery(query):
    cursor.execute(query)
    return True


def readAllMovies():
    query = "SELECT * FROM movies"
    return selectQuery(query)


def readAllTickets():
    query = "SELECT * FROM tickets"
    return selectQuery(query)


def deleteTicketId(id):
    query = f"DELETE FROM tickets where ticket_id = {id}"
    return dataQuery(query)


def updateMovieTitleId(id, title):
    # Every movie will be updated to the new title, what can I do to choose a movie to update
    query = f"UPDATE movies SET movie_title = '{title}' WHERE movie_id = {id}"
    return dataQuery(query)


# My cinema app doesn't persist data, and doesn't let me choose what I want to do or add my own data
# CRUD (Create, Read, Update, Delete) Uses the terminal to ask what input the user would like to do
# The user should be able to Add data to table 1, add to table 2, read all data from table1, read by id table 1, update by id one field in table 1, and delete by id in table 1

"""
    Recommend: 
    Some form of large printing, asking the user what they would like to do
    some input fields where the user can choose
    If else / to run a function, which does said thing 
    Some form of while loop to keep the user from adding and reading data til they want to end 
"""

print("Welcome to Cinema / zoo, what would you like to do?; ")
print("1. Add a movie")

print(readAllMovies())
print(readAllTickets())
deleteTicketId(2)
print(readAllTickets())

