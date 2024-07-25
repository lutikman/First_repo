# Створення словника
my_dict = {} # пустого словника
my_dict = {"name": "Alice", "age": 25, "city": "New York"} # заповненого деякими значеннями словника
print(my_dict)

# Отримання значення словника за ключем
print(f"Value per key 'name' = {my_dict["name"]}")

# Щоб змінити значення або додати нову пару ключ-значення, просто використовуйте ключ для присвоєння нового значення:
my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
print(my_dict)

# del - оператор видалення елемента за ключем
del my_dict["age"]
print(f"my dict after del key 'age' : {my_dict}")

# in = оператор для перевірки, чи є ключ у словнику
print("key 'name' exist? - ", "name" in my_dict)
print("key 'age' exist? - ", "age" in my_dict)

# pop - метод, який у словниках дозволяє видалити елемент за вказаним ключем і повернути його значення
city = my_dict.pop("city")
print(f"city = {city}")
print(f"my_dict after pop: {my_dict}")

# update - метод використовується для оновлення словника іншим словником або парами ключ-значення.
# значення вже існуючих ключів буде оновлена, а нових додано
my_dict.update({"name": "Alisa", "age": 25, "city": "New York"})
print(f"my_dict after update: {my_dict}")

# copy - метод, який створює поверхневу копію словника. В результати отримаємо копію словника як окремого об'єкта
new_dict = my_dict.copy()
print(f"new dict: {new_dict}")

# clear - метод, який очищає словник, в результаті чого він стає пустим
my_dict.clear()
print(f"my_dict after clear: {my_dict}")

# get - метод, який використовується для безпечного отримання значення за ключем зі словника.
# якщо ключ відсутній, get() повертає None або інше значення, яке ви можете визначити як значення за замовчуванням

age = new_dict.get("age")
gender = new_dict.get("gender")
print(f"age = {age}")
print(f"gender = {gender}")