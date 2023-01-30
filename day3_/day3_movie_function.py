# Exercise - Create a function that asks the user to input the following :
# name, movie_seeing, number_seats, VIP seats (save as a string)
# Create a bookings.txt file and push the data to the file persisting the data

m = ("./movie.txt")

# def count():
#     for i in range(100):
#         i += 1
#     return i

def count():
    count.counter += 1
    print(count.counter)
count.counter = 0

def movie_booking():
    booker = input("What is your name?: ")
    movie_name = input("Which Movie would you like to book?: ")
    seat_no = int(input("How many seats would you like to book?: "))
    vip_seat = input("Would you like to book VIP Seats?: ")

    with open("./movie.txt", "a") as m:
        m.write(f"Booking No:{(count())}\nName: {booker}\nMovie Name: {movie_name}\nSeat No: {seat_no}\nVIP Seats: {vip_seat}\n=============\n")

print(f", {movie_booking()}, {(count())}")
