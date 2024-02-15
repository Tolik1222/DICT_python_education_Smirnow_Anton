import random

def generate_question():
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
    return question, answer

def main():
    while True:
        # Генеруємо питання
        question, correct_answer = generate_question()
        print(question)
        user_answer = input("> ")
        # Перевіряємо відповідь
        try:
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                print("Right!")
            else:
                print("Wrong!")
        except ValueError:
            print("Please enter a valid integer.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
