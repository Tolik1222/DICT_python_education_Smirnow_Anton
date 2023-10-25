"""the user needs to guess the word by letters. If you lose, you "hang". If the user wins, he survives."""

import random

def play_stage1():
    chosen_word = random.choice(['python', 'java', 'javascript', 'php'])
    guessed_word = ['_'] * len(chosen_word)
    attempts = 8

    guessed_letters = []

    while attempts > 0:
        print(' '.join(guessed_word))
        print(f'Input a letter: > ')
        guess = input().lower()

        if len(guess) != 1:
            print("You should input a single letter")
        elif not guess.isalpha() or not guess.islower():
            print("Please enter a lowercase English letter")
        elif guess in guessed_letters:
            print("You've already guessed this letter")
        elif guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"That letter doesn't appear in the word")

        guessed_letters.append(guess)

        if '_' not in guessed_word:
            print("You guessed the word!")
            break

    if attempts == 0:
        print("You lost!")

def main_menu():
    print("HANGMAN")
    while True:
        print("Type 'play' to play the game, 'exit' to quit: >")
        choice = input()

        if choice == "play":
            play_stage1()

        elif choice == "exit":
            break
        else:
            print("Invalid input. Please enter 'play' or 'exit'.")
main_menu()


