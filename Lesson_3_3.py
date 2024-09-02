import random, math

# dice_roll = random.randint(1, 6)
# print(f"Ви кинули {dice_roll}")

# num = random.random()
# print(num)

# fill_percentage = random.random() * 100
# print(f"Заповнення: {fill_percentage:.2f}%")

# print(random.randrange(10))  # Верхня межа є 10, але не включається

target = random.randrange(1, 11, 2)
print(f"Ціль: {target}")


# cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
# random.shuffle(cards)

# print(f"Перемішана колода: {cards}")

# # вибрати випадковий елемент зі списку
# print(random.choice(cards))


# items = ['яблуко', 'банан', 'вишня', 'диня']
# chosen_item = random.choices(items, k=2)
# print(chosen_item)  

# colors = ['червоний', 'зелений', 'синій']
# weights = [10, 1, 1] # Елемент 'червоний' має набагато більшу ймовірність бути обраним
# chosen_color = random.choices(colors, weights, k=2)
# print(chosen_color)  

# творення випадкової команди з 4 учасників з групи з 10 осіб
# participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
# team = random.sample(participants, 4)
# print(f"Команда: {team}")

# price = random.uniform(50, 100)
# print(f"Випадкова ціна: {price:.2f}")


# Вихідне число
# x = 3.7

# # Використання різних методів округлення
# ceil_result = math.ceil(x)  # Округлення вгору
# floor_result = math.floor(x)  # Округлення вниз
# trunc_result = math.trunc(x)  # Відсікання дробової частини

# print(ceil_result, floor_result, trunc_result)


# Використання констант
# print(math.pi)  # Виведе приблизне значення π

# # Тригонометрія
# angle = math.radians(60)  # Конвертація з градусів у радіани
# print(math.sin(angle))  # Синус кута

# # Корінь числа
# print(math.sqrt(9))  # Квадратний корінь з 9

# # Логарифми
# print(math.log(10, 2))  # Логарифм 10 за основою 2

# r = math.isclose(0.1 + 0.2, 0.3,)
# print(r)  # Це поверне True

# r = math.isclose(0.1, 0.10000000009)
# print(r)  # Це поверне True