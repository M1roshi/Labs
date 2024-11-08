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
    
    # Используем регулярное выражение для нахождения всех чисел
    numbers = re.findall(r'\b\d+\b', content)
    
    transformed_numbers = []
    for i, num in enumerate(numbers):
        # Проверяем, является ли число нечетным
        if int(num) % 2 != 0:
            transformed_numbers.append(num)
        else:
            # Четное число на нечетной позиции: заменяем первую цифру на английскую пропись
            if (i + 1) % 2 != 0:  # нечетная позиция (начиная с 1)
                first_digit_english = digit_to_english(num[0])
                transformed_num = first_digit_english + num[1:]
                transformed_numbers.append(transformed_num)
            else:
                transformed_numbers.append(num)  # четное число на четной позиции оставляем как есть
    
    # Выводим преобразованные числа
    print(" ".join(transformed_numbers))

# Пример вызова функции
process_file('input.txt')
