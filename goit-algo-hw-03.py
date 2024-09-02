from datetime import datetime
import random, re

# Перше завдання
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")

def get_days_from_today(date):
    try:
        date_date = string_to_date(date)
        today = datetime.today()
        return (today - date_date).days
    except ValueError:
        print("Не вірний формат дати")

print(get_days_from_today("2024-07-31"))


# Друге завдання
def get_numbers_ticket(min, max, quantity):
    if quantity < 1 or min < 1 or max > 1000 or (max-min)+1 < quantity: 
        return []
    
    set_numbers = set()
    while len(set_numbers) < quantity:
        set_numbers.add(random.randint(min, max))

    list_numbers = list(set_numbers)
    list_numbers.sort()
    return list_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


#Третє завдання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    norm_phone = re.sub(r"[^0-9+]", "", phone_number)
    if not norm_phone.startswith("+"):
        if norm_phone.startswith("380"):
            norm_phone = "+" + norm_phone
        else: 
            norm_phone = "+38" + norm_phone
    return norm_phone

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)