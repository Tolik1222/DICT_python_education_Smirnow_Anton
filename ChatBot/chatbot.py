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
