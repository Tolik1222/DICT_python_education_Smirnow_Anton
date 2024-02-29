"""creating a Rock, Scissors, Paper game for the user to play against the computer."""


<<<<<<< HEAD
import random  # Importing the random module for generating computer choices.
import os  # Importing the os module for file operations.
import string  # Importing the string module for string-related operations.


def get_user_options():
    """
    Function to get user options for the game.
    """
    while True:
        game_options_input = input("Enter your options separated by commas (e.g., rock,paper,scissors): ").lower()
        if not game_options_input:
            print("Using default options: rock, paper, scissors.")
            return ['rock', 'paper', 'scissors']
        elif not all(char in string.ascii_lowercase + ',' for char in game_options_input):
            print("Options should only contain letters and commas.")
        else:
            game_options = game_options_input.split(',')
            if len(game_options) < 3:
                print("Please enter at least three options.")
            else:
                return game_options


def computer_choice(game_options):
    """
    Function to generate computer's choice.
    """
    return random.choice(game_options)


def determine_winner(user_choice, comp_choice, game_options):
    """
    Function to determine the winner of the game.
    """
    half_len = len(game_options) // 2
    index_user = game_options.index(user_choice)
    index_comp = game_options.index(comp_choice)
    if user_choice == comp_choice:
        return f"There is a draw ({comp_choice})", 50
    elif index_user < index_comp:
        if index_comp - index_user <= half_len:
            return f"Sorry, but the computer chose {comp_choice}", 0
        else:
            return f"Well done. The computer chose {comp_choice} and failed", 100
    else:
        if index_user - index_comp <= half_len:
            return f"Well done. The computer chose {comp_choice} and failed", 100
        else:
            return f"Sorry, but the computer chose {comp_choice}", 0


def get_user_input(game_options):
    """
    Function to get user input during the game.
    """
    while True:
        user_choice = input(f"Enter your choice ({', '.join(game_options)}) or type '!exit' to quit: ").lower()
        if user_choice == '!exit':
            return '!exit', None
        elif user_choice == '!rating':
            return '!rating', None
        elif user_choice in game_options:
            return 'option', user_choice
        else:
            print("Invalid input.")


def update_rating(user_name, user_points):
    """
    Function to update user's rating.
    """
    with open('rating.txt', 'r') as rating_file:
        rating_lines = rating_file.readlines()

    user_ratings = {}
    for line in rating_lines:
        name, rating = line.strip().split()
        user_ratings[name] = int(rating)

    if user_name in user_ratings:
        user_ratings[user_name] += user_points
    else:
        user_ratings[user_name] = user_points

    with open('rating.txt', 'w') as rating_file:
        for name, rating in user_ratings.items():
            rating_file.write(f"{name} {rating}\n")


if not os.path.isfile('rating.txt'):
    with open('rating.txt', 'w') as new_rating_file:
=======
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
>>>>>>> 4f0974a789a1f7a108b4099bc2636202341146ac
        pass

while True:
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")

<<<<<<< HEAD
    options = get_user_options()
    print("Okay, let's start.")

    with open('rating.txt', 'r') as read_rating_file:
        ratings = dict(line.strip().split() for line in read_rating_file)
=======
    options = get_user_options()  # Getting game options from the user
    print("Okay, let's start.")

    with open('rating.txt', 'r') as file:
        ratings = dict(line.strip().split() for line in file)
>>>>>>> 4f0974a789a1f7a108b4099bc2636202341146ac

    user_rating = int(ratings.get(user_name, 0))
    print(f"Your rating: {user_rating}")

    while True:
<<<<<<< HEAD
        action, user_choice = get_user_input(options)

        if action == '!exit':
            print("Bye!")
            exit()
        elif action == '!rating':
            print(f"Your rating: {user_rating}")
        elif action == 'option':
            comp_choice = computer_choice(options)
            result, points = determine_winner(user_choice, comp_choice, options)
            user_rating += points
            update_rating(user_name, points)
            print(result)
=======
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
>>>>>>> 4f0974a789a1f7a108b4099bc2636202341146ac
