#  09 Списки. Часть 1
""""""

# Task 01
"""
data - список целых чисел.
Определить, все ли числа в списке data четные
Input:  [2, 4, 6, 8, 10]
Output: True
"""
import json
data = json.loads(input())

def all_even(data):
    # return all(not el % 2 for el in data)
    return all(map(lambda el: el % 2 == 0, data))

def all_even(data):
    for el in data:
        if el % 2 != 0:
            return False
    return True

result = all_even(data)
# print(result)


# Task 02
"""
data - список целых чисел.
Определить, все ли числа в списке data нечетные
Input:  [1, 3, 5]
Output: True
"""
import json
data = json.loads(input())

def all_odd(data):
    # return all(el % 2 for el in data)
    return all(map(lambda el: el % 2 != 0, data))

def all_odd(data):
    for el in data:
        if el % 2 == 0:
            return False
    return True

result = all_odd(data)
# print(result)


# Task 03
"""
Определить, все ли числа в списке data больше num
Input:  10 | [20, 30]
Output: True
"""
import json
num, data = map(str.strip, input().split(" | "))
data = json.loads(data)
num = int(num)

def all_greater(data):
    # return all(el > num for el in data)
    return all(map(lambda el: el > num, data))

result = all_greater(data)
# print(result)


# Task 04
"""
Определить, все ли числа в списке data меньше num
Input:  10 | [2, 3]
Output: True
"""
import json
num, data = map(str.strip, input().split(" | "))
data = json.loads(data)
num = int(num)

def all_less(data):
    return all(el < num for el in data)
    # return all(map(lambda el: el < num, data))

result = all_greater(data)
# print(result)


# Task 05
"""
Обратить порядок следования элементов списка data и записать результат через запятую.
Input:  ["Макс", "Дастин", "Майк", "Стив", "Билли"]
Output: Билли, Стив, Майк, Дастин, Макс
"""
import json
data = json.loads(input())

def reversed_data(data: list):
    data.reverse()
    return ", ".join(data)

result = reversed_data(data)
# print(result)


# Task 06
"""
Обратить порядок следования элементов списка data в порядке возрастания, и записать результат через запятую.
Input:  ["Макс", "Дастин", "Майк", "Стив", "Билли"]
Output: Билли, Дастин, Майк, Макс, Стив
"""
import json
data = json.loads(input())

def sorted_asc_data(data: list):
    data.sort()
    return ", ".join(data)

result = sorted_asc_data(data)
# print(result)



# Task 07
"""
Обратить порядок следования элементов списка data в порядке убывания, и записать результат через запятую.
Input:  ["Макс", "Дастин", "Майк", "Стив", "Билли"]
Output: Стив, Макс, Майк, Дастин, Билли
"""
import json
data = json.loads(input())

def sorted_desc_data(data: list):
    data.sort(reverse=True)
    return ", ".join(data)

result = sorted_desc_data(data)
# print(result)


# Task 08
"""
Сортировать числовые элементы списка data в порядке возрастания,
 и записывать результат через запятую в переменную
Input:  [1, 3, 2, 4, 5]
Output: 1, 2, 3, 4, 5
"""
import json
data = json.loads(input())

def sorted_asc_data(data: list):
    data.sort()
    return ", ".join(map(str, data))

result = sorted_asc_data(data)
# print(result)


# Task 09
"""
Сортровать числовые элементы списка data в порядке убывания и записать результат через запятую
Input:  [1, 3, 2, 4, 5]
Output: 5, 4, 3, 2, 1
"""
import json
data = json.loads(input())

def sorted_desc_data(data: list):
    data.sort(reverse=True)
    return ", ".join(map(str, data))

result = sorted_desc_data(data)
# print(result)


# Task 10
"""
Сортровать числовые элементы списка data в порядке возрастания и отсеять дубликаты
Записать результат через запятую
Input:  [1, 1, 3, 2, 4, 5, 2, 3]
Output: 1, 2, 3, 4, 5
"""
import json
data = json.loads(input())

def sort_and_filter_unique(data: list):
    data = list(set(data))
    data.sort()
    return ", ".join(map(str, data))

result = sort_and_filter_unique(data)
# print(result)


# Task 11
"""
Сортровать строковые элементы списка data в порядке возрастания и отсеять дубликаты
Записать результат через запятую
Input:  ["action", "adventure", "strategy", "simulation", "sports", "racing", "puzzle", "simulation", "sports"]
Output: action, adventure, puzzle, racing, simulation, sports
"""
import json
tags = json.loads(input())

def sort_and_filter_unique(tags: list):
    tags = list(set(tags))
    tags.sort()
    return ", ".join(map(str, tags))

result = sort_and_filter_unique(tags)
# print(result)


# Task 11
"""
Подсчитать количество тегов в списке tags.
Записать результат через запятую.
Input:  ["action", "adventure", "strategy", "simulation", "sports", "racing", "puzzle", "strategy", "simulation", "sports"]
Output: action: 1, adventure: 1, strategy: 2, simulation: 2, sports: 2, racing: 1, puzzle: 1
"""
import json
tags = json.loads(input())

def get_tag_counts(tags: list):
    d = dict()
    for el in tags:
        d.setdefault(el, 0)
        d[el] += 1
    res = [f'{k}: {v}' for k, v in d.items()]
    return ', '.join(res)

def get_tag_counts(tags: list):
    res = dict.fromkeys([f'{el}: {tags.count(el)}' for el in tags])
    return ', '.join(res) # передаются только ключи

result = get_tag_counts(tags)
# print(result)


# Task 12
"""
Подсчитать количество элементов в списке data  (+ во всех вложенных списках)
Input:  [1, [2], [3, 4, [5, 6, [7, 8, [9, 10]]]]]
Output: 10
"""
import json
data = json.loads(input())

def count_elements(data: list):
    cnt = 0
    for el in data:
        if isinstance(el, list):
            cnt += count_elements(el)  # рекурсия
        else:
            cnt += 1
    return cnt

result = count_elements(data)
# print(result)


# Task 13
"""
Подсчитать количество вложенных списков в списке data
Input:  [1, [2, 3], 3, [4, [5]]]
Output: 3
"""
import json
data = json.loads(input())

def count_lists(data: list):
    cnt = 0
    for el in data:
        if isinstance(el, list):
            cnt += count_lists(el) + 1
    return cnt

# Просто считаем одинаковые скобки )))
def count_lists(data):
    s = str(data)
    return s.count('[') - 1

result = count_lists(data)
# print(result)


# Task 14
"""
Напишите код, который находит индекс игрока по имени Майк и записывает результат в переменную result.
Input:  [{"name":"Макс","x":100,"y":50},{"name":"Дастин","x":200,"y":100},{"name":"Стив","x":300,"y":150},
        {"name":"Билли","x":300,"y":170},{"name":"Майк","x":300,"y":170},{"name":"Лукас","x":200,"y":170}]
Output: 4
"""
import json
players = json.loads(input())

def find_index_by_name(players):
    for el in players:
        if el["name"] == "Майк":
            return players.index(el)

result = find_index_by_name(players)
# print(result)

# Вариант через методы строки
result = str(players)[:str(players).index('Майк')].count('}')
# print(result)


# Task 15
"""
Напишите код, который находит только те корабли у которых активированы щиты и 
записывает названия кораблей через запятую в переменную result.
Input:  [{"uss_enterprise":{"name":"USS Enterprise","shields":false,"weapons":true,"engine_power":90},
        "millennium_falcon":{"name":"Millennium Falcon","shields":true,"weapons":true,"engine_power":100},
        "ikar":{"name":"Ikar","shields":false,"weapons":true,"engine_power":70},
        "dedalus":{"name":"Dedalus","shields":true,"weapons":true,"engine_power":70}}]
Output: Millennium Falcon, Dedalus
"""
import json
starships = json.loads(input())

def get_names_of_ships_with_shields_enabled(starships):
    ls = list()
    for d in starships:
        ls.extend([el["name"] for el in d.values() if el["shields"]])
        # for el in d.values():
        #     if el["shields"]:
        #         ls.append(el["name"])
    return ', '.join(ls)

result = get_names_of_ships_with_shields_enabled(starships)
#  print(result)


