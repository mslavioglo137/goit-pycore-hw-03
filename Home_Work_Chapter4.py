import re, random 
from datetime import timedelta, date, datetime

'''Завдання 1: Напишіть функцію, яка приймає дату у форматі "РРРР-ММ-ДД" і повертає кількість 
днів від цієї дати до сьогоднішнього дня. '''
def get_days_from_today(DateForDelta):
    try:
        input_date = datetime.strptime(DateForDelta, "%Y-%m-%d").date()
        today = date.today()
        delta = (today -input_date ).days
        return delta
    except ValueError:
        return None

 
''' Завдання 2: написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел 
 для таких лотерей. Вона буде повертати випадковий набір чисел 
 у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні '''

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1):
        return []
    
    return sorted(random.sample(range(min, max + 1), quantity))

'''Завдання 3 Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку.
Функція приймає один аргумент — рядок з телефонним номером у будь-якому форматі та перетворює його на стандартний формат, залишаючи тільки цифри та символ '+'. 
Якщо номер не містить міжнародного коду, функція автоматично додає код '+38' (для України). Це гарантує, що всі номери будуть придатними для відправлення SMS.'''    

def normalize_phone(phone_number):
    # 1. залишаємо тільки цифри
    cleaned = re.sub(r'\D', '', phone_number)
    # 2. нормалізуємо код
    if cleaned.startswith('380'):
        return '+' + cleaned
    elif cleaned.startswith('0'):
        return '+38' + cleaned
    else:
        return '+380' + cleaned # Якщо номер починається лише з коду оператора без 0, додаємо код '+380'

""" 
Завдання 4
У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. 
Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, 
яка допоможе вам визначати, кого з колег потрібно привітати. 
Функція повинна повернути список всіх у кого день народження вперед на 7 днів 
включаючи поточний день.
"""
def get_upcoming_birthdays(users):
    today = date.today()
    UpcomingBirthdays = []
    
    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            birthday_this_year = birthday.replace(year=today.year)
            
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
            days_until_birthday = (birthday_this_year - today).days
            
            if 0 <= days_until_birthday <= 7:
                congratulation_date = birthday_this_year
                if congratulation_date.weekday() >= 5:  # Якщо день народження припадає на вихідний
                    congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))  # Переносимо на наступний понеділок
                
                UpcomingBirthdays.append({
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                })
        except ValueError:
            print(f"Невірний формат дати для користувача {user['name']}. Будь ласка, використовуйте формат 'рік.місяць.дата'.")
    
    return UpcomingBirthdays

#Попередні дані необхідні для завдань 3 та 4

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "63-123-45-67"]
users = [
    {"name": "Олександр", "birthday": "1990.04.20"},
    {"name": "Марія", "birthday": "1985.05.01"},
    {"name": "Іван", "birthday": "1992.10.03"},
    {"name": "Катерина", "birthday": "1988.04.30"},
    {"name": "Петро", "birthday": "1995.10.02"},
    {"name": "Анна", "birthday": "1991.10.07"},
    {"name": "Сергій", "birthday": "1989.10.04"},
    {"name": "Ольга", "birthday": "1993.10.06"} ]


#Вибір завдання і його запуск

YourChoice = input("Оберіть завдання (1-4): ")

if YourChoice == "1":
    DataDelta = get_days_from_today(input("Введіть дату у форматі 'РРРР-ММ-ДД': "))
    print(DataDelta if DataDelta is not None else "Невірний формат дати. Будь ласка, використовуйте формат 'РРРР-ММ-ДД'.")

elif YourChoice == "2":
    min_val, max_val, qty = map(int, input("Введіть три числа через пробіл (min max quantity): ").split())
    numbers = get_numbers_ticket(min_val, max_val, qty)
    print("Ваші лотерейні числа:", ", ".join(map(str, numbers)))

elif YourChoice == "3":
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

elif YourChoice == "4":
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Користувачі, у яких день народження вперед на 7 днів:")
    for user in upcoming_birthdays:
        print(f"- {user['name']}: {user['congratulation_date']}")

else:
    print("Невірний вибір")





