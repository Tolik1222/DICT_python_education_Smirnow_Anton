"""creating a Rock, Scissors, Paper game for the user to play against the computer."""


import random  # Importing the random module for generating computer choices.
import os  # Importing the os module for file operations.
import string  # Importing the string module for string-related operations.

# Function to get user options for the game.


def get_user_options():
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

# Function to generate computer's choice.


def computer_choice(game_options):
    return random.choice(game_options)

# Function to determine the winner of the game.


def determine_winner(user_choice, comp_choice, game_options):

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

# Function to get user input during the game.


def get_user_input(game_options):
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

# Function to update user's rating.


def update_rating(user_name, user_points):
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
        pass

while True:
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")

    options = get_user_options()
    print("Okay, let's start.")

    with open('rating.txt', 'r') as read_rating_file:
        ratings = dict(line.strip().split() for line in read_rating_file)

    user_rating = int(ratings.get(user_name, 0))
    print(f"Your rating: {user_rating}")

    while True:
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
