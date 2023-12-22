#  09 Списки. Часть 4
""""""

# Task 01
"""
Напишите код, который заменяет все логические значения True на строковое "on", 
а все логические значения False на "off" 
Input:  [true,false,1,"hello",false,true]
Output: ["on","off",1,"hello","off","on"]
"""
import json
data = json.loads(input())

def boolean_to_string(el):
    if isinstance(el, bool):
        if el:
            return 'on'
        return 'off'
    return el

result = [boolean_to_string(el) for el in data]
print(json.dumps(result, separators=(',', ':')))


def boolean_to_string(data):
    for i, el in enumerate(data):
        if isinstance(el, bool):
            if data[i]:
                data[i] = 'on'
            else:
                data[i] = 'off'
    return data

result = boolean_to_string(data)
print(json.dumps(result, separators=(',', ':')))


# Task 02
"""
Напишите код, который выбирает первый положительный элемент из списка data 
и записывает результат в переменную result.
Если положительный элемент не найден, тогда возвращаем None
Input:  [-5, -3, 2, 4, 6]
Output: 2
"""
import json
data = json.loads(input())

def find_first_positive(data):
    for el in data:
        if el > 0:
            return el
#    return None  # Не обязательно - функция и так вернет None

result = find_first_positive(data)
# print(result)


# Task 03
"""
Напишите код, который выбирает первый отрицательный элемент из списка data 
и записывает результат в переменную result.
Если отрицательный элемент не найден, тогда возвращаем None
Input:  [2, 3, 4, 1, -2, -1]
Output: -2
"""
import json
data = json.loads(input())

def find_first_negative(data):
    # return next((el for el in data if el < 0), None)
    for el in data:
        if el < 0:
            return el

result = find_first_negative(data)
# print(result)


# Task 04
"""
Напишите код, который выбирает максимальный по модулю элемент из списка data
Input:  [-5.4, 3.2, -7.6, 4.8, -2.1]
Output: -7.6
"""
import json
data = json.loads(input())

def find_max_absolute(data):
    # return max(data, key=lambda x: abs(x))
    return max(data, key=abs)

def find_max_absolute(data):
    res = [abs(el) for el in data]
    idx = res.index(max(res))
    return data[idx]

result = find_max_absolute(data)
# print(result)


# Task 05
"""
Напишите код, который заменяет числовые значения элементов списка data на противоположные и записывает новый список
Input:  [1, -5, 0, 3, -4]
Output: [-1,5,0,-3,4]
"""
import json
data = json.loads(input())

def find_max_absolute(data):
    return [-el for el in data]
    # return [el * -1 for el in data]

result = find_max_absolute(data)
print(json.dumps(result, separators=(',', ':')))


# Task 06
"""
Напишите код, который умножает все числовые значения элементов списка data 
на максимальный элемент списка data
Input:  [1, 2, 4, 5]
Output: [5,10,20,25]
"""
import json
data = json.loads(input())

def multiply_max(data):
    n = max(data)
    return [el * n for el in data]

result = multiply_max(data)
print(json.dumps(result, separators=(',', ':')))


# Task 07
"""
Напишите код, который умножает все числовые значения элементов списка data 
на минимальный элемент списка data
Input:  [2, 3, 4, 5, 6]
Output: [4,6,8,10,12]
"""
import json
data = json.loads(input())

def process_data(data):
    n = min(data)
    return [el * n for el in data]

result = process_data(data)
print(json.dumps(result, separators=(',', ':')))


# Task 08
"""
Напишите код, который выбирает элементы списка data, 
которые больше среднего арифметического списка data
Input:  [1, 2, 3, 4, 5]
Output: [4,5]
"""
import json
data = json.loads(input())
from statistics import mean  # среднее значение списка

def filter_above_average(data):
    n = mean(data)
    return [el for el in data if el > n]

result = filter_above_average(data)
print(json.dumps(result, separators=(',', ':')))


# Task 09
"""
Напишите код, который выбирает элементы списка data, 
которые больше, чем элементы, стоящие перед ними.
Input:  [3, 9, 8, 4, 5, 1]
Output: [9,5]
"""
import json
data = json.loads(input())

def get_greater_than_previous(data):
    res = []
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            res.append(data[i])
    return res

def get_greater_than_previous(data):
    return [data[i] for i in range(1, len(data)) if data[i] > data[i - 1]]


result = get_greater_than_previous(data)
print(json.dumps(result, separators=(',', ':')))


# Task 10
"""
Напишите код, который находит все файлы в список files с расширением .png 
и записывает новый список.
Input:  ["image1.png", "image2.jpg", "image3.png", "image4.gif"]
Output: ["image1.png","image3.png"]
"""
import json
files = json.loads(input())

def find_files(files):
    return [el for el in files if el[-4:] == '.png']
    # return [el for el in files if el.split('.')[1] == 'png']
    # result = list(filter(lambda el: el.endswith('.png'), files))

result = find_files(files)
print(json.dumps(result, separators=(',', ':')))


# Task 11
"""
Напишите код, который находит все файлы в списке files, которые начинаются с  image
Input:  ["image1.png", "index.php", "buttons.js", "image4.gif"]
Output: ["image1.png","image4.gif"]
"""
import json
files = json.loads(input())

def find_files(files):
    # return [el for el in files if el[:5] == 'image']
    return [el for el in files if el.startswith('image')]
    # return list(filter(lambda el: el.startswith('image'), files))

result = find_files(files)
print(json.dumps(result, separators=(',', ':')))


# Task 12
"""
Напишите код, который находит сумму элементов для каждой строки двумерного списка data
Input:  [[1,2,3,4,5],[5,5,3,2,3],[2,1,2,3,5]]
Output: [15,18,13]
"""
import json
data = json.loads(input())
def row_sum(data):
    return [sum(el) for el in data]

result = row_sum(data)
print(json.dumps(result, separators=(',', ':')))


# Task 13
"""
Напишите код, который находит сумму элементов для каждого столбца двумерного списка data
Input:  [[1,2,3,4,5],[5,5,3,2,3],[2,1,2,3,5]]
Output: [8,8,8,9,13]
"""
import json
data = json.loads(input())

def column_sum(data):
    # return [sum(el) for el in zip(*data)]
    return list(map(sum, zip(*data)))

result = column_sum(data)
print(json.dumps(result, separators=(',', ':')))


# Task 14
"""
https://stepik.org/lesson/957400/step/14?unit=963833
data - список чисел произвольного размера. Количество элементов всегда четное.
Напишите код, который определяет вес левой и правой стороны списка. 
    Если левая сторона имеет больший вес, тогда записываем сообщение: Левая сторона тяжелее
    Если правая сторона имеет больший вес, тогда записываем сообщение: Правая сторона тяжелее
    Если вес обеих сторон имеют одинаковый, тогда записываем сообщение: Обе стороны сбалансированы
Input:  [4, 2, 1, 4, 3, 3]
Output: Правая сторона тяжелее
"""
import json
data = json.loads(input())

def balance(data):
    ls = ['Левая сторона тяжелее', 'Правая сторона тяжелее', 'Обе стороны сбалансированы']
    n = len(data) // 2
    left = sum(data[:n])
    right = sum(data[n:])
    if left > right:
        return ls[0]
    elif left < right:
        return ls[1]
    return ls[2]
    # return ls[0] if left > right else(ls[1] if left < right else ls[2])

result = balance(data)
# print(result)
