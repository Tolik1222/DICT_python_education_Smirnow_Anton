import requests

# Кеш для зберігання обмінних курсів
cache = {}

def get_exchange_rate(currency_code):
    # Перевіряємо, чи валюта є в кеші
    if currency_code in cache:
        print("Checking the cache...")
        return cache[currency_code]
    else:
        print("Checking the cache...")
        url = f"http://www.floatrates.com/daily/{currency_code}.json"
        response = requests.get(url)
        data = response.json()
        # Зберігаємо обмінний курс у кеші
        cache[currency_code] = data
        return data

def convert_currency(source_currency, target_currency, amount):
    # Отримуємо дані про обмінний курс для валют, які цікавлять користувача
    source_data = get_exchange_rate(source_currency.upper())
    target_data = get_exchange_rate(target_currency.upper())

    # Перевіряємо, чи є дані для обох валют
    if source_currency.lower() not in source_data or target_currency.lower() not in target_data:
        print("Sorry, but data for one or both currencies is not available.")
        return None

    # Обчислюємо суму в цільовій валюті
    target_amount = amount * target_data[target_currency.lower()]['rate'] / source_data[source_currency.lower()]['rate']
    return round(target_amount, 2)

# Головна частина програми
while True:
    source_currency = input("Enter the source currency code (leave blank to stop): ").upper()
    if not source_currency:
        break

    target_currency = input("Enter the target currency code: ").upper()
    amount = float(input("Enter the amount: "))

    result = convert_currency(source_currency, target_currency, amount)
    if result is not None:
        print(f"You received {result} {target_currency}.")
