class CoffeeMachineSimulator:
    def __init__(self):
        self.water_available = 0
        self.milk_available = 0
        self.coffee_beans_available = 0
        self.water_per_cup = 200  # мл
        self.milk_per_cup = 50  # мл
        self.coffee_beans_per_cup = 15  # г

    def check_resources(self, cups_needed):
        water_needed = cups_needed * self.water_per_cup
        milk_needed = cups_needed * self.milk_per_cup
        coffee_beans_needed = cups_needed * self.coffee_beans_per_cup

        if self.water_available >= water_needed and self.milk_available >= milk_needed and self.coffee_beans_available >= coffee_beans_needed:
            extra_cups = min(
                self.water_available // self.water_per_cup,
                self.milk_available // self.milk_per_cup,
                self.coffee_beans_available // self.coffee_beans_per_cup
            )

            if extra_cups > 0:
                print(f"Yes, I can make that amount of coffee (and even {extra_cups} more than that)")
            else:
                print("Yes, I can make that amount of coffee")
        else:
            max_cups = min(
                self.water_available // self.water_per_cup,
                self.milk_available // self.milk_per_cup,
                self.coffee_beans_available // self.coffee_beans_per_cup
            )
            print(f"No, I can make only {max_cups} cups of coffee")

    def get_resources_from_user(self):
        self.water_available = int(input("Write how many ml of water the coffee machine has:\n"))
        self.milk_available = int(input("Write how many ml of milk the coffee machine has:\n"))
        self.coffee_beans_available = int(input("Write how many grams of coffee beans the coffee machine has:\n"))

    def get_cups_needed_from_user(self):
        cups_needed = int(input("Write how many cups of coffee you will need:\n"))
        return cups_needed


# Створюємо об'єкт для симулятора кавомашини
coffee_machine = CoffeeMachineSimulator()

# Отримуємо від користувача кількість інгредієнтів
coffee_machine.get_resources_from_user()

# Отримуємо від користувача кількість чашок кави, яку він хоче приготувати
cups_needed = coffee_machine.get_cups_needed_from_user()

# Перевірка наявності достатньої кількості інгредієнтів для приготування кави
coffee_machine.check_resources(cups_needed)
