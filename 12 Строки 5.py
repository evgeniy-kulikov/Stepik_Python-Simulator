#  12 Строки 5
""""""

# Task 01
"""
path - полный путь файла в unix формате. 
Найти название файла (без расширения).
Input:  /Users/lia/hello-world/hello-world.js
Output: hello-world
"""
path = input().strip()

def get_filename(path: str):
    path = path.split('/')[-1]
    return path[:path.rindex('.')]

result = get_filename(path)
# print(result)


# Task 02
"""
Кодировать строку message с помощью азбуки Морзе
Input:  NINA PROJECT
Output: -. .. -. .-   .--. .-. --- .--- . -.-. -
"""
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' '
}
message = input().strip()

def encode(message: str):
    return ' '.join(MORSE_CODE[el] for el in message)

result = encode(message)
# print(result)



# Task 03
"""
Декодировать строку message с помощью азбуки Морзе
Input:  -. .. -. .-   .--. .-. --- .--- . -.-. -
Output: NINA PROJECT
"""
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' '
}
message = input().strip()

def decode(message: str):
    MORSE_DECODE = {v: k for k, v in MORSE_CODE.items()}
    message = message.replace(' ', '*').replace('***', '* *').split('*')
    return ''.join(MORSE_DECODE[el] for el in message)

result = decode(message)
# print(result)


# Task 04
"""
https://stepik.org/lesson/982532/step/4?unit=989800
Расстояние Хэмминга - это число позиций, в которых соответствующие символы двух строк одинаковой длины различны.
Обработать две строки и вычислить расстояние Хэмминга между ними. 
Если строки имеют разную длину тогда в переменную result записать -1.
Input:  message1, message2 = 'abc', 'ade'
Output: 2
"""
message1, message2 = map(str.strip, input().split(" | "))

def get_hamming(s1, s2):
    if len(s1) == len(s2):
        return sum(el[0] != el[1] for el in zip(message1, message2))
    return -1

result = get_hamming(message1, message2)
# print(result)
