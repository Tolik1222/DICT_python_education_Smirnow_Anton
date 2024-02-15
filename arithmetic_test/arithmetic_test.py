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
    correct_answers = 0
    for _ in range(5):
        # Генеруємо питання
        question, correct_answer = generate_question()
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

if __name__ == "__main__":
    main()
