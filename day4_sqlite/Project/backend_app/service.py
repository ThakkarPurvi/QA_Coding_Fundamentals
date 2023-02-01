# Service file is the business logic, and middle man
# Controller sends requests to service, service sends requests to repo

from repo import selectQuery

def readAllMovies():
    query = "SELECT * FROM movies"
    return selectQuery(query)