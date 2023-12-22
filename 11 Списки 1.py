# 11 Списки 1
""""""

# Task 01
"""
Найти все возможные варианты из двух чисел в списке data, 
которые при сложении были бы равны значению переменной k.
Полученный результат в виде строки записать в формате: (x+y)(x+y)(x+y) и тд.
Если таких чисел не было найдено, тогда записать значение: ()
Input:  7 | [2, 3, 2, 4, 5]
Output: (2+5)(3+4)(2+5)
"""
import json
k, data = map(str.strip, input().split(" | "))
k = int(k)
data = json.loads(data)

def find_pairs(k, data):
    res = ''
    for i in range(len(data)):
        for v in range(i + 1, len(data)):
            if data[i] + data[v] == k:
                res += f"({data[i]}+{data[v]})"
    if res:
        return res
    return "()"

result = find_pairs(k, data)
# print(result)


# Task 02
"""
https://stepik.org/lesson/957417/step/2?unit=963850
0 - блок воды на карте
1 - блок земли на карте
Размер двумерного списка 4х4 
Input:  [[1,0,0,0],[1,0,1,0],[1,0,0,0],[1,0,0,0]]
Output: блоков воды: 11, блоков земли: 5
"""
import json
grid = json.loads(input())

def count_tiles(grid):
    ground = sum(map(sum, grid))
    # ground = sum(sum(el) for el in grid)
    return f"блоков воды: {16 - ground}, блоков земли: {ground}"


import numpy as np
def count_tiles(grid):
    arr = np.array(grid)
    return f'блоков воды: {arr.size - arr.sum()}, блоков земли: {arr.sum()}'

result = count_tiles(grid)
# print(result)


# Task 03
"""
https://stepik.org/lesson/957417/step/3?unit=963850
0 - блок воды на карте.
1 - блок земли на карте.
2 - блок корабля на карте.
Размер двумерного списка 4х4 
Input:  [[1,0,0,2],[1,2,1,0],[1,0,2,0],[1,2,0,2]]
Output: блоков воды: 6, блоков земли: 5, блоков кораблей: 5
"""
import json
grid = json.loads(input())

def count_tiles(grid):
    ground = sum([row.count(1) for row in grid])
    ship = sum([row.count(2) for row in grid])
    # ground = sum(sum(el for el in row if el == 1) for row in grid)
    # ship = sum(sum(el for el in row if el == 2) for row in grid) // 2
    return f"блоков воды: {16 - ground - ship}, блоков земли: {ground}, блоков кораблей: {ship}"


import numpy as np
def count_tiles(grid):
    arr = np.array(grid)
    ground = np.where(arr == 1)[0].size
    ship = np.where(arr == 2)[0].size
    # water = np.where(arr == 0)[0].size
    return f"блоков воды: {16 - ground - ship}, блоков земли: {ground}, блоков кораблей: {ship}"

result = count_tiles(grid)
# print(result)


# Task 04
"""
https://stepik.org/lesson/957417/step/4?unit=963850
0 - блок воды на карте.
1 - блок земли на карте.
2 - блок корабля на карте.
3 - блок вулкана на карте.
Размер двумерного списка 4х4 
Input:  [[1,0,0,2],[1,2,3,0],[1,0,0,0],[1,2,0,2]]
Output: блоков воды: 7, блоков земли: 4, блоков кораблей: 4, блоков вулканов: 1
"""
import json
grid = json.loads(input())

def count_tiles(grid):
    water = sum([row.count(0) for row in grid])
    ground = sum([row.count(1) for row in grid])
    ship = sum([row.count(2) for row in grid])
    volcano = sum([row.count(3) for row in grid])
    return f"блоков воды: {water}, блоков земли: {ground}, блоков кораблей: {ship}, блоков вулканов: {volcano}"


import numpy as np
def count_tiles(grid):
    arr = np.array(grid)
    water = np.where(arr == 0)[0].size
    ground = np.where(arr == 1)[0].size
    ship = np.where(arr == 2)[0].size
    volcano = np.where(arr == 3)[0].size
    return f"блоков воды: {water}, блоков земли: {ground}, блоков кораблей: {ship}, блоков вулканов: {volcano}"

result = count_tiles(grid)
# print(result)


# Task 05
"""
https://stepik.org/lesson/957417/step/5?unit=963850
Подсчитать количество столбцов где есть единица.
1 - есть элемент столбца
0 - пустота
Размер двумерного списка 6 х 3
Input:  [[0,1,0,1,0,0],[0,1,0,1,0,0],[1,1,0,1,1,0]]
Output: 4
"""
import json

grid = json.loads(input())


def count_towers(grid: list):
    # trans = zip(*grid)
    # return sum(1 for row in trans if sum(row) > 0)
    return sum(1 for row in zip(*grid) if sum(row) > 0)

    # return sum(map(any, zip(*grid)))

result = count_towers(grid)
print(result)


# Task 06
"""
https://stepik.org/lesson/957417/step/6?unit=963850
Подсчитать количество столбцов где НЕТ единицы.
1 - есть элемент столбца
0 - пустота
Размер двумерного списка 6 х 3
Input:  [[0,1,0,1,0,0],[0,1,0,1,0,0],[1,1,0,1,1,0]]
Output: 2
"""
import json
grid = json.loads(input())

def count_towers(grid: list):
    return sum(1 for row in zip(*grid) if sum(row) == 0)

result = count_towers(grid)
# print(result)



# Task 07
"""
https://stepik.org/lesson/957417/step/7?unit=963850
севере, востоке, юге, западе
0 - блок воды на карте.
1 - блок земли на карте.
2 - блок корабля на карте.
3 - блок вулкана на карте.
Размер двумерного списка 4х4 
Input:  [[1,0,0,2],[1,2,3,0],[1,0,0,0],[3,2,0,2]]
Output: Вулкан 1 граничит на севере с водой, на востоке с водой, на юге с водой, на западе с кораблем. 
        Вулкан 2 граничит на севере с землей, на востоке с кораблем.
"""
# import json
# # grid = json.loads(input())

def analyze_volcano(grid: list):
    cnt = 0
    res = []
    d = ['водой', 'землей', 'кораблем']
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 3:
                s = ''
                cnt += 1
                ls = []
                if row > 0:
                    ls.append(f"на севере с {d[grid[row - 1][col]]}")
                if col < 3:
                    ls.append(f"на востоке с {d[grid[row][col + 1]]}")
                if row < 3:
                    ls.append(f"на юге с {d[grid[row + 1][col]]}")
                if col > 0:
                    ls.append(f"на западе с {d[grid[row][col - 1]]}")
                s += f"Вулкан {cnt} граничит {', '.join(ls)}"
                res.append(s)
    return '. '.join(res) + '.'


result = analyze_volcano(grid)
# print(result)


# Task 08
"""
https://stepik.org/lesson/957417/step/8?unit=963850
северо-востоке, севере, северо-западе
востоке, юго-востоке, юге, юго-западе, западе
0 - блок воды на карте.
1 - блок земли на карте.
2 - блок корабля на карте.
3 - блок вулкана на карте.
Размер двумерного списка 4х4 
Input:  [[1,0,0,2],[1,2,3,0],[1,0,0,0],[3,2,0,2]]
Output: Вулкан 1 граничит на северо-западе с водой, на севере с водой, 
        на северо-востоке с кораблем, на востоке с водой, на юго-востоке с водой, на юге с водой, 
        на юго-западе с водой, на западе с кораблем. 
        Вулкан 2 граничит на севере с землей, на северо-востоке с водой, на востоке с кораблем.
"""
import json
grid = json.loads(input())

def analyze_volcano(grid: list):
    cnt = 0
    res = []
    d = ['водой', 'землей', 'кораблем', 'вулканом']
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 3:
                s = ''
                cnt += 1
                ls = []
                if row > 0 and col > 0:
                    ls.append(f"на северо-западе с {d[grid[row - 1][col - 1]]}")
                if row > 0:
                    ls.append(f"на севере с {d[grid[row - 1][col]]}")
                if row > 0 and col < 3:
                    ls.append(f"на северо-востоке с {d[grid[row - 1][col + 1]]}")
                if col < 3:
                    ls.append(f"на востоке с {d[grid[row][col + 1]]}")
                if col < 3 and row < 3:
                    ls.append(f"на юго-востоке с {d[grid[row + 1][col + 1]]}")
                if row < 3:
                    ls.append(f"на юге с {d[grid[row + 1][col]]}")
                if col > 0 and row < 3:
                    ls.append(f"на юго-западе с {d[grid[row + 1][col - 1]]}")
                if col > 0:
                    ls.append(f"на западе с {d[grid[row][col - 1]]}")
                s += f"Вулкан {cnt} граничит {', '.join(ls)}"
                res.append(s)
    return '. '.join(res) + '.'

result = analyze_volcano(grid)
# print(result)


# Task 09
"""
https://stepik.org/lesson/957417/step/9?unit=963850
Опустить "1" в каждой колонке вниз.
Размер Размер двумерного списка  может быть любым.
Input:  [[1,1,1,0,0],[0,0,0,1,0],[1,1,0,0,1],[0,0,0,1,0]]
Output: [[0,0,0,0,0],[0,0,0,0,0],[1,1,0,1,0],[1,1,1,1,1]]
"""
import json
grid = json.loads(input())

def gravity_switch(grid: list):
    trans = map(sorted, zip(*grid))
    back = list(map(list, zip(*trans)))
    return back
result = gravity_switch(grid)
print(json.dumps(result, separators=(',', ':')))


# Task 10
"""
https://stepik.org/lesson/957417/step/10?unit=963850
Поднять "1" в каждой колонке вверх.
Размер Размер двумерного списка  может быть любым.
Input:  [[1,1,1,0,0],[0,0,0,1,0],[1,1,0,0,1],[0,0,0,1,0]]
Output: [[1,1,1,1,1],[1,1,0,1,0],[0,0,0,0,0],[0,0,0,0,0]]
"""
import json
grid = json.loads(input())

def gravity_switch(grid: list):
    trans = [sorted(list(el), reverse=True) for el in zip(*grid)]
    return list(zip(*trans))

result = gravity_switch(grid)
print(json.dumps(result, separators=(',', ':')))


# Task 11
"""
https://stepik.org/lesson/957417/step/11?unit=963850
Прижать "1" в каждой строке влево.
Размер Размер двумерного списка  может быть любым.
Input:  [[1,1,1,0,0],[0,0,0,1,0],[1,1,0,0,1],[0,0,0,1,0]]
Output: [[1,1,1,0,0],[1,0,0,0,0],[1,1,1,0,0],[1,0,0,0,0]]
"""
import json
grid = json.loads(input())

def gravity_switch(grid: list):
    return [sorted(list(el), reverse=True) for el in grid]

result = gravity_switch(grid)
print(json.dumps(result, separators=(',', ':')))


# Task 12
"""
https://stepik.org/lesson/957417/step/12?unit=963850
Прижать "1" в каждой строке право.
Размер Размер двумерного списка  может быть любым.
Input:  [[1,1,1,0,0],[0,0,0,1,0],[1,1,0,0,1],[0,0,0,1,0]]
Output: [[0,0,1,1,1],[0,0,0,0,1],[0,0,1,1,1],[0,0,0,0,1]]
"""
import json
grid = json.loads(input())

def gravity_switch(grid: list):
    # return [sorted(list(el)) for el in grid]
    return list(map(sorted, grid))

result = gravity_switch(grid)
print(json.dumps(result, separators=(',', ':')))


# Task 13
"""
https://stepik.org/lesson/957417/step/13?unit=963850
Подсчитать "1" в каждом столбце.
Размер двумерного списка 6 х 3
Input:  [[0,0,0,1,0,0],[1,0,0,1,1,0],[1,1,1,1,1,1]]
Output: одноэтажных башен: 3, двухэтажных башен: 2, трехэтажных башен: 1
"""
import json
grid = json.loads(input())

def count_towers(grid: list):
    ls = [0 for _ in range(len(grid) + 1)]
    revers = zip(*grid)
    for el in revers:
        ls[sum(el)] += 1
    return f"одноэтажных башен: {ls[1]}, двухэтажных башен: {ls[2]}, трехэтажных башен: {ls[3]}"


# grid = [[0, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1]]
def count_towers(grid):
    revers = [sum(el) for el in zip(*grid)]  # [2, 1, 1, 3, 2, 1]
    ls = [revers.count(el) for el in range(len(grid) + 1)]  # [0, 3, 2, 1]
    return f"одноэтажных башен: {ls[1]}, двухэтажных башен: {ls[2]}, трехэтажных башен: {ls[3]}"


result = count_towers(grid)
print(result)

