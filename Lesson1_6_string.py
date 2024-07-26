# Рядок — це незмінна впорядкована послідовність символів у деякому кодуванні.
# Важливо тільки пам'ятати, що рядки в Python є незмінними (immutable), це значить, що ви не можете змінити окремі символи в рядку без створення нового рядка.

game_string = 'My favorite "Game"'
game_string = "My favorite 'Game'"

# Впорядкована послідовність означає, що до елементів рядка можна звертатися за індексом:
print(game_string[0])

# Незмінна послідовність означає, що якщо рядок уже створений, то змінити його не можна, можна тільки створити новий.

# upper - метод, що дозволяє усі літери рядка перевести у верхній регістр
print(game_string.upper())

# lower - метод, що дозволяє усі літери рядка перевести у нижній регістр
print(game_string.lower())

# startswith - метод, що дозволяє перевірити, що рядок починається з вказаного підрядка
print(game_string.startswith("My"))
print(game_string.startswith("my"))

# endswith - метод, що дозволяє перевірити, що рядок закінчується вказаним підрядком
s = "hello.jpg"
print(s.endswith("jpg"))

# capitalize - метод робить перший символ рядка великою літерою, а інші — малими
print("hello world".capitalize())

# title - метод перетворює перші літери кожного слова в рядку на великі
print("hello world".title())

# isdigit, isalpha, isspace - методи, які перевіряють, чи складається рядок тільки з цифр, літер, пробілів тощо відповідно
print("123 is digital? - ", "123".isdigit())
print("hello is alpha? - ", "hello".isalpha())
print("this is spase? - ", " ".isspace())


# Метод format у Python використовується для форматування рядків.
# Він замінює {} в рядку на аргументи, які передаються методу format.
# Це надзвичайно корисно для створення динамічних рядків.

# Просте форматування рядка
name = 'John'
print('Hello, {}!'.format(name))

# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))

# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))