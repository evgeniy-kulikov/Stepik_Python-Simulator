#  12 Строки 1
""""""

# Task 01
"""
Подсчитывать все заглавные буквы в переменной message
Input:  Привет Лия
Output: 2
"""
message = "Привет Лия"
# message = input().strip()

result = sum(el.isupper() for el in message)
# result = len(list(filter(lambda el: el.isupper(), message)))

# result = 0
# for el in message:
#     if el.isupper():
#         result += 1

# print(result)


# Task 02
"""
Подсчитывать все строчные  буквы в переменной message
Input:  Привет Лия
Output: 7
"""
message = "Привет Лия"
# message = input().strip()

result = sum(el.islower() for el in message)
# result = len(list(filter(lambda el: el.islower(), message)))

# print(result)


# Task 03
"""
Подсчитывать все пробелы буквы в переменной message
Input:  Привет Лия
Output: 1
"""
message = "Привет Лия"
# message = input().strip()

result = message.count(' ')
# result = sum(el.isspace() for el in message)
# result = len(list(filter(lambda el: el.isspace(), message)))

# print(result)


# Task 04
"""
Поменять строчные буквы на заглавные, а заглавные на строчные  в переменной message
Input:  Лия
Output: лИЯ
"""
message = "Лия"
# message = input().strip()

result = message.swapcase()
# print(result)



# Task 05
"""
Поменять первые буквы слов на заглавные в переменной message
Input:  привет лия
Output: Привет Лия
"""
message = "привет лия"
# message = input().strip()

result = message.title()
# result = ' '.join([el.capitalize() for el in message.split()])

# print(result)


# Task 07
"""
Переменная message, принимает входные пользовательские данные.
Данные такого формата: ЧИСЛО,ЧИСЛО,ЧИСЛО и тд...
Сложить все числа
Input:  2,2,2
Output: 6
"""
message = "2,2,2"
# message = input().strip()

result = sum(list(map(int, message.split(','))))
# result = sum(map(lambda x: int(x), message.split(',')))
# result = sum([int(el) for el in message.split(',')])

# print(result)


# Task 08
"""
Переменная message, принимает входные пользовательские данные.
Данные такого формата: букваЧИСЛО,букваЧИСЛО,букваЧИСЛО и тд...
Сложить все числа
Input:  a2,b2,f2
Output: 6
"""

message = "a2,b2,f2"
# message = input().strip()

result = sum([int(el[1:]) for el in message.split(',')])
# result = sum(map(lambda x: int(x[1:]), message.split(',')))

# message = ''.join(i for i in message if not i.isalpha())  # удаляем буквы из строки
# result = sum([int(el) for el in message.split(',')])

import re
# result = sum(map(int, re.findall(r'\d+', message)))
# result = sum(int(x) for x in re.findall(r'\d+', message))
# result = sum(map(int, filter(None, re.split(r"[\D]", message))))

# print(result)


# Task 09
"""
Переменная message, принимает входные пользовательские данные.
Проверить, заканчивается ли строка в переменной message на символ /
Input:  https://awilum.ru/
Output: True
"""
message = "https://awilum.ru/"
# message = input().strip()

result = message.endswith('/')
# result = message[-1] == '/'

# print(result)


# Task 10
"""
Переменная message, принимает входные пользовательские данные.
Проверить, начинается ли строка в переменной message на "https://"
Input:  https://awilum.ru/
Output: True
"""
message = "https://awilum.ru/"
# message = input().strip()

result = message.startswith('https://')
# result = message[:8] == 'https://'

# print(result)


# Task 11
"""
У вас есть переменная title, которая содержит входные пользовательские данные.
Напишите код, который преобразует содержимое переменной title в валидный slug
Input:  The Hellfire Club
Output: the-hellfire-club
"""
title = input().strip()

result = title.lower().replace(' ', '-')

# print(result)


# Task 12
"""
Переменные search, message принимают входные пользовательские данные.
Проверить, содержит ли строка в переменной message строку из переменной search
Input:  одежду | Учитесь выбирать свои мысли, как выбираете в шкафу одежду каждый день.
Output: True
"""
search = "одежду"
message = "Учитесь выбирать свои мысли, как выбираете в шкафу одежду каждый день."
# search, message = map(str.strip, input().split(" | "))

result = search in message
# result = any([el == search for el in message.split()])
# result = any(list(map(lambda el: el == search, message.split())))

# print(result)


# Task 13
"""
Заменить в строке message слово яблоки на значение переменной replace
Input:  бананы | Я люблю яблоки.
Output: Я люблю бананы.
"""
replace = "бананы"
message = "Я люблю яблоки."
# replace, message = map(str.strip, input().split(" | "))

result = message.replace('яблоки', replace)

# print(result)


# Task 14
"""
Напишите код, который объединяет значение переменной currency с price
Input:  € | 9.99
Output: €9.99
"""
# currency, price = map(str.strip, input().split(" | "))
# price = float(price)
currency, price = '€', 9.99
result = currency + str(price)

# print(result)


# Task 15
"""
Подсчитать сколько раз встречается буква в строке city, 
Отобразить количество повторений в виде звездочек *  (Регистр значение не имеет)
Input:  Ривенделл
Output: р:*,и:*,в:*,е:**,н:*,д:*,л:**
"""
# city = input().strip().lower()
city = "ривенделл"

# словарь - счетчик
d = {}
for el in city:
    d.setdefault(el, '')
    d[el] += '*'

result = [f"{k}:{v}" for k, v in d.items()]
result = ','.join(result)


# строка через цикл
result = ''
for el in city:
    if el not in result:
        result += f'{el}:{city.count(el) * "*"},'
result = result[:-1]

# строка через генератор списка
# i == city.find(el) - отсеивает повторно встречающиеся элементы
result = [f'{el}:{city.count(el) * "*"}' for i, el in enumerate(city) if i == city.find(el)]
result = ','.join(result)

# print(result)
