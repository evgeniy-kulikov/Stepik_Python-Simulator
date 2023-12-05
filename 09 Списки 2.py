#  09 Списки. Часть 2
""""""

# Task 01
"""
переменные n, data которые содержат входные пользовательские данные.
Умножить каждый элемент списка на значение переменной n
Input:  2 | [1, 2, 3]
Output: 2, 4, 6
"""
import json
n, data = input().split(" | ")
n = int(n)
data = json.loads(data)

result = ', '.join([str(el * n) for el in data])
# result = ', '.join(map(lambda el: str(el * n), data))

# print(result)


# Task 02
"""
переменные n, data которые содержат входные пользовательские данные.
Исключить из списка data все значения, которые больше значения переменной n
Input:  3 | [1, 2, 3, 4, 5, 1, 2, 3, 4]
Output: 1, 2, 3, 1, 2, 3
"""
import json
n, data = input().split(" | ")
n = int(n)
data = json.loads(data)

result = ', '.join([str(el) for el in data if el <= n])
# result = ', '.join(map(str, filter(lambda el: el <= n, data)))

# print(result)


# Task 03
"""
переменная data содержит входные пользовательские данные.
Проверить, все ли элементы в списке имеют значение True
Input:  [true, true, true]
Output: True
"""
import json
data = json.loads(input())

result = all(data)

# print(result)


# Task 04
"""
переменная data содержит входные пользовательские данные.
Проверить, все ли элементы в списке имеют значение false
Input:  [false, false, false]
Output: True
"""
import json
data = json.loads(input())

result = not any(data)

# print(result)


# Task 05
"""
Переменныe list1, list2, которые содержат входные пользовательские данные.
Сравнить список list1 с list2 и записать разницу между ними в виде строки через запятую.
Input:  [1, 2, 3, 4, 5] | [1, 2, 5]
Output: 3, 4
"""
import json
list1, list2 = map(json.loads, input().split(" | "))


if list1 != list2:
    result = ', '.join(map(str, [el for el in list1 if el not in list2]))
    # result = ', '.join(map(str, filter(lambda el: el not in list2, list1)))
    #  result = ", ".join(str(el) for el in list(set(list1) - set(list2)))
else:
    result = 'Списки одинаковые'

# print(result)


# Task 06
"""
https://stepik.org/lesson/957398/step/6?unit=963831
У вас есть переменныe size, position, data, которые содержат входные пользовательские данные.
Напишите код, который заполняет список data до нужного размера size нулями (0) в зависимости от значения position, 
которое может принимать значения: left или right.
Важно!
Если размер списка data  больше размера size, тогда в переменную result записываем сообщение: 
Неверный размер
Если размер списка data  равен значению переменной size, тогда в переменную result записываем: 
Массив data в виде строки через запятую.
Если значение переменной position не равно left или right, тогда в переменную result записываем сообщение:
Неверная позиция
Сначала проверяем на корректность размера, потом проверяем на корректность позиции.
Input:  5 | right | [1, 2, 3, 4, 5]
Output: 1, 2, 3, 4, 5
"""
import json

size, position, data = input().split(" | ")
size = int(size)
position = str(position)
data = json.loads(data)


def pad(size, position, data):
    if len(data) > size:
        return 'Неверный размер'
    elif position not in ['left', 'right']:
        return 'Неверная позиция'
    else:
        zero = [0 for _ in range(size - len(data))]
        return ', '.join(map(str, (zero + data) if position == 'left' else (data + zero)))

result = pad(size, position, data)

# print(result)


# Task 07
"""
Напишите код, который проверяет все ли элементы в списка null
Input:  [null, null, null, true, null]
Output: False
"""
import json
data = json.loads(input())

result = all([el is None for el in data])

# print(result)


# Task 08
"""
Напишите код, который находит максимальное число в двумерном списке произвольного размера
Input:  [[1, 2, 3],[4, 42, 6],[7, 8, 9]]
Output: 42
"""
import json
data = json.loads(input())

result = max(max(el) for el in data)

print(result)


# Task 09
"""
Напишите код, который находит минимальное число в двумерном списке произвольного размера
Input:  [[2, 3, 1],[4, 42, 6],[7, 8, 9]]
Output: 1
"""
import json
data = json.loads(input())

result = min(min(el) for el in data)

# print(result)


# Task 10
"""
Напишите код, который находит число k в двумерном в списке data 
и записывает логический результат в переменную result.
Input:  5 | [[1,2,3],[4,5,6],[7,8,9]]
Output: True
"""
import json
k, data = input().split(" | ")
k = int(k)
data = json.loads(data)

def find_number_2d(k, data):
    return any([k in el for el in data])

result = find_number_2d(k, data)

# print(result)


# Task 11
"""
Напишите код, который будет находить четные и нечетные числа и записывать результат в виде строки:
(четные) (нечетные) в переменную result.
Input:  [4, 3, 7, 1, 8, 6, 5, 2]
Output: (2, 4, 6, 8) (1, 3, 5, 7)
"""
import json
data = json.loads(input())

def create_chunks(data):
    even = [el for el in data if el % 2 == 0]
    odd = [el for el in data if el not in even]
    even = ', '.join(map(str, sorted(even)))
    odd = ', '.join(map(str, sorted(odd)))
    return f'({even}) ({odd})'

result = create_chunks(data)
# print(result)


# Task 12
"""
Напишите код, который перемещает элементы списка items из начала списка в конец списка.
n - число элементов которые необходимо переместить.
Input:  3 | [1, 3, 2, 5, 9, 8, 1, 2]
Output: 5, 9, 8, 1, 2, 1, 3, 2
"""
import json
n, items = input().split(" | ")
n = int(n)
items = json.loads(items)

def move_first_to_end(n, items):
    ls = items[:n]
    items.extend(ls)
    return ', '.join(map(str, items[n:]))

result = move_first_to_end(n, items)
# print(result)


# Task 13
"""
Напишите код, который копирует элементы списка items из начала списка в конец списка 
и записывается результат в переменную result.
n - число элементов которые необходимо скопировать.
Input:  2 | [1, 2, 3]
Output: 1, 2, 3, 1, 2
"""
import json
n, items = input().split(" | ")
n = int(n)
items = json.loads(items)

def copy_first_to_end(n, items):
    ls = items[:n]
    items.extend(ls)
    return ', '.join(map(str, items))

result = copy_first_to_end(n, items)
# print(result)


# Task 14
"""
https://stepik.org/lesson/957398/step/14?unit=963831
Input:  70 | ["Меч", "Щит", "Свиток", "Зелье"]
Output: 80
"""
import json
health, items = input().split(" | ")
health = int(health)
items = json.loads(items)


def update_health(health, items):
    res = health + items.count("Зелье") * 10
    return min(res, 100)

result = update_health(health, items)
# print(result)


# Task 15
"""
https://stepik.org/lesson/957398/step/15?unit=963831
Input:  70 | ["Меч", "Щит", "Кофе", "Зелье", "Энергетик"]
Output: 85
"""
import json
power, items = input().split(" | ")
power = int(power)
items = json.loads(items)

def update_power(power, items):
    res = power + items.count("Энергетик") * 5 + items.count("Кофе") * 10
    return min(res, 100)

result = update_power(power, items)
# print(result)


# Task 16
"""
Напишите код, который складывает все числа одного списка с числами второго списка 
и записывает результат через запятую в переменную result.
Input:  [2, 1, 3] | [1, 2, 2]
Output: 3, 3, 5
"""
import json
list1, list2 = map(json.loads, input().split(" | "))

def sum_lists(list1, list2):
    res = map(sum, zip(list1, list2))
    # res = [a + b for a, b in zip(list1, list2)]
    return ', '.join(map(str, res))

result = sum_lists(list1, list2)
# print(result)
