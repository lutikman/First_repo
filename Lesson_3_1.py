from datetime import datetime, date, time, timedelta, timezone

# Поточний час
now = datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)

# Створення об'єктів date і time
# date_part = date(2023, 12, 14)
# time_part = time(12, 30, 15)

# print(type(date_part))
# print(type(time_part))  


# # Комбінування дати і часу в один об'єкт datetime
# combined_datetime = datetime.datetime.combine(date_part, time_part)
# print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# specific_date = datetime.datetime(year=2020, month=1, day=7)
# print(specific_date)

# specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)
# print(specific_datetime)

# # Отримання номера дня тижня
# day_of_week = now.weekday()
# # Поверне число від 0 (понеділок) до 6 (неділя)
# print(f"Сьогодні: {day_of_week}")  


# delta = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)
# print(delta)

# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# difference = seventh_day_2020 - seventh_day_2019
# print(difference)  # 365 days, 0:00:00
# print(difference.total_seconds())  # 31536000.0


# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(future_date)

# # Створення об'єкта datetime
# date = datetime(year=2023, month=12, day=18)

# # Отримання порядкового номера
# ordinal_number = date.toordinal()
# print(f"Порядковий номер дати {date} становить {ordinal_number}")


# # Конвертація datetime в timestamp
# timestamp = datetime.timestamp(now)
# print(timestamp)  # Виведе timestamp поточного часу

# timestamp = 1724779196

# # Конвертація timestamp назад у datetime
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object)  # Виведе відповідний datetime


# Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date) 

# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only)

# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only)  

# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only)


# # Припустимо, у нас є дата у вигляді рядка
# date_string = "2023.14.03"

# # Перетворення рядка в об'єкт datetime
# datetime_object = datetime.strptime(date_string, "%Y.%d.%m")
# print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу


# # Конвертація у формат ISO 8601
# iso_format = now.isoformat()
# print(iso_format)

# iso_date_string = "2023-03-14T12:39:29.992996"

# # Конвертація з ISO формату
# date_from_iso = datetime.fromisoformat(iso_date_string)
# print(date_from_iso)


# # Використання isoweekday() для отримання дня тижня
# day_of_week = now.isoweekday()
# print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня

# # Отримання ISO календаря
# iso_calendar = now.isocalendar()
# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")


# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)

# print(local_now)
# print(utc_now)  # Виведе поточний час в UTC

# # Створення часової зони для Східного часового поясу (UTC-5)
# time_zone = timezone(timedelta(hours=-5))
# eastern_time = utc_now.astimezone(time_zone)
# # Перетворює час UTC в час Східного часового поясу
# print(time_zone)
# print(eastern_time)


# Припустимо, місцевий час належить до часової зони UTC+2
# local_timezone = timezone(timedelta(hours=2))
# local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# # Конвертація локального часу в UTC
# utc_time = local_time.astimezone(timezone.utc)
# print(utc_time)  # Виведе час в UTC
# # print(local_time)  # Виведе час в UTC

# # Конвертація у формат ISO 8601
# iso_format_with_timezone = local_time.isoformat()
# print(iso_format_with_timezone)