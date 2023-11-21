#  10 Списки. Часть 1
""""""

# Task 01
"""
Дана переменная height.
Напишите код, который создает двумерный список с равнобедренным треугольником. Где:
1 - тело треугольника
0 - пустота.
Если height = 3 тогда:
 [[ 0, 0, 1, 0, 0 ], 
  [ 0, 1, 1, 1, 0 ], 
  [ 1, 1, 1, 1, 1 ]]

"""
import json
height = int(input())

def create_triangle(height):
    result = [[] for _ in range(height)]
    for n in range(height):
        zero = [0] * (height - n - 1)
        one = [1] * (2 * n + 1)
        result[n].extend(zero + one + zero)
    return result

result = create_triangle(height)
print(json.dumps(result, separators=(',', ':')))


# Task 02
"""
Дана переменная size.
Напишите код, который создает двумерный список с квадратом
size = 4 тогда:
 [[1,1,1,1],
  [1,1,1,1],
  [1,1,1,1],
  [1,1,1,1]]
"""
import json
size = int(input())

def create_square(size):
    return [[1] * size for _ in range(size)]

result = create_square(size)
print(json.dumps(result, separators=(',', ':')))


# Task 03
"""
Подсчитать количество вложенных списков в списке data.
Input:  [1, [2, 3], 3, [4, [5]]]
Output: 3
"""
import json
data = json.loads(input())

# рекурсия
def count_nested_lists(data):
    total = 0
    for i in data:
        if isinstance(i, list):
            total += count_nested_lists(i) + 1
    return total

# Через строку
def count_nested_lists(data):
    return str(data).count('[') - 1

result = count_nested_lists(data)
# print(result)


# Task 04
"""
Подсчитать количество элементов в списке data (+ во всех вложенных списках).
Input:  [1, [2], [3, 4, [5, 6, [7, 8, [9, 10]]]]]
Output: 10
"""
import json
data = json.loads(input())

def count_list_elements(data):
    st = str(data)
    for el in '[]':
        st = st.replace(el, '')
    ls = list(map(int, st.split(', ')))
    return len(ls)

result = count_list_elements(data)
# print(result)

# рекурсия
def count_list_elements(data):
    result = []
    for item in data:
        if isinstance(item, list):
            result.extend(count_list_elements(item))
        else:
            result.append(item)
    return result

result = len(count_list_elements(data))
# print(result)


# Task 05
"""
Подсчитать сумму значений элементов в списке data (+ во всех вложенных списках).
Input:  [[1], [1, 1, [2, 2, [3, 3]]]]
Output: 13
"""
import json
data = json.loads(input())

def sum_list(data):
    result = []
    for el in data:
        if isinstance(el, list):
            result.extend(sum_list(el))
        else:
            result.append(el)
    return result

# Вариант
def sum_list(data):
    return sum(sum_list(el) if isinstance(el, list) else el for el in data)

result = sum(sum_list(data))
# print(result)


# Task 06
"""
Подсчитать сумму нечетных значений элементов в списке data (+ во всех вложенных списках).
Input:  [1, 2, [1], [1, 1, [2, 2, [3, 3]]]]
Output: 10
"""
import json
data = json.loads(input())

def sum_list_odd_elements(data):
    result = []
    for el in data:
        if isinstance(el, list):
            result.extend(sum_list_odd_elements(el))
        else:
            result.append(el)
    return result

result = sum(el * (el % 2) for el in sum_list_odd_elements(data))

# Вариант
def sum_list_odd_elements(data):
    return sum(sum_list_odd_elements(el) if isinstance(el, list) else el * (el % 2) for el in data)

result = sum_list_odd_elements(data)
# print(result)


# Task 07
"""
Подсчитать сумму четных значений элементов в списке data (+ во всех вложенных списках).
Input:  [1, 2, [2, 1, [3, 1]]]
Output: 4
"""
import json
data = json.loads(input())

def sum_list_even_elements(data):
    result = []
    for el in data:
        if isinstance(el, list):
            result.extend(sum_list_even_elements(el))
        else:
            result.append(el)
    return result

result = sum(el for el in sum_list_even_elements(data) if el % 2 == 0)

# Вариант
def sum_list_even_elements(data):
    return sum(sum_list_even_elements(el) if isinstance(el, list) else el * ((el + 1) % 2) for el in data)

result = sum_list_even_elements(data)
# print(result)


# Task 08
"""
Подсчитать сумму пропущенных чисел из списка data. Например: 
[1,5]=2+3+4=9
[1,2,3]=0

Input:  [1, 3, 5]
Output: 6
"""
import json
data = json.loads(input())

def sum_of_missing_numbers(data):
    result = 0
    for i in range(len(data) - 1):
        if (data[i + 1] - data[i]) != 1:
            result += sum(range(data[i] + 1, data[i + 1]))
    return result

# Вариант
def sum_of_missing_numbers(data):
    start, end = data[0], data[-1] + 1
    return sum(set(range(start, end)).difference(data))

result = sum_of_missing_numbers(data)
# print(result)


# Task 09
"""
Подсчитать сумму пропущенных четных чисел из списка data. Например: 
[1,5]=2+4=6
[1,2,3]=0

Input:  [1, 3, 5]
Output: 6
"""
import json
data = json.loads(input())

def sum_of_missing_numbers(data):
    start, end = data[0], data[-1] + 1
    # return sum(el * ((el + 1) % 2) for el in set(range(start, end)).difference(data))
    # return sum(el for el in set(range(start, end)).difference(data) if el % 2 == 0)
    return sum(el for el in range(start, end) if el not in data and el % 2 == 0)

result = sum_of_missing_numbers(data)
# print(result)


# Task 10
"""
Подсчитать сумму пропущенных нечетных чисел из списка data. Например: 
[1,2,5,8]=3+7=10
[1,2,3]=0

Input:  [1, 2, 5, 8]
Output: 8
"""
import json
data = json.loads(input())

def sum_of_missing_numbers(data):
    start, end = data[0], data[-1] + 1
    return sum(el * (el % 2) for el in set(range(start, end)).difference(data))
    # return sum(el for el in set(range(start, end)).difference(data) if el % 2 != 0)
    # return sum(el for el in range(start, end) if el not in data and el % 2 != 0)

result = sum_of_missing_numbers(data)
# print(result)


# Task 11
"""
Напишите код, который сопоставляет первое число в списке с последним, второе число с предпоследним и т.д.. Например: 
[1,2,3,4]=(1,4),(2,3)
[1,2,3]=(1,3),(2,2)
[]=()

Input:  [1,2,3]
Output: (1,3),(2,2)
"""
import json
data = json.loads(input())

def sum_of_misspairs(data):
    full, half = len(data), len(data) // 2
    revers = data[::-1]
    if full:
        if not full % 2:
            data = data[:half]
        else:
            data = data[:half + 1]
        return ','.join([str(el) for el in zip(data, revers)])
    return '()'

# Вариант
def sum_of_misspairs(data):
    if not data:
        return '()'
    else:
        res = []
        while data:
            res.append(f'({data[0]},{data[-1]})')
            data = data[1:-1]
        return ','.join(res)

result = sum_of_misspairs(data).replace(' ', '')
# print(result)


# Task 12
"""
data - двумерный список, который содержит различные пользовательские данные.
Подсчитать количество схожих элементов двумерного списка.
Важно! Отсортировать результат в порядке возрастания!. Например: 

Input:  0: 8, 1: 8, 2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 6, 8: 7, 9: 8
Output: 
 [[2, 4, 1, 9, 0, 7, 3, 8],
  [6, 0, 5, 1, 8, 9, 4, 3],
  [7, 6, 2, 1, 3, 0, 5, 9],
  [8, 1, 9, 3, 2, 7, 4, 0],
  [4, 2, 7, 9, 1, 0, 6, 8],
  [0, 8, 1, 6, 7, 5, 9, 4],
  [5, 7, 2, 8, 1, 3, 9, 0],
  [9, 8, 6, 5, 3, 1, 0, 2]]
"""
import json
data = json.loads(input())

def count_elements(data):
    lst = []
    [lst.extend(el) for el in data]
    key = sorted(set(lst))
    return ', '.join([f'{el}: {lst.count(el)}' for el in key])

result = count_elements(data)
# print(result)


# Task 13
"""
Проверить является ли список data отсортированным или нет.
Input:  [1, 2, 3, 4, 5]
Output: True
"""
import json
data = json.loads(input())

def is_sorted(data):
    ls = sorted(data)
    return data == ls

result = is_sorted(data)
# print(result)


# Task 14
"""
Напишите код, который проходит по списку data и создает новый список с элементами исходного списка, 
хранящимися в вложенных списках. Элементы с одинаковым значением должны находиться в одном вложенном списке. 
Важно!
Вложенные списки должны быть созданы в порядке первого появления каждого элемента в списке data
Input:  [4,3,3,4,2,2,1,1,10,10,1,10]
Output: [[4,4],[3,3],[2,2],[1,1,1],[10,10,10]]
"""
import json
data = json.loads(input())

def advanced_sort(data):
    res = [[data[0]]]
    for item in data[1:]:
        idx = None
        for el in res:
            if el[0] == item:
                idx = res.index(el)
                break
        if idx is not None:
            res[idx].append(item)
        else:
            res.append([item])
    return res

result = advanced_sort(data)
# print(json.dumps(result, separators=(',', ':'), ensure_ascii=False))


# Task 15
"""
Напишите код, который сортирует список data особым способом. 
Результатом должен быть новый список, отсортированный в порядке возрастания (число, буква, число, буква и тд.)
Input:  [2,3,"а",1,"б",4,"д","г"]
Output: [1,"а",2,"б",3,"г",4,"д"]
"""
import json
data = json.loads(input())

def custom_sort(data):
    res = []
    num = sorted([el for el in data if str(el).isnumeric()])
    alfa = sorted([el for el in data if str(el).isalpha()])
    for k, v in list(zip(num, alfa)):
        res.append(k)
        res.append(v)
    sep = len(res) // 2
    if len(num) > sep:
        res.extend(num[sep:])
    elif len(alfa) > sep:
        res.extend(alfa[sep:])
    return res

# Вариант
def custom_sort(data):
    res = []
    num = sorted([el for el in data if str(el).isnumeric()], reverse=True)
    alpha = sorted([el for el in data if str(el).isalpha()], reverse=True)
    while num and alpha:
        res.append(num.pop())
        res.append(alpha.pop())
    res.extend(num)
    res.extend(alpha)
    return res

result = custom_sort(data)
# print(json.dumps(result, separators=(',', ':'), ensure_ascii=False))


# Task 16
"""
data - список слов произвольного размера.
order - порядок сортировки.
Упорядочить буквы каждого элемента в списке data в порядке возрастания (ASC) или убывания (DESC) и создать новый список
Input:  ["кгуде","вгa"] | ASC
Output: ["гдеку","aвг"]
"""
import json
data, order = map(str.strip, input().split(" | "))
data = json.loads(data)
order = str(order)

def custom_sort(data, order):
    res = [''.join(sorted(el, reverse=(order == 'DESC'))) for el in data]
    return res

result = custom_sort(data, order)
# print(json.dumps(result, separators=(',', ':'), ensure_ascii=False))

