"""creating a Rock, Scissors, Paper game for the user to play against the computer."""


import random  # Import the random module for generating random values
import os  # Import the os module to work with the operating system
import string  # Import the string module for working with strings


def get_user_options():
    while True:
        # A request from the user to enter game options
        user_input = input("Enter your options separated by commas (e.g., rock,paper,scissors): ").lower()
        if not user_input:
            # If the entered options are empty, we use the default values
            print("Using default options: rock, paper, scissors.")
            return ['rock', 'paper', 'scissors']
        elif not all(char in string.ascii_lowercase + ',' for char in user_input):
            # Checking the correctness of entered characters
            print("Options should only contain letters and commas.")
        else:
            options = user_input.split(',')
            if len(options) < 3:
                # Checking the number of options entered
                print("Please enter at least three options.")
            else:
                return options


def computer_choice(options):
    return random.choice(options)  # Generation of a random computer selection from game options


def determine_winner(user_choice, comp_choice, options):
    half_len = len(options) // 2
    index_user = options.index(user_choice)
    index_comp = options.index(comp_choice)
    if user_choice == comp_choice:
        # Checking for a tie
        return f"There is a draw ({comp_choice})", 50
    elif index_user < index_comp:
        if index_comp - index_user <= half_len:
            # Determination of the winner
            return f"Well done. The computer chose {comp_choice} and failed", 100
        else:
            return f"Sorry, but the computer chose {comp_choice}", 0
    else:
        if index_user - index_comp <= half_len:
            return f"Sorry, but the computer chose {comp_choice}", 0
        else:

            return f"Well done. The computer chose {comp_choice} and failed", 100


def get_user_input(options):
    while True:
        # A request from the user to select an option
        user_input = input(f"Enter your choice ({', '.join(options)}) or type '!exit' to quit: ").lower()
        if user_input == '!exit':
            # Choose to exit the game
            return '!exit', None
        elif user_input == '!rating':
            # View rating
            return '!rating', None
        elif user_input in options:
            # Returning the selected option to the user
            return 'option', user_input
        else:
            print("Invalid input.")  # Incorrect input message


def update_rating(user, points):
    with open('rating.txt', 'r') as file:
        lines = file.readlines()

    ratings = {}
    for line in lines:
        name, rating = line.strip().split()
        ratings[name] = int(rating)

    if user in ratings:
        ratings[user] += points
    else:
        ratings[user] = points

    with open('rating.txt', 'w') as file:
        for name, rating in ratings.items():
            file.write(f"{name} {rating}\n")


if not os.path.isfile('rating.txt'):
    with open('rating.txt', 'w') as file:
        pass

while True:
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")

    options = get_user_options()  # Getting game options from the user
    print("Okay, let's start.")

    with open('rating.txt', 'r') as file:
        ratings = dict(line.strip().split() for line in file)

    user_rating = int(ratings.get(user_name, 0))
    print(f"Your rating: {user_rating}")

    while True:
        action, user_input = get_user_input(options)  # Getting the user's choice

        if action == '!exit':
            print("Bye!")  # Exiting from the game
            exit()
        elif action == '!rating':
            print(f"Your rating: {user_rating}")  # Displaying the user's rating
        elif action == 'option':
            comp_input = computer_choice(options)  # Generation of computer selection
            result, points = determine_winner(user_input, comp_input, options)  # Determination of the winner
            user_rating += points
            update_rating(user_name, points)  # User rating update
            print(result)  # Displaying the result of the game