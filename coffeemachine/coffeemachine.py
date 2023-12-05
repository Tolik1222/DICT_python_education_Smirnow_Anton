"""Creating a coffee machine simulator"""


# determine the initial state of the coffee machine before starting any operations or interactions with it.


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

# processes a user-entered selection or command for the coffee machine.

    def process_action(self, action):
        if action == "buy":
            self.buy_coffee()
        elif action == "fill":
            self.fill_supplies()
        elif action == "take":
            self.take_money()
        elif action == "remaining":
            self.display_status()
        elif action == "exit":
            exit()
        else:
            print("Invalid input. Please try again.")

    def buy_coffee(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ")

        if coffee_type == "back":
            return

        try:
            coffee_type = int(coffee_type)
            water_needed, milk_needed, beans_needed, cost = 0, 0, 0, 0

            if coffee_type == 1:  # Espresso
                water_needed, milk_needed, beans_needed, cost = 250, 0, 16, 4
            elif coffee_type == 2:  # Latte
                water_needed, milk_needed, beans_needed, cost = 350, 75, 20, 7
            elif coffee_type == 3:  # Cappuccino
                water_needed, milk_needed, beans_needed, cost = 200, 100, 12, 6
            else:
                print("Invalid")
                return

            if (
                    self.water >= water_needed
                    and self.milk >= milk_needed
                    and self.coffee_beans >= beans_needed
                    and self.disposable_cups >= 1
            ):
                print("I have enough resources, making you a coffee!")
                self.water -= water_needed
                self.milk -= milk_needed
                self.coffee_beans -= beans_needed
                self.disposable_cups -= 1
                self.money += cost
            else:
                print("Sorry, not enough resources to make the coffee.")
        except ValueError:
            print("Invalid input. Please try again.")

    def fill_supplies(self):
        try:
            water_to_add = int(input("Write how many ml of water you want to add:\n> "))
            self.water += water_to_add

            milk_to_add = int(input("Write how many ml of milk you want to add:\n> "))
            self.milk += milk_to_add

            coffee_beans_to_add = int(input("Write how many grams of coffee beans you want to add:\n> "))
            self.coffee_beans += coffee_beans_to_add

            disposable_cups_to_add = int(input("Write how many disposable coffee cups you want to add:\n> "))
            self.disposable_cups += disposable_cups_to_add

            if water_to_add < 0 or milk_to_add < 0 or coffee_beans_to_add < 0 or disposable_cups_to_add < 0:
                print("Invalid input. Please enter positive integers.")
            else:
                self.water += water_to_add
                self.milk += milk_to_add
                self.coffee_beans += coffee_beans_to_add
                self.disposable_cups += disposable_cups_to_add
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# handles the choice of coffee type made by the user when performing the "buy" action.
    def buy_coffee(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ")
        if coffee_type == "back":
            return

        coffee_type = int(coffee_type)
        water_needed, milk_needed, beans_needed, cost = 0, 0, 0, 0

        if coffee_type == 1:  # Espresso
            water_needed, milk_needed, beans_needed, cost = 250, 0, 16, 4
        elif coffee_type == 2:  # Latte
            water_needed, milk_needed, beans_needed, cost = 350, 75, 20, 7
        elif coffee_type == 3:  # Cappuccino
            water_needed, milk_needed, beans_needed, cost = 200, 100, 12, 6
        else:
            print("Invalid coffee type. Please try again.")
            return

        if self.water >= water_needed and self.milk >= milk_needed and self.coffee_beans >= beans_needed and self.disposable_cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= water_needed
            self.milk -= milk_needed
            self.coffee_beans -= beans_needed
            self.disposable_cups -= 1
            self.money += cost
        else:
            print("Sorry, not enough resources to make the coffee.")

# allows the user to replenish the supplies of ingredients and disposable cups in the coffee machine
    def fill_supplies(self):
        self.water += int(input("Write how many ml of water you want to add:\n> "))
        self.milk += int(input("Write how many ml of milk you want to add:\n> "))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add:\n> "))
        self.disposable_cups += int(input("Write how many disposable coffee cups you want to add:\n> "))

# displays a message about how much money was taken from the coffee machine
    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

# outputs information about the current state of the coffee machine to the console
    def display_status(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.coffee_beans} grams of coffee beans")
        print(f"{self.disposable_cups} disposable cups")
        print(f"${self.money} of money")


# Example usage
coffee_machine = CoffeeMachine()

# ending code
while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n> ")
    coffee_machine.process_action(action)
