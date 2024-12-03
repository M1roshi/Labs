"""
Написать программу, которая читая символы из файла, распознает, преобразует и выводит на экран объекты по определенному правилу. 
Объекты разделены пробелами. Распознавание и преобразование делать по возможности через регулярные выражения. 
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.

Вариант 6.
Целые нечетные числа. Замена: первая цифра каждого четного числа на нечетном месте на английскую цифру прописью.
"""

import re

# Функция для преобразования цифр в английские слова
def digit_to_word(digit):
    words = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    return words.get(digit, digit)

# Функция обработки чисел по условию
def process_numbers(numbers):
    processed = []
    for index, number in enumerate(numbers):
        if index % 2 == 0:  # нечетная позиция (начиная с 0)
            if re.match(r'.*[02468]$', number):  # Четное число
                # Заменяем первую цифру на текстовое представление
                processed.append(digit_to_word(number[0]) + number[1:])
            else:
                processed.append(number)
        else:
            processed.append(number)
    return processed

# Чтение данных из файла
input_file = "input.txt"  # Укажите путь к файлу
with open(input_file, 'r') as file:
    content = file.read()

# Распознаем числа с помощью регулярного выражения
numbers = re.findall(r'\b-?\d+\b', content)

# Обрабатываем числа
result = process_numbers(numbers)

# Выводим результат
print(" ".join(result))





