from service import read_all_animals, update_animal_name, delete_animal_id, add_data_animals
from repo import creating_table

def run_zoo_app():

    print("""
    Welcome to London Zoo! 
    Please select an option from below: 
    1. ADD ANIMALS 
    2. VIEW ANIMALS 
    3. UPDATE ANIMALS
    4. DELETE ANIMALS
    """
    )
    running = True

    while running:
        choice = int(input("Please select a choice using a number: "))
        if choice == 1:
            print(add_data_animals())
        elif choice == 2:
            print(read_all_animals())
        elif choice == 3:
            print(update_animal_name())
        elif choice == 4:
            print(delete_animal_id())
        else:
            print("Incorrect choice.. try again..")
        end_choice = input("Do you want to query more data Y / N: ")
        if end_choice.upper() == "N":
            running = False

# creating_table()
run_zoo_app()