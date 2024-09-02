from datetime import datetime, date, timedelta

users = [
    {"name": "Bill Gates", "birthday": "1955.09.05"},
    {"name": "Steve Jobs", "birthday": "1955.09.07"},
    {"name": "Jinny Lee", "birthday": "1956.09.08"},
    {"name": "John Doe", "birthday": "1985.10.03"},
    {"name": "Jane Smith", "birthday": "1990.01.04"}
]

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return datetime.strftime(date, "%Y.%m.%d")

# date_string = "2024.01.01"
# converted_date = string_to_date(date_string)
# print(converted_date)
# date_string = date_to_string(converted_date)
# print(date_string)


def prepare_user_list(users_data):
    prepared_list = []
    for user in users_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

# prepared_users = prepare_user_list(users)
# print(users)
# print(prepared_users)


def find_next_weekday(start_date:datetime, weekday=0):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    days = timedelta(days_ahead)
    return start_date + days

# start_date = string_to_date("2024.09.07")  # Перетворення рядка на дату
# next_monday = find_next_weekday(start_date, 0)  # Знайти наступний понеділок
# print(next_monday)
# next_friday = find_next_weekday(start_date, 4)  # Знайти наступну п'ятницю
# print(next_friday)

def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    else:
        return birthday
    

def get_upcoming_birthdays(users_data, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users_data:
        birthday_this_year = user["birthday"].replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # if (birthday_this_year - today).days in range(0, days):
        if 0 <= (birthday_this_year - today).days <= days:
            birthday_this_year = adjust_for_weekend(birthday_this_year)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": date_to_string(birthday_this_year)})

    return upcoming_birthdays


users_with_birthday_this_year = get_upcoming_birthdays(prepare_user_list(users), 7)
# print(users_with_birthday_this_year)