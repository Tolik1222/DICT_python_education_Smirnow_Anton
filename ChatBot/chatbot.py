print("Hello! My name is TolikBot")
print("I was created in 2023")
print("Please, remind me your name.")

your_name = input()

print(f"What a great name you have")

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {your_age}; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want")

iterations_count = int(input())
for i in range(iterations_count + 1):
    print(f"{i}!")

print("Let`s test your programming knowledge")
print("How to set the value to Username in Git?")
print("1. All commands except git user.name")
print("2. git user.name")
print("3. git config --global user.name")
print("4. git config user.name")

answer = int(input())

while True:
    if answer < 1 or answer > 4:
        print("There is no such answer. Try from 1 to 4")
    else:
        if answer == 2:
            print("Completed, have a nice day!")
            break
        else:
            print("Please, try again.")
            answer = int(input())
print("Congratulations, have a nice day!")
