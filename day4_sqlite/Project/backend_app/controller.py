from service import readAllMovies

def runApp():

    print("""
    Welcome to QA Cinema! 
    Please select an option from below: 
    1. Read All Movies
    2. UPDATE
    3. ????
    4. ????
    """
    )
    running = True

    # Does a thing while a condition is true
    while running:
        choice = int(input("Please select a choice using a number: "))
        if choice == 1:
            print(readAllMovies())
        else:
            print("Incorrect choice.. try again..")

        # To ask if they want to carry on using
        end_choice = input("Do you want to query more data Y / N: ")
        if end_choice.upper() == "N":
            running = False

# Exercise - Modularise your own project, with controller, service and repo files


runApp()