#  10 Списки. Часть 2
""""""

# Task 01
"""
data - список чисел произвольного размера.
order - порядок сортировки.
Упорядочить цифры каждого числового элемента в списке data в 
порядке возрастания (ASC) или убывания (DESC) и создает новый список.
Input:  [321,42,991] | ASC
Output: [123,24,199]
"""
import json
data, order = map(str.strip, input().split(" | "))
data = json.loads(data)
order = str(order)

def custom_sort(data, order):
    res = [''.join(sorted(str(el), reverse=(order == 'DESC'))) for el in data]
    return [int(el) for el in res]

result = custom_sort(data, order)
# print(json.dumps(result, separators=(',', ':')))


# Task 02
"""
data - список чисел произвольного размера.
shift - сдвиг.
Выполнить кольцевой циклический сдвиг элементов списка вправо на значение переменной shift.
Input:  [1, 2, 3, 4, 5, 6] | 2
Output: [5,6,1,2,3,4]
"""
import json
data, shift = map(str.strip, input().split(" | "))
data = json.loads(data)
shift = int(shift)

def cyclic_right_shift(data, shift):
    # shift %= len(data)
    # res = data[-shift:] + data[:-shift]
    # return res

    # shift %= len(data)
    # for i in range(shift):
    #     data.insert(0, data.pop())
    # return data

    ln = len(data)
    res = [data[(i - shift) % ln] for i in range(ln)]
    return res

result = cyclic_right_shift(data, shift)
# print(json.dumps(result, separators=(',', ':')))


# Task 03
"""
data - двумерный список чисел произвольного размера.
shift - сдвиг.
Выполнить кольцевой циклический сдвиг элементов списка влево на значение переменной shift.
Input:  [[1,2,3],[1,2,3]] | 1
Output: [[2,3,1],[2,3,1]]
"""
import json
data, shift = map(str.strip, input().split(" | "))
data = json.loads(data)
shift = int(shift)

def cyclic_left_shift(data, shift):
    res = []
    for el in data:
        ln = len(el)
        ls = [el[(i + shift) % ln] for i in range(ln)]
        res.append(ls)
    return res

result = cyclic_left_shift(data, shift)
# print(json.dumps(result, separators=(',', ':')))


# Task 04
"""
data - двумерный список чисел произвольного размера.
shift - сдвиг.
Выполнить кольцевой циклический сдвиг элементов списка влево на значение переменной shift.
Input:  [[1,2,3],[1,2,3]] | 1
Output: [[2,3,1],[2,3,1]]
"""
import json
data, shift = map(str.strip, input().split(" | "))
data = json.loads(data)
shift = int(shift)

def cyclic_left_shift(data, shift):
    res = []
    for el in data:
        ln = len(el)
        ls = [el[(i + shift) % ln] for i in range(ln)]
        res.append(ls)
    return res

result = cyclic_left_shift(data, shift)
# print(json.dumps(result, separators=(',', ':')))


# Task 05
"""
data - двумерный список чисел произвольного размера.
shift - сдвиг.
Выполнить кольцевой циклический сдвиг элементов списка вправо на значение переменной shift.
Input:  [[1,2,3],[1,2,3]] | 1
Output: [[3,1,2],[3,1,2]]
"""
import json
data, shift = map(str.strip, input().split(" | "))
data = json.loads(data)
shift = int(shift)

def cyclic_right_shift(data, shift):
    res = []
    for el in data:
        ln = len(el)
        ls = [el[(i - shift) % ln] for i in range(ln)]
        res.append(ls)
    return res

result = cyclic_right_shift(data, shift)
# print(json.dumps(result, separators=(',', ':')))


# Task 06
"""
Используя переменные width,height,
создать новый двумерный список (прямоугольник из единиц)
Input:  3 | 5
Output: [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
"""
import json
width, height = map(int, input().split(" | "))

def create_rectangle(width, height):
    return [[1] * width for _ in range(height)]

result = create_rectangle(width, height)
# print(json.dumps(result, separators=(',', ':')))


# Task 07
"""
Создать двумерный список по следующему правилу: 
на главной диагонали должны быть записаны числа 0. 
На двух диагоналях, прилегающих к главной, числа 1. 
На следующих двух диагоналях числа 2, и т.д.    Например:
n = 4
 [[ 0, 1, 2, 3 ], 
  [ 1, 0, 1, 2 ], 
  [ 2, 1, 0, 1 ], 
  [ 3, 2, 1, 0 ]]

n = 5  
 [[0, 1, 2, 3, 4],
  [1, 0, 1, 2, 3],
  [2, 1, 0, 1, 2],
  [3, 2, 1, 0, 1],
  [4, 3, 2, 1, 0]]

Input:  5
Output: [[0,1,2,3,4],[1,0,1,2,3],[2,1,0,1,2],[3,2,1,0,1],[4,3,2,1,0]]
"""
n = 5
def fill_diagonal_list(n):
    # mask = list(range(n, 0, -1)) + list(range(n + 1))  # [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]  n = 5
    # res = [mask[el:el + n][::-1] for el in range(1, n + 1)]
    res = [[abs(el - i) for i in range(n)] for el in range(n)]
    return res

result = fill_diagonal_list(n)
# print(result)


# Task 08
"""
Создать двумерный список по следующему правилу: 
Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
Числа, стоящие выше этой диагонали, равны 0.
Числа, стоящие ниже этой диагонали, равны 2.    Например:
n = 4
 [[ 0, 0, 0, 1 ], 
  [ 0, 0, 1, 2 ], 
  [ 0, 1, 2, 2 ], 
  [ 1, 2, 2, 2 ]]

n = 5  
 [[ 0, 0, 0, 0, 1 ],
  [ 0, 0, 0, 1, 2 ],
  [ 0, 0, 1, 2, 2 ],
  [ 0, 1, 2, 2, 2 ],
  [ 1, 2, 2, 2, 2 ]]

Input:  4
Output: [[0,0,0,1],[0,0,1,2],[0,1,2,2],[1,2,2,2]]

Input:  5
Output: [[0,0,0,0,1,2],[0,0,1,2,2],[0,1,2,2,2],[1,2,2,2,2]]
"""
import json
n = int(input())

def fill_diagonal_list(n):
    mask = list([0] * (n - 1)) + [1] + list([2] * (n + 1))
    res = [mask[el:el + n] for el in range(n)]
    return res

def fill_diagonal_list(n):
    res = [[1 if i == j else (2 if j < i else 0) for j in range(n)][::-1] for i in range(n)]
    return res

result = fill_diagonal_list(n)
# print(json.dumps(result, separators=(',', ':')))


# Task 09
"""
data - список произвольного размера.
Заменить в нем  все числа, меньшие последнего элемента списка, на первый элемент.
Input:  [3, 7, 10, 5, 1, 9]
Output: [3,3,10,3,3,9]
"""
import json
data = json.loads(input())

if data:
    first, end = data[0], data[-1]
    result = [first if el < end else el for el in data]
else:
    result = []

print(json.dumps(result, separators=(',', ':')))



# Task 10
"""
data - список произвольного размера.
Заменить в нем наибольший четный элемент списка и поменять его местами с наименьшим нечетным элементом. 
Если одного из таких элементов нет, то всем элементам массива присвоить значение, равное нулю.
Input:  [3, 7, 2, 5, 1, 9]
Output: [3,7,1,5,2,9]
"""
# import json
# data = json.loads(input())
data = [3, 7, 2, 5, 1, 9]

def swap_elements(data):
    even = [i for i in data if i % 2 == 0]
    odd = [i for i in data if i % 2 != 0]
    if even and odd:
        max_even, min_odd = max(even), min(odd)
        idx_even, idx_odd = data.index(max_even), data.index(min_odd)
        data[idx_even] = min_odd
        data[idx_odd] = max_even
        return data
    return [0 for _ in data]

result = swap_elements(data)
# print(json.dumps(result, separators=(',', ':')))


# Task 11
"""
data - список чисел.
Найти подсписок в списке data, у которого произведение всех элементов максимально среди всех возможных подсписков. 
Примечание: Подсписки для "data" - это варианты среза "data"
Input:  [-6,4,-5,8,-10,0,8]
Output: 1600
"""
# import json
# data = json.loads(input())
data = [40, 0, -20, -10]

result = 0
size = len(data)
for i in range(size - 1):
    multiply_num = data[i - size]
    data = data[i - size + 1:]
    data_num = []
    for el in data:
        multiply_num *= el
        data_num.append(multiply_num)
    if max(data_num) > result:
        result = max(data_num)

print(result)

# Task 12 - не решено

# Task 13
"""
data - список целых чисел, эти числа обозначают температуру в конкретный день.
Для каждого дня найти количество суток до наступления более тёплого дня. 
Input:  [17,16,19,15,13,18,20]
Output: [2,1,4,2,1,1,0]
"""
# data = [17, 16, 19, 15, 13, 18, 20]  # [2,1,4,2,1,1,0]
# data = [20, 21, 23, 15, 13, 18, 20]  # [1,1,0,2,1,1,0]
# data = [20, 24, 23]  # [1,0,0]
import json
data = json.loads(input())

def swap_elements(data):
    result = []
    ln = len(data)
    for i in range(ln):
        for k in range(i + 1, ln):
            if data[i] < data[k]:
                result.append(k - i)
                break
        else:  # отработает, если цикл для "k" не прервется.
            result.append(0)
    return result

# Вариант хуже
# Через "flag" без блока "else" в цикле для "k"
def swap_elements(data):
    result = []
    flag = True
    for el in range(len(data)):
        for k in range(el + 1, len(data)):
            if data[el] < data[k]:
                result.append(k - el)
                flag = False
                break
        if flag:
            result.append(0)
        flag = True
    return result

result = swap_elements(data)
# print(json.dumps(result, separators=(',', ':')))
# print(result)


# Task 12
"""
https://stepik.org/lesson/957414/step/12?unit=963847
data - строка
d - список (словарь)
Напишите код, который анализирует строку data и
возвращает массив всех возможных комбинаций слов, которые образуют исходную строку.

Input:  Wordbreakproblem
        ["this","th","is","famous","Word","break","b","r","e","a","k","br","bre","brea","ak","problem"]

Output: ["Word b r e a k problem",
        "Word b r e ak problem",
        "Word br e a k problem",
        "Word br e ak problem",
        "Word bre a k problem",
        "Word bre ak problem",
        "Word brea k problem",
        "Word break problem"]
"""
import json
data, d = map(str.strip, input().split(" | "))
d = json.loads(d)

from itertools import permutations, chain
def parse(data, d):
    ls = chain(*map(lambda x: permutations(d, x), range(len(d) + 1)))
    result = [' '.join(el) for el in ls if ''.join(el) == data]
    result.sort()
    return sorted(result)

# print(json.dumps(result := parse(data, d), separators=(',', ':')))

