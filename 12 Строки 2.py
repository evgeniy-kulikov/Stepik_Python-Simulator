#  12 Строки 2
""""""

# Task 01
"""
Увеличить значение переменной message  на значение page
Input:  8 | page-42
Output: page-50
"""
page, message = map(str.strip, input().split(" | "))
page = int(page)

p_new = int(message.split("-")[1]) + page
result = f"page-{p_new}"
# print(result)


# Task 02
"""
Увеличить значение переменной message  на значение uri_id
Input:  2 | api/entires/fetch/10/body
Output: api/entires/fetch/12/body
"""
uri_id, message = map(str.strip, input().split(" | "))
uri_id = int(uri_id)

id_new = int(message.split("/")[-2]) + uri_id
result = f"api/entires/fetch/{id_new}/body"
# print(result)


# Task 03
"""
Проверить, является ли строка палиндромом.
Input:  анна
Output: True
"""
message = input().strip().lower()

def is_palindrome(message):
    # part = int(len(message) / 2)
    # return message[:1 - part] == message[part:][::-1]
    return message == message[::-1]

result = is_palindrome(message)
# print(result)


# Task 04
"""
Если количество слово в предложении больше значению words_count, тогда
обрезать предложение до определенного количества слов, и в конце поставить "..."
Если количество слово в предложении меньше или равно значению words_count, тогда строку не меняем.
Input:  9 | Каждый проступок, как и каждое доброе дело, рождают новое будущее.
Output: Каждый проступок, как и каждое доброе дело, рождают новое...
"""
words_count, message = map(str.strip, input().split(" | "))
words_count = int(words_count)

st = message.split(' ')

if len(st) > words_count:
    result = ' '.join(st[:words_count]) + '...'
else:
    result = message

# result = [message, " ".join(st[:words_count]) + "..."][len(st) > words_count]

# print(result)


# Task 05
"""
Проверить: есть ли повторяющиеся подряд буквы в слове
Input:  Анна
Output: True
"""
message = input().strip()

result = False
for i in range(1, len(message)):
    if message[i - 1] == message[i]:
        result = True
        break

# короче
result = any(message[i - 1] == message[i] for i in range(1, len(message)))
# print(result)


# Task 06
"""
Выбрать все строчные буквы в переменной message
Input:  ПрИВет
Output: р, е, т
"""
message = input().strip()

result = ', '.join(el for el in message if el.islower())
# короче
# result = ', '.join(filter(str.islower, message))

# print(result)


# Task 07
"""
Выбрать все заглавные буквы в переменной message
Input:  ПРиВеТ
Output: П, Р, В, Т
"""
message = input().strip()

result = ', '.join(filter(str.isupper, message))
# result = ', '.join(el for el in message if el.isupper())
# print(result)


# Task 08
"""
Подсчитать количество символов # в строке message
Input:  ###1111###01###
Output: 9
"""
message = input().strip()

result = message.count('#')
# print(result)


# Task 09
"""
Подсчитать количество  букв внутри [] и вывести результат через запятую 
Input:  [Лия][Парфенова][]
Output: 3, 9, 0
"""
message = input().strip()

def letters_count(message):
    result = message[1:-1].split('][')
    return ', '.join(str(len(el)) for el in result)

result = letters_count(message)
# print(result)


# Task 10
"""
Найти первую повторяющуюся букву в переменной "message" и записать результат в переменную "result". 
Если повторяющихся букв нет, тогда записываем пустую строку. Тесты чувствительны к регистру.
Input:  Практика
Output: а
"""
message = input().strip()

def find_first_repeating_char(message):
    for el in message.lower():
        if message.count(el) > 1:
            return el
    return ''

result = find_first_repeating_char(message)
# print(result)


# Task 11
"""
Проверить, нет ли в строке слов дубликатов и записать логический результат в переменную result.
Тесты чувствительны к регистру.
Input:  лия Лия Привет
Output: True
"""
message = input().strip()

def has_duplicate_words(message):
    ls = message.lower().split()
    for el in ls:
        if ls.count(el) > 1:
            return True
    return False

def has_duplicate_words(message):
    ls = message.lower().split()
    return len(ls) != len(set(ls))

result = has_duplicate_words(message)
# print(result)


# Task 12
"""
Разбить слово на части, размер которых указан в переменной cases 
и возвратить части слова разделенные запятыми в переменную result.
Если слово не может быть разбито на две равные части, 
тогда записываем сообщением "Слово не может быть равномерно разделено." в переменную result.  
Input:  2 | Привет
Output: При, вет
"""
cases, message = map(str.strip, input().split(" | "))
cases = int(cases)
# message = 'Привет'
# cases = 2

def split_string_into_cases(message, cases):
    if len(message) % cases:
        return "Слово не может быть равномерно разделено."
    else:
        part = len(message) // cases
        return ', '.join(message[n:n + part] for n in range(0, len(message), part))

# from textwrap import wrap as part
# def split_string_into_cases(message, cases):
#     if cases == 1:
#         return message
#     else:
#         if not len(message) % cases:
#             return ', '.join(part(message, len(message) // cases))
#         return "Слово не может быть равномерно разделено."

result = split_string_into_cases(message, cases)
# print(result)


# Task 13
"""
Удалить все гласные буквы из переменной message 
Input:  Привет
Output: Првт
"""
message = input().strip()
vowels = 'ауоыэяюёиеАУОЫЭЯЮЁИЕ'

result = ''.join(el for el in message if el not in vowels)
# print(result)


# Task 14
"""
Изменить порядок букв в каждом слове переменной message на обратный
Input:  Входные пользовательские данные
Output: еындохВ еиксьлетавозьлоп еыннад
"""
message = input().strip()

result = ' '.join(el[::-1] for el in message.split())
# result = ' '.join(map(lambda el: el[::-1], message.split()))
# print(result)


# Task 15
"""
Изменить порядок букв в каждом слове переменной message 
на отсортированный в алфавитном порядке по возрастанию 
Input:  Самый полный курс для начинающих программистов
Output: Саймы йлнопы крсу для ааииннхчщю авгиммоопррст
"""
message = input().strip()

result = ' '.join(''.join(sorted(el)) for el in message.split())
# result = ' '.join(map(lambda el: ''.join(sorted(el)), message.split()))
# print(result)


# Task 16
"""
Переменные message1, message2, содержат входные данные.
Проверить является ли значение перменной message2 обращенным (reverse) значению перменной message1 
и записать логический результат в переменную result
Input:  Привет | тевирП
Output: True
"""
message1, message2 = map(str.strip, input().split(" | "))
def is_rotation(message1, message2):
    return message1 == message2[::-1]
    # return message1 == ''.join(reversed(message2))

result = is_rotation(message1, message2)
# print(result)
