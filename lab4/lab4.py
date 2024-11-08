"""
Написать программу, которая читая символы из файла, распознает, преобразует и выводит на экран объекты по определенному правилу. 
Объекты разделены пробелами. Распознавание и преобразование делать по возможности через регулярные выражения. 
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.

Вариант 6.
Целые нечетные числа. Замена: первая цифра каждого четного числа на нечетном месте на английскую цифру прописью.
"""

import re

# Функция для преобразования цифры в английское слово
def digit_to_english(digit):
    english_digits = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    return english_digits.get(digit, '')

# Основная функция для обработки файла
def process_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    # Используем регулярное выражение для нахождения всех чисел (включая отрицательные)
    numbers = re.findall(r'-?\b\d+\b', content)
    
    transformed_content = content  # Копия исходного текста для замены

    for i, num in enumerate(numbers):
        # Проверяем, является ли число нечетным
        if int(num) % 2 != 0:
            continue  # Нечетное число не изменяем
        else:
            # Четное число на нечетной позиции: заменяем первую цифру на английское слово
            if (i + 1) % 2 != 0:  # нечетная позиция (начиная с 1)
                # Определяем первую цифру, пропуская знак минус, если он есть
                first_digit_english = digit_to_english(num[1] if num[0] == '-' else num[0])
                transformed_num = (first_digit_english + num[2:]) if num[0] == '-' else (first_digit_english + num[1:])
                
                # Заменяем исходное число в тексте на преобразованное
                transformed_content = re.sub(r'\b' + re.escape(num) + r'\b', transformed_num, transformed_content, 1)
    
    # Выводим преобразованный текст
    print(transformed_content)

# Пример вызова функции
process_file('input.txt')

