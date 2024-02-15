"""writing a program that implements a simple arithmetic test."""


import random

def generate_question(level):
    if level == 1:
        # Генеруємо два випадкових числа в діапазоні від 2 до 9
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        # Вибираємо випадкову арифметичну операцію
        operator = random.choice(['+', '-', '*'])
        # Формуємо рядок із завданням
        question = f"{num1} {operator} {num2}"
        # Обчислюємо правильну відповідь
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
    elif level == 2:
        # Генеруємо випадкове число від 11 до 29
        num = random.randint(11, 29)
        # Формуємо рядок із завданням
        question = f"Square of {num}"
        # Обчислюємо правильну відповідь
        answer = num ** 2
    return question, answer

def main():
    while True:
        level = input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> ")
        try:
            level = int(level)
            if level not in [1, 2]:
                raise ValueError
        except ValueError:
            print("Incorrect format.")
            continue

        correct_answers = 0
        for _ in range(5):
            # Генеруємо питання
            question, correct_answer = generate_question(level)
            print(question)
            while True:
                user_answer = input("> ")
                # Перевіряємо формат відповіді
                try:
                    user_answer = int(user_answer)
                    break  # Вихід з циклу, якщо відповідь у правильному форматі
                except ValueError:
                    print("Incorrect format. Please enter a valid integer.")

            # Перевіряємо відповідь
            if user_answer == correct_answer:
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
