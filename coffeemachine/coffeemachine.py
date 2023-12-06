class CoffeeMachineSimulator:
    def __init__(self):
        self.water_available = 400  # мл
        self.milk_available = 540   # мл
        self.coffee_beans_available = 120  # г
        self.disposable_cups_available = 9
        self.money_earned = 550  # грн

        self.espresso_recipe = {"water": 250, "coffee_beans": 16, "cost": 4}
        self.latte_recipe = {"water": 350, "milk": 75, "coffee_beans": 20, "cost": 7}
        self.cappuccino_recipe = {"water": 200, "milk": 100, "coffee_beans": 12, "cost": 6}

    def display_resources(self):
        print("\nThe coffee machine has:")
        print(f"{self.water_available} of water")
        print(f"{self.milk_available} of milk")
        print(f"{self.coffee_beans_available} of coffee beans")
        print(f"{self.disposable_cups_available} of disposable cups")
        print(f"{self.money_earned} of money")

    def buy_coffee(self, choice):
        if choice == 1:  # Espresso
            recipe = self.espresso_recipe
        elif choice == 2:  # Latte
            recipe = self.latte_recipe
        elif choice == 3:  # Cappuccino
            recipe = self.cappuccino_recipe
        else:
            return

        if (
            self.water_available >= recipe["water"]
            and self.milk_available >= recipe.get("milk", 0)
            and self.coffee_beans_available >= recipe["coffee_beans"]
            and self.disposable_cups_available >= 1
        ):
            print("I have enough resources to make your coffee. Making coffee...")
            self.water_available -= recipe["water"]
            self.milk_available -= recipe.get("milk", 0)
            self.coffee_beans_available -= recipe["coffee_beans"]
            self.disposable_cups_available -= 1
            self.money_earned += recipe["cost"]
            print("Coffee is ready!")
        else:
            print("Not enough resources to make coffee. Please fill the machine.")

    def fill_machine(self):
        self.water_available += int(input("Write how many ml of water you want to add:\n"))
        self.milk_available += int(input("Write how many ml of milk you want to add:\n"))
        self.coffee_beans_available += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.disposable_cups_available += int(input("Write how many disposable coffee cups you want to add:\n"))

    def take_money(self):
        print(f"I gave you {self.money_earned} money")
        self.money_earned = 0

    def process_action(self, action):
        if action == "buy":
            choice = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"))
            self.buy_coffee(choice)
        elif action == "fill":
            self.fill_machine()
        elif action == "take":
            self.take_money()

# Створюємо об'єкт для симулятора кавомашини
coffee_machine = CoffeeMachineSimulator()

# Виводимо початковий стан ресурсів
coffee_machine.display_resources()

# Отримуємо від користувача дію (купівля, поповнення або вилучення грошей) і виконуємо відповідну дію
action = input("\nWrite action (buy, fill, take):\n")
coffee_machine.process_action(action)

# Виводимо стан ресурсів після виконання дії
coffee_machine.display_resources()
