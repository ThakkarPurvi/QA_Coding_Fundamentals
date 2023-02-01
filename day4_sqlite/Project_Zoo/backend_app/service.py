from repo import select_query, data_query, cursor

""" ======== READ ======== """
def read_all_animals():
    query = "SELECT * FROM animals"
    return select_query(query)


""" ======== UPDATE ======== """
def update_animal_name(animal_id, animal_name):
    # Every animal name will be updated to the new name, what can I do to choose a animal to update
    query = f"UPDATE enclosures SET animal_name = '{animal_name}' WHERE animal_id = {animal_id}"
    return data_query(query)
# print(update_animal_name(animal_name="monkey"))


""" ======== DELETE ======== """
def delete_animal_id(animal_id):
    query = f"DELETE FROM animals where animal_id = {animal_id}"
    return data_query(query)
# print(delete_animal_id())


""" ======== ADD ======== """
def add_data_animals():
    animals_query = "INSERT INTO animals " \
                    "(enclosure_id, animal_name, trophic_level, life_span) " \
                    "VALUES (2, 'Gorilla','Herbivores', 40),;"
    cursor.execute(animals_query)
    return True
add_data_animals()

