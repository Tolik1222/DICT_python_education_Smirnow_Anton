"""writing a program that implements a simple arithmetic test."""

import random
from typing import Tuple

def generate_question(level: int) -> Tuple[str, str]:
    """
    Generates questions for the test depending on the level of difficulty.


    Args:
        level (int): Difficulty level (1 or 2).


    Returns:
        tuple: A tuple containing the question and the correct answer.

    """
    question = ""
    answer = ""
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operator = random.choice(['+', '-', '*'])
        question = f"{num1} {operator} {num2}"
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
    elif level == 2:
        num = random.randint(11, 29)
        question = f"Square of {num}"
        answer = num ** 2
    return question, str(answer)


def main() -> None:
    """
    The main function of the program controls the execution of the test and the saving of the results.

    """
    while True:
        level = input(
            "Which level do you want? Enter a number:\n"
            "1 - simple operations with numbers 2-9\n"
            "2 - integral squares of 11-29\n> "
        )
        try:
            level = int(level)
            if level not in [1, 2]:
                raise ValueError
        except ValueError:
            print("Incorrect format.")
            continue

        correct_answers = 0
        for _ in range(5):
            question, correct_answer = generate_question(level)
            print(question)
            while True:
                user_answer = input("> ")
                try:
                    user_answer = int(user_answer)
                    break
                except ValueError:
                    print("Incorrect format. Please enter a valid integer.")

            if user_answer == int(correct_answer):
                print("Right!")
                correct_answers += 1
            else:
                print("Wrong!")

        print(f"Your mark is {correct_answers}/5.")

        save_result = input("Would you like to save the result? Enter yes or no.\n> ").lower()
        if save_result.startswith('y'):
            name = input("What is your name?\n> ")
            with open("results.txt", "a") as file:
                file.write(f"{name}: {correct_answers}/5 in level {level} ")
                if level == 1:
                    file.write("(simple operations with numbers 2-9).\n")
                else:
                    file.write("(integral squares of 11-29).\n")
            print("The results are saved in \"results.txt\".")

        play_again = input("Do you want to play again? Enter yes or no.\n> ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
