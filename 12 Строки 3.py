#  12 Строки 3
""""""

# Task 01
"""
Конвертировать значение строки message из (#1) в (#2) и записать результат в переменную result.
(#1) - tagname.class1.class2.classN
(#2) - <tagname class="class1 class2 classN"></tagname>
Input:  a.btn.btn-primary
Output: <a class="btn btn-primary"></a>
"""
message = input().strip()

tag = message.split('.')
result = f'<{tag[0]} class="{" ".join(tag[1:])}"></{tag[0]}>'
# result = f'<{tag[0]} class="{" ".join(el for el in tag[1:])}"></{tag[0]}>'

# print(result)


# Task 02
"""
Конвертировать значение строки message из (#1) в (#2).
(#1) - tagname>tagname>tagname
(#2) - <tagname><tagname><tagname></tagname></tagname></tagname>
Input:  p>p>div
Output: <p><p><div></div></p></p>
"""
message = input().strip()

tag = message.split('>')
result = ''.join(f'<{el}>' for el in tag) + ''.join(f'</{el}>' for el in tag[::-1])

# print(result)


# Task 03
"""
Конвертировать значение строки message из (#1) в (#2).
(#1) - tagname>tagname>tagname{Привет, Мир!}
(#2) - <tagname><tagname><tagname>Привет, Мир!</tagname></tagname></tagname>
Input:  p>p>div{Привет, Лия!}
Output: <p><p><div>Привет, Лия!</div></p></p>
"""
message = input().strip()
sep = message.split('{')
val = sep[1][:-1]
tag = sep[0].split('>')
result = ''.join(f'<{el}>' for el in tag) + val + ''.join(f'</{el}>' for el in tag[::-1])

# print(result)


# Task 04
"""
Конвертировать значение строки message из kebab-case в lowerCamelCase.
Input:  the-nina-project
Output: theNinaProject
"""
message = input().strip()

def kebab_to_lower_camel(message: str):
    st = message.split('-')
    return st[0] + ''.join(map(str.title, st[1:]))
    # return st[0] + ''.join(map(str.capitalize, st[1:]))


# Вариант
def kebab_to_lower_camel_1(message: str):
    st = message.split('-')
    return message[0] + ''.join(el.title() for el in st)[1:]
    # return message[0] + ''.join(el.capitalize() for el in st)[1:]

result = kebab_to_lower_camel(message)
print(result)


# Регулярные выражения
import re
message = input().strip()

def kebab_to_lower_camel_2(message):
    return re.sub(r'-\w', lambda x: x[0][1].upper(), message)

result = kebab_to_lower_camel_2(message)
print(result)


# Task 05
"""
Конвертировать значение строки message из kebab-case в UpperCamelCase.
Input:  the-nina-project
Output: TheNinaProject
"""
message = input().strip()

def kebab_to_upper_camel(message):
    st = message.split('-')
    return ''.join(map(str.title, st))
    # return ''.join(map(str.capitalize, st))

# Регулярные выражения
import re
def kebab_to_upper_camel(message):
    return re.sub(r'-\w|^\w', lambda x: x[0][-1].upper(), message)


result = kebab_to_upper_camel(message)
# print(result)


# Task 06
"""
Конвертировать значение строки message из UpperCamelCase в snake_case.
Input:  TheNinaProject
Output: the_nina_project
"""
message = input().strip()

def upper_camel_to_snake(message: str):
    st = ''.join('_' + el.lower() if el.isupper() else el for el in message)
    return st.lstrip('_')

def upper_camel_to_snake(message: str):
    st = ''
    for el in message:
        if el.isupper():
            st += '_' + el.lower()
        else:
            st += el
    return st[1:]


# Регулярные выражения
import re
def upper_camel_to_snake(message):
    pattern = r'([A-Z])|(\d+)'
    return re.sub(pattern, r'_\1\2', message).lower().lstrip('_')


def upper_camel_to_snake(message):
    pattern = r'([a-z])([A-Z])'
    return re.sub(pattern, r'\1_\2', message).lower()

def upper_camel_to_snake(message):
    return re.sub(r'[A-Z]', lambda x: '_' + x[0].lower(), message)[1:]


result = upper_camel_to_snake(message)
print(result)


# Task 07
"""
Конвертировать значение строки message в соответствии к какому паттерну относится значение строки message.
Строка может подходить под пять паттернов:
    kebab-case          aaa-bbb-ccc
    snake_case          aaa_bbb_ccc
    lowerCamelCase      aaaBbbCcc
    UpperCamelCase      AaaBbbCcc
    unknown             Aaa Bbb Ccc
Input:  the-monster-and-the-superhero
Output: kebab-case
"""
message = 'AaaBbb2Ccc'
# message = input().strip()

def detect_case(message: str):
    if '-' in message:
        return 'kebab-case'
    if '_' in message:
        return 'snake_case'
    if message.isalnum():
        if message[0].islower():
            return 'lowerCamelCase'
        elif message[0].isupper():
            return 'UpperCamelCase'
    return 'unknown'

# Регулярные выражения
def detect_case(message: str):
    if re.fullmatch(r"(?:[a-z]+(?:-[a-z]+)+)", message):
        return "kebab-case"
    elif re.fullmatch(r"(?:[a-z]+(?:_[a-z]+)+)", message):
        return "snake_case"
    elif re.fullmatch(r"(?:[a-z]+(?:[A-Z][a-z]+)+)", message):
        return "lowerCamelCase"
    elif re.fullmatch(r"(?:[A-Z][a-z]+)+", message):
        return "UpperCamelCase"
    else:
        return "unknown"

result = detect_case(message)
# print(result)


# Task 08
"""
Подсчитать количество слов в строке message, 
которые начинаются и заканчиваются с одинаковой буквы (регистр неважен)
Input:  Привет Анна
Output: 1
"""
message = input().strip()

def count_words(message):
    return sum(el[0] == el[-1] for el in message.lower().split())
    # return sum(map(lambda x: x[0] == x[-1], message.lower().split()))

result = count_words(message)
# print(result)


# Task 09
"""
Найти длину самого короткого слова в строке.
Input:  May the Force be with you
Output: 2
"""
message = input().strip()

def find_shortest_word_length(message):
    return min(len(el) for el in message.split())
    # return min(map(len, message.split()))
    # return len(min(message.split(), key=len))

result = find_shortest_word_length(message)
# print(result)


# Task 10
"""
Найти длину самого длинного слова в строке.
Input:  May the Force be with you
Output: 5
"""
message = input().strip()

def find_longest_word_length(message):
    return max(map(len, message.split()))

result = find_longest_word_length(message)
# print(result)


# Task 11
"""
Удалить из строки символы # @ $ % 
Input:  Hello#World@$%
Output: HelloWorld
"""
message = input().strip()

def clean_message(message):
    res = [el for el in list(message) if el not in '#@$%']
    return ''.join(res)

# Регулярные выражения
import re
def clean_message(message):
    return re.sub(r"[@#$%]", "", message)

result = clean_message(message)
print(result)


# Task 12
"""
Удалить из строки каждый третий символ
Input:  Пользователь
Output: Поьзваел
"""
message = input().strip()

def new_message(message):
    return ''.join(el for i, el in enumerate('_' + message) if i % 3 != 0)

# del  - метод списка
def new_message(message):
    message = list(message)
    del message[2::3]
    return ''.join(message)

result = new_message(message)
# print(result)


# Task 13
"""
words - список слов.
Создать новый список букв из списка слов words
Input:  ["apple", "banana", "cherry"]
Output: ["a","p","p","l","e","b","a","n","a","n","a","c","h","e","r","r","y"]
"""
import json
words = json.loads(input())

def split_words(words):
    return list(''.join(words))

def split_words(words):
    res = []
    for el in words:
        res.extend(list(el))
    return res

result = split_words(words)
print(json.dumps(result, separators=(',', ':'), ensure_ascii=False))


# Task 14
"""
words - список слов.
Создать новый список центральных букв нечетных слов из списка слов words.
Нечетное слово это слово у которого количество букв нечетное.
Input:  ["apple", "banana", "apple"]
Output: ["p","p"]
"""
import json
words = json.loads(input())

def get_central_letters(words: list):
    # ls = [el for el in words if len(el) % 2 != 0]
    # res = [el[len(el) // 2] for el in ls]
    res = [el[len(el) // 2] for el in words if len(el) % 2 != 0]
    return res

result = get_central_letters(words)
print(json.dumps(result, separators=(',', ':'), ensure_ascii=False))



# Task 15
"""
words - список слов.
Создать новый список крайних (первая, последняя) букв слов из списка слов words.
Input:  ["apple", "banana", "cherry"]
Output: ["a","e","b","a","c","y"]
"""
import json
words = json.loads(input())

def get_first_and_last_letters(words: list):
    res = ''.join(el[0] + el[-1] for el in words)
    return list(res)

def get_first_and_last_letters(words: list):
    res = []
    for el in words:
        res.extend([el[0], el[-1]])
    return res

# Нестандартное использование sum(). По сути делает тоже что написано выше.
def get_first_and_last_letters(words):
    return sum([[el[0], el[-1]] for el in words], [])


result = get_first_and_last_letters(words)
print(json.dumps(result, separators=(',', ':'), ensure_ascii=False))


# Task 16
"""
Маскировать все символы в строке  message символом # за исключением 4 последних символов 
Input:  TheNinaProject
Output: ##########ject
"""
words = input()

def mask(words):
    st = '#' * (len(words) - 4)
    return st + words[-4:]

result = mask(words)
print(result)

