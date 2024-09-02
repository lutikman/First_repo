import re

text = "Вивчення Python може бути веселим."
# pattern = "Python"
# match = re.search(pattern, text)

# if match:
#     print("Знайдено:", match.span())
#     print("Знайдено:", match.string)
#     print("Знайдено:", match.group())
# else:
#     print("Не знайдено.")


# # Тепер використаємо метасимволи, та виконаємо пошук слова, що починається на "в" та закінчується на "м".
# pattern = r"в\w*м"
# match = re.search(pattern, text, re.IGNORECASE)

# if match:
#     print("Знайдено:", match.group())


# text = "Моя електронна адреса: example@example.com"
# pattern = r"\w+@\w+\.\w+"
# match = re.search(pattern, text)

# if match:
#     print("Електронна адреса:", match.group())


# # Треба розділити "username@domain.com" на "username" (ім'я користувача) та "domain.com" (домен).
# email = "test username@domain.com"
# pattern = r"(\w+)@(\w+\.\w+)"
# match = re.search(pattern, email)

# if match:
#     user_name = match.group(1)
#     domain_name = match.group(2)
#     print("Ім'я користувача:", user_name)
#     print("Домен:", domain_name)


# # Необхідно знайти всі числа у рядку
# text = "Рік 2023 був складнішим, ніж 2022"
# pattern = r"\d+"
# matches = re.findall(pattern, text)

# print(matches)


# # Необхідно зробити вибірка всіх слів в тексті
# text = "Python - це проста, але потужна мова програмування."
# pattern = r"\w+"
# matches = re.findall(pattern, text)

# print(matches)  # Виведе список всіх слів у рядку


# # Замінити всі пробільні символи на підкреслення
# file_name = "Мій документ Python.txt"
# pattern = r"\s"
# replacement = "_"
# formatted_name = re.sub(pattern, replacement, file_name)

# print(formatted_name)  


# # Видалимо всі пунктуаційні знаки з рядка.
# text = "Python - потужна, універсальна; мова!"
# pattern = r"[;,\-:!\.]"
# replacement = ""
# modified_text = re.sub(pattern, replacement, text)

# print(text, modified_text, sep='\n')


# # В тексті в нас телефони записані в такому форматі 050-171-1634, нам необхідно замінити їх на формат (050) 171-1634
# phone = """Михайло Куліш: 050-171-1634
#         Вікторія Кущ: 063-134-1729
#         Оксана Гавриленко: 068-234-5612"""

# pattern = r"(\d{3})-(\d{3})-(\d{4})"
# replacement = r"(\1) \2-\3"
# formatted_phone = re.sub(pattern, replacement, phone)

# print(formatted_phone)


# Спробуємо розділити рядок на частини, використовуючи пунктуаційні знаки як роздільники.
text = "Python - потужна; проста, універсальна: мова!"
pattern = r"[;,\-:!\s]+"
elements = re.split(pattern, text)

print(elements)  # Виведе список частин, розділених пунктуацією
elements = elements[:-1:] # Останній пустий елемент, кінець рядка, можна видалити зрізами
print(elements)