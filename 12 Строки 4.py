#  12 Строки 4
""""""

# Task 01
"""
Разобрать строку message на буквы и между каждой буквы проставляет пробелы.
*   Если в строке message есть хотя бы одна буква в верхнем регистре (заглавная), 
    тогда все буквы переводим в верхний регистр, иначе оставляем строку в текущем регистре.
*   Код должен работать как с кириллицей так и с латиницей.
*   Кириллица и латиница может встречаться в одной строке
Input:  TheNinaProject
Output: T H E N I N A P R O J E C T
"""
message = input().strip()

def update_message(message: str):
    if message.lower() == message:
        return ' '.join(message)
    return ' '.join(message.upper())

# Регулярные выражения
import re
def update_message(message):
    if re.search(r'[A-ZА-ЯЁ]', message):
        return ' '.join(message.upper())
    return ' '.join(message)

# длинный вариант
def update_message(message: str):
    flag = False
    for el in message:
        if el.isupper():
            flag = True
            break
    if flag:
        return ' '.join(message.upper())
    return ' '.join(message)

result = update_message(message)
# print(result)


# Task 02
"""
Переместить все заглавные буквы (в том порядке, в котором они были найдены) в начало слова.
Input:  TheNinaProject
Output: TNPheinaroject
"""
message = input().strip()

def update_message(message: str):
    up = ''.join(el for el in message if el.isupper())
    low = ''.join(el for el in message if el.islower() or el.isnumeric())
    return up + low


# Регулярные выражения
import re
def update_message(message):
    upper = re.findall(r'[A-ZА-Я]', message)
    lower = re.findall(r'[a-zа-я0-9]', message)
    return ''.join(upper + lower)

result = update_message(message)
# print(result)


# Task 03
"""
Переместить все заглавные буквы (отсортированные в порядке возрастания) в начало слова.
Input:  TheNinaProject
Output: NPTheinaroject
"""
message = input().strip()

def update_message(message: str):
    up = ''.join(sorted(el for el in message if el.isupper()))
    low = ''.join(el for el in message if el.islower() or el.isnumeric())
    return up + low


# Регулярные выражения
import re
def update_message(message):
    upper = re.findall(r'[A-ZА-Я]', message)
    lower = re.findall(r'[a-zа-я0-9]', message)
    return ''.join(sorted(upper) + lower)

result = update_message(message)
# print(result)


# Task 04
"""
Первая буква каждого слова в строке должна быть заглавной, а остальная часть каждого слова — строчной.
Input:  HELLo worLD 5
Output: Hello World 5
"""
message = input().strip()

def update_message(message: str):
    return ' '.join(el.capitalize() for el in message.split())

result = update_message(message)
# print(result)


# Task 05
"""
Найти номера символов, совпадающих с последним символом строки message.
    * Учитывайте регистр A != a
    * Индекс последнего символа выводить ненужно.
Input:  Привет мирный Мир
Output: Соответствующие индексы: 1, 9
"""
message = input().strip()

def show_matching_idx(message: str):
    s = message[-1]
    res = ', '.join(str(i) for i, el in enumerate(message[:-1]) if el == s)
    return f'Соответствующие индексы: {res if res else "нет"}'

result = show_matching_idx(message)
# print(result)


# Task 06
"""
https://stepik.org/lesson/982468/step/6?unit=989736
Найти общее количество символов + и - в строке message. 
А так же сколько таких символов, после которых следует цифра 0
Input:  Hello+World-+-0-
Output: Общее количество символов: 5, Количество символов, после которых следует цифра ноль: 1
"""
message = input().strip()

def stats(message: str):
    symbol = message.count('+') + message.count('-')
    zero = message.count('+0') + message.count('-0')
    return f"Общее количество символов: {symbol}, Количество символов, после которых следует цифра ноль: {zero}"

def stats(message: str):
    symbol = sum(el in '+-' for el in message)
    zero = sum(el in '+-' for i, el in enumerate(message[:-1]) if message[i + 1] == '0')
    return f"Общее количество символов: {symbol}, Количество символов, после которых следует цифра ноль: {zero}"

# Регулярные выражения
import re
def stats(message):
    symbol = len(re.findall(r'[+-]', message))
    zero = len(re.findall(r'[+-]0', message))
    return f'Общее количество символов: {symbol}, Количество символов, после которых следует цифра ноль: {zero}'

result = stats(message)
# print(result)


# Task 07
"""
https://stepik.org/lesson/982468/step/7?unit=989736
Определить какой символ в строке message встречается раньше: "["  или  "]"
Если в строке message нет символов [ и ]  - выводится сообщение: В строке нет символов [ и ]
Если в строке message нет символа [   - выводится сообщение: В строке нет символа [
Если в строке message нет символа ]  - выводится сообщение: В строке нет символа ]
Если в строке message символ [ встречается раньше символа ]  - выводится сообщение:
Символ [ встречается раньше символа ]
Если в строке message символ ] встречается раньше символа [   - выводится сообщение:
Символ ] встречается раньше символа [
Input:  Всегда [делись тем, чему ты научился — Йода
Output: В строке нет символа ]
"""
message = input().strip()

def get_info(message: str):
    open = message.find('[')
    close = message.find(']')
    if open + close == -2:
        return 'В строке нет символов [ и ]'
    elif open * close < 0:
        return f"В строке нет символа {'[]'[open > close]}"
    return f"Символ {'[]'[open > close]} встречается раньше символа {']['[open > close]}"

# Простая версия
def get_info(message: str):
    open = message.find('[')
    close = message.find(']')
    if open + close == -2:
        return 'В строке нет символов [ и ]'
    elif open == -1:
        return 'В строке нет символа ['
    elif close == -1:
        return 'В строке нет символа ]'
    elif open < close:
        return 'Символ [ встречается раньше символа ]'
    return 'Символ ] встречается раньше символа ['

result = get_info(message)
# print(result)


# Task 08
"""
Удалить в строке message все буквы x за которыми следует abc (xxxabc -> xx)
abc не должно быть в итоговой строке.
Input:  xabcxxabcxx
Output: xxx
"""
message = input().strip()

def update_message(message: str):
    return message.replace('xabc', '').replace('abc', '')

result = update_message(message)
# print(result)



# Task 09
"""
Удалить в строке message все лишнее пробелы.
    * пробелы в начале и в конце строки .
    * пробелы которые идут более одного подряд.
Input:  Всегда  есть два, не  больше,   не меньше.   Мастер  и  ученик  —  Йода.
Output: Всегда есть два, не больше, не меньше. Мастер и ученик — Йода.
"""
message = input().strip()

def update_message(message: str):
    return ' '.join(message.split())

result = update_message(message)
# print(result)


# Task 10
"""
Найти наибольшее количество идущих подряд цифр в строке.
Input:  Lorem ipsum dolor sit 1234 amet, consectetur adipiscing 56789 elit.
Output: 5
"""
message = input().strip()

def get_digits_count(message):
    cnt, res = 0, 0
    for el in message:
        if el.isdigit():
            cnt += 1
        else:
            if cnt > res:
                res = cnt
            cnt = 0
    return res

def get_digits_count(message: str):
    cnt = 1
    res = []
    for i, el in enumerate(message[:-1]):
        if el.isdecimal() and message[i + 1].isdecimal():
            cnt += 1
        else:
            res.append(cnt)
            cnt = 1
    return max(res)


# Регулярные выражения
import re

def get_digits_count(message):
    return max(map(len, re.findall(r'([0-9]+)', message)))

result = get_digits_count(message)
# print(result)


# Task 11
"""
Найти сумму цифр в строке message.
Input:  Lorem ipsum dolor sit 123 amet, consectetur adipiscing 456 elit.
Output: 21
"""
message = input().strip()

def get_digits_count(message):
    cnt = 0
    for el in message:
        if el.isdigit():
            cnt += int(el)
    return cnt


# Регулярные выражения
import re
def get_digits_count(message):
    return sum(map(int, re.findall(r'\d', message)))

result = get_digits_count(message)
# print(result)


# Task 12
"""
Отсортировать строки в списке строк messages в зависимости от количества цифр в каждой строке.
    * Если строки в списке строк messages имеют одинаковое количество цифр, 
      тогда записываем их в том порядке в котором они были найдены.
    * В строке с цифрами, цифры всегда начинаются после знака _
Input:  ["Action", "Pagination_3", "Controller_24", "Arrows_451", "Elements_451"]
Output: Action, Pagination_3, Controller_24, Arrows_451, Elements_451
"""
import json
words = json.loads(input())

def custom_sort(words: list):
    w = [el for el in words if el.find('_') == -1]
    n = [el for el in words if el.find('_') > 0]
    n.sort(key=lambda el: len(el[el.index('_'):]))
    return ', '.join(w + n)

def custom_sort(words):
    res = sorted(words, key=lambda el: sum(s.isdigit() for s in el))
    return ', '.join(res)

# Регулярные выражения
import re
def custom_sort(words: list):
    return ', '.join(sorted(words, key=lambda el: len(re.findall(r"[0-9]", el))))

result = custom_sort(words)
# print(result)


# Task 13
"""
message1, message2 - принимают входные пользовательские данные.
Определить: содержится ли меньшая по длине строка в большей (с учетом регистра) и записать логический результат.
Input:  Hello World | World
Output: True
"""
message1, message2 = map(str.strip, input().split(" | "))

def is_substring_included(message1, message2):
    if len(message2) < len(message1):
        message1, message2 = message2, message1
    return message1 in message2

def is_substring_included(message1, message2):
    return message1 in message2 or message2 in message1

result = is_substring_included(message1, message2)
# print(result)


# Task 14
"""
Определить  индекс каждого символа в строке message 
и записать результат в переменную result в формате: symbol(index)
Input:  Hello
Output: H(0) e(1) l(2) l(3) o(4) 
"""
message = input().strip()

def get_idx(message: str):
    return ' '.join(f"{el}({i})" for i, el in enumerate(message))

def get_idx(message: str):
    res = ''
    for i, el in enumerate(message):
        res += f"{el}({i}) "
    return res.rstrip()

result = get_idx(message)
# print(result)


# Task 15
"""
Определить  индекс каждого символа в строке message 
и записать результат в переменную result в формате: symbol(index) * len(message)
Input:  Hello
Output: H(0) e(5) l(10) l(15) o(20)
"""
message = input().strip()

def get_idx(message: str):
    n = len(message)
    return ' '.join(f"{el}({i * n})" for i, el in enumerate(message))

result = get_idx(message)
# print(result)


# Task 16
"""
path - полный путь файла в unix формате. 
Найти расширение файла.
Input:  /Users/lia/hello-world/hello-world.js
Output: js
"""
path = input().strip()

def get_ext(path: str):
    return path[path.rindex('.') + 1:]
    # return path.split('.')[-1]

result = get_ext(path)
# print(result)