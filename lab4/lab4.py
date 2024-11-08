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

# Регулярные выражения для различных категорий чисел
positive_even_pattern = re.compile(r'^\d*[02468]$')
positive_odd_pattern = re.compile(r'^\d*[13579]$')
negative_even_pattern = re.compile(r'^-\d*[02468]$')
negative_odd_pattern = re.compile(r'^-\d*[13579]$')

# Основная функция для обработки файла
def process_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    transformed_lines = []
    for line in lines:
        # Разбиваем строку на объекты, разделенные пробелами
        objects = line.split()
        
        transformed_objects = []
        for i, obj in enumerate(objects):
            transformed_obj = obj  # Изначально объект остается без изменений
            
            # Проверка условий с помощью регулярных выражений
            if positive_even_pattern.fullmatch(obj) or negative_even_pattern.fullmatch(obj):
                # Четное число
                is_odd_position = (i + 1) % 2 != 0  # Проверка на нечетную позицию (нумерация от 1)
                
                if is_odd_position:
                    # Четное число на нечетной позиции: заменяем первую цифру на английское слово
                    first_char = obj[1] if obj.startswith('-') else obj[0]
                    first_digit_english = digit_to_english(first_char)
                    # Формируем новое число с замененной первой цифрой
                    if obj.startswith('-'):
                        transformed_obj = '-' + first_digit_english + obj[2:]
                    else:
                        transformed_obj = first_digit_english + obj[1:]
            
            # Добавляем обработанный объект
            transformed_objects.append(transformed_obj)
        
        # Добавляем преобразованную строку в список строк
        transformed_lines.append(" ".join(transformed_objects))
    
    # Выводим результат, сохраняя многострочную структуру
    print("\n".join(transformed_lines))

# Пример вызова функции
if __name__ == "__main__":
    process_file('input.txt')


