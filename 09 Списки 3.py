#  09 Списки. Часть 3
""""""

# Task 01
"""
Напишите код, который проходит по списку data, 
удаляет все нулевые элементы списка и записывает новый список в переменную result.
Input:  [0,1,0,1,1,1,0,1]
Output: [1,1,1,1,1]
"""
import json
data = json.loads(input())

def remove_zeros(data):
    # return [el for el in data if el != 0]
    # return list(filter(lambda x: x == 1, data))
    return list(filter(lambda x: x, data))


result = remove_zeros(data)
print(json.dumps(result, separators=(',', ':')))


# Task 02
"""
Напишите код, который проходит по списку data, 
и записывает символы вместе с числом их повторений в переменную result.
Input:  ["a", "a", "a", "b", "b", "c", "c", "a", "a", "a"]
Output: a3b2c2a3
"""
import json
data = json.loads(input())


# лучший вариант
# https://docs-python.ru/standart-library/modul-itertools-python/funktsija-groupby-modulja-itertools/
# https://pythonz.net/references/named/itertools.groupby/


# from itertools import groupby
# def compress(data):
#     res = ''
#     for k, v in groupby(data):
#         res += f'{k}{len(list(v))}'
#     return res

def compress(data):
    char, cnt, res = data[0], 1, ""
    for el in data[1:]:
        if char == el:
            cnt += 1
        else:
            res += f"{char}{cnt}"
            char, cnt = el, 1
    res += f"{char}{cnt}"  # для последней итерации
    return res


result = compress(data)
# print(result)


# Task 03
"""
Напишите код, который:
Читает строку message  вида: a2b3c1
Воссоздает список: a2b3c1 -> ["a","a","b","b","b","c"]
Записывает воссозданный список через запятую в переменную result.
!!!  Число повторяющихся букв всегда от 1 до 9.
Input:  a2b3c1
Output: a, a, b, b, b, c
"""
message = input().strip()

def decompress(message):
    chr, num = message[::2], message[1::2]
    res = [', '.join(el * int(num)) for el, num in zip(chr, num)]
    return ', '.join(res)

result = decompress(message)
# print(result)


# Task 04
"""
https://stepik.org/lesson/957399/step/4?unit=963832
Напишите код, который находит сумму всех чисел по двум диагоналям двумерного списка grid .
Код должен работать для любого размера двухмерного списка grid например: 2х2, 3х3, 4х4 и тд...
Важно! Вам необходимо убедиться в том, что размер списка по высоте и ширине одинаковый! 
Если размеры списка grid тогда записываем сообщение "Список некорректный".
Input:  [[1, 0, 1],[0, 1, 0],[1, 1, 1]]
Output: 6
"""
import json
grid = json.loads(input())

def calculate_sum(grid):
    size = len(grid)
    if len(grid[0]) == size:
        main, second = 0, 0
        for i in range(size):
            main += grid[i][i]
            second += grid[i][size - i - 1]  # индекс положительный
            # second += grid[i][- i - 1]  # индекс отрицательный
        return main + second
    return 'Список некорректный'

def calculate_sum(data):
    size = len(data)
    if size != len(data[0]):
        return 'Список некорректный'
    return sum(data[i][i] + data[i][size - i - 1] for i in range(size))

result = calculate_sum(grid)
# print(result)


# Task 05
"""
Напишите код, который находит сумму всех чисел по четырем границам двумерного списка grid.
Код должен работать для любого размера двухмерного списка grid например: 2х2, 3х3, 4х4 и тд...
Input:  [[1, 1, 1],[1, 2, 1],[1, 1, 1]]
Output: 12
"""
import json
grid = json.loads(input())

def calculate_sum(grid):
    res = 0
    for _ in range(4):
        grid = list(zip(*grid[::-1]))
        res += sum(grid[0])
    return res

def calculate_sum(grid):
    trans = [list(row) for row in zip(*grid)]
    grid[0].extend(grid[-1])
    trans[0].extend(trans[-1])
    return sum(grid[0]) + sum(trans[0])

result = calculate_sum(grid)
print(result)


# Task 06
"""
https://stepik.org/lesson/957399/step/6?unit=963832
Напишите код, который суммирует числа в списке data между числами start и end включительно.
Пример1. Eсли start = 2, end = 4, data = [1, 2, 3, 4, 5] тогда 2 + 3 + 4 = 9
Пример2. Eсли start = 42, end = 1, data = [1, 2, 3, 3, 5] тогда 0 + 0 = 0
Input:  [1, 2, 3, 3, 5] | 1 | 3
Output: 9
"""
import json

data, start, end = map(str.strip, input().split(" | "))
data = json.loads(data)

def calculate_sum_between(data, start, end):
    res = [el for el in data if int(start) <= el <= int(end)]
    return sum(res)

result = calculate_sum_between(data, start, end)
# print(result)


# Task 07
"""
Напишите код, который суммирует числа в списке data между элементами start и end.
Если в списке нет элементов start и end тогда записываем сообщение: Неверный формат списка
Важно!
Элемент start всегда должен идти перед элементом end.
Eсли это условия не соблюдено, тогда записываем сообщение: Неверный формат списка
Input:  [1, 2, "start", 2, 2, 1, "end", 1, 5]
Output: 5
"""
import json
data = json.loads(input())

def sum_between_start_and_end(data):
    if 'start' in data and 'end' in data:
        start = data.index('start')
        end = data.index('end')
        if end > start:
            return sum(data[start + 1:end])
    return 'Неверный формат списка'

result = sum_between_start_and_end(data)
# print(result)


# Task 08
"""
Напишите код, который проверяет все элементы в списке и записывает в новый список только числа.
Новый список записать через запятую.
Input:  [null, 42, "Лия", false, 3.14, true]
Output: 42, 3.14
"""
import json
data = json.loads(input())

def filter_only_numbers(data):
    return ', '.join([str(el) for el in data if type(el) in (int, float)])

result = filter_only_numbers(data)
# print(result)


# Task 09
"""
Напишите код, который проверяет все элементы в списке
и записывает в новый список только логические значения True и False.
Новый список записать через запятую в переменную.
Input:  [null, 42, "Макс", false, 3.14, true]
Output: False, True
"""
import json
data = json.loads(input())

def filter_only_bool(data):
    return ', '.join([str(el) for el in data if type(el) == bool])

result = filter_only_bool(data)
# print(result)


# Task 10
"""
Напишите код, который проверяет все элементы в списке и записывает в новый список все значения кроме None.
Новый список записать через запятую в переменную.
Input:  [null, 42, "Макс", false, 3.14, true]
Output: 42, Макс, False, 3.14, True
"""
import json
data = json.loads(input())

def filter_not_null_only(data):
    return ", ".join(map(str, [el for el in data if el is not None]))

result = filter_not_null_only(data)
# print(result)


# Task 11
"""
Напишите код, который проверяет все ли элементы в списке data одинаковые и записывает логический результат
Input:  [42, 42, 42, 42]
Output: True
"""
import json
data = json.loads(input())

def is_eq(data):
    return len(set(data)) == 1
    # return all([el == data[0] for el in data])

result = is_eq(data)
# print(result)


# Task 12
"""
Напишите код, который отображает зеркально список data в новом списке и записывает результат через запятую
Input:  [1, 2, 3]
Output: 1, 2, 3, 2, 1
"""
import json
data = json.loads(input())

def mirror_list(data):
    data.extend(data[-2::-1])
    return ', '.join(map(str, data))

result = mirror_list(data)
# print(result)


# Task 13
"""
Напишите код, который принимает список чисел data и возвращает новый список, 
в котором все отрицательные числа заменены на 0
Input:  [1, 3, 0, -1, 2, 5]
Output: [1,3,0,0,2,5]
"""
import json

data = json.loads(input())
def replace_negative_with_zero(data):
    for i in range(len(data)):
        if data[i] < 0:
            data[i] = 0
    return data

def replace_negative_with_zero(data):
    return [max(el, 0) for el in data]
   # return list(map(lambda el: el if el > 0 else 0, data))

result = replace_negative_with_zero(data)
print(json.dumps(result, separators=(',', ':')))


# Task 14
"""
Напишите код, который определяет, имеются ли в списке два подряд идущих нуля и записывает логический результат
Input:  [1, 2, 3, 0, 1, 0]
Output: False
"""
import json
data = json.loads(input())


def has_two_consecutive_zeros(data):
    for i in range(1, len(data)):
        if data[i - 1] == data[i] == 0:
        # if data[i - 1] == 0 and data[i] == 0:
            return True
    return False

def has_two_consecutive_zeros(data):
    return any(data[i - 1] == data[i] == 0 for i in range(len(data)))

result = has_two_consecutive_zeros(data)
# print(result)


# Task 15
"""
Напишите код, который вместо каждого элемента с нулевым значением поставляет сумму двух предыдущих элементов списка 
и записывает результат в виде нового списка
Input:  [1, 0, 2, 0, 3, 4, 0]
Output: [1,0,2,2,3,4,7]
"""
import json
data = json.loads(input())

def replace_zeros(data):
    for i in range(2, len(data)):
        if data[i] == 0:
            data[i] = sum(data[i - 2: i])
    return data

result = replace_zeros(data)
print(json.dumps(result, separators=(',', ':')))

