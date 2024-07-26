# Список — це впорядкований змінюваний контейнер даних
my_list = list()

# Списки можуть містити різні типи даних:
my_list = [1, "Hello", 3.14, "Hello"]
print(f"Create list: {my_list}")

# append() - метод, додавання нового елемента в кінець списку
my_list.append(4)
my_list.append("Hello")
print(f"After append: {my_list}")

# remove() - метод, видалити елемент списку
my_list.remove("Hello")
print(f"After remove: {my_list}")

# синтаксис доступу за індексом виглядає так:
some_iterable = ["a", "b", "c"]
middle_one = some_iterable[1]
print(f"Get item by index 1: {middle_one}")

# Python підтримує індексування елементів з кінця
# перший елемент з кінця — це -1, другий — -2 і так далі
middle_one = some_iterable[-2]
last_letter = some_iterable[-1]
print(f"Get item by index -1: {last_letter}")

# змінити значення будь-якого елемента списку
some_iterable[-1] = 5
print(f"After change item with index -1: {some_iterable}")

# pop(i) - метод, який повертає елемент за індексом i та видаляє його зі списку
last = some_iterable.pop(-1)
print(f"After pop(-1): {some_iterable}")
print(f"last={last}")

# extend() - метод для розширення одного списку іншим
some_iterable.extend(my_list)
print(f"After extend(my_list): {some_iterable}")

# insert(i, x) - метод для вставки елемента x на позицію з індексом i у список
some_iterable.insert(2, 'c')
print(f"After insert(2, 'c'): {some_iterable}")

# index() - метод знаходження індексу першого входження заданого елемента у списку
# Якщо елемент не знаходиться у списку, Python викине помилку ValueError
print(f"After index(3.14): {some_iterable.index(3.14)}")

# count() - метод для підрахунку кількості разів, скільки певний елемент зустрічається у списку
my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
print(f"Count 2 in list: {count_2}")

# len - вбодована функція для визначення довжини (кількості елементів) списку
length = len(my_list)
print(f"length of list = {length}")
print(my_list)

# sort() - метод, використовується для сортування елементів списку в порядку зростання або спадання
my_list.sort()
print(f"list after sort: {my_list}")
# reverse=True - агрумент, якщо потрібно відсортувати елементи в порядку спадання
my_list.sort(reverse=True)
print(f"list after sort desc: {my_list}")

# для сортування за ключем використовуємо аргумент "key". Наприклад, у наступному прикладі ми відсортуємо список за довжиною слова у списку.
words = ["bananas", "apple", "cherry"]
words.sort(key=len)
print(f"list after sort by key=len: {words}")

# sorted() - функція, яка повертає новий відсортований список, не змінюючи початковий список
# Функція також використовує аргумент reverse=True, щоб відсортувати об'єкти у зворотному порядку,
# та за допомогою аргументу key можна вказати функцію, яка буде застосовуватися для визначення порядку сортування.

nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)
print(f"list: {nums}")
print(f"Sorted copy list: {sorted_nums}")

sorted_nums_desc = sorted(nums, reverse=True)
print(f"Sorted copy list: {sorted_nums_desc}")

words = ["bananas", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print(f"list: {words}")
print(f"Sorted copy list: {sorted_words}")

sorted_words = sorted(words, key=len, reverse=True)
print(f"Sorted copy list: {sorted_words}")

# reverse() - використовується, щоб змінити порядок елементів у списку на зворотний
print(f"list: {words}")
words.reverse()
print(f"Reverse list: {words}")

# clear() - метод для очищення списку
print(f"list: {words}")
words.clear()
print(f"List after clear: {words}")