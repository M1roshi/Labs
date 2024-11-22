"""
Написать программу, которая читая символы из файла, распознает, преобразует и выводит на экран объекты по определенному правилу. 
Объекты разделены пробелами. Распознавание и преобразование делать по возможности через регулярные выражения. 
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.

Вариант 6.
Целые нечетные числа. Замена: первая цифра каждого четного числа на нечетном месте на английскую цифру прописью.
"""

import re

# Словарь для преобразования цифры в слово на английском
digit_to_word = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

def process_numbers(file_path):
    try:
        # Читаем содержимое файла
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Разделяем содержимое на объекты через пробел
        objects = content.split()
        
        # Функция для проверки и преобразования чисел
        def transform_number(number, index):
            if not re.fullmatch(r'-?\d+', number):  # Пропуск, если это не целое число
                return number
            
            num = int(number)  # Преобразуем в число
            
            # Проверяем, что число четное и стоит на нечетной позиции
            if num % 2 == 0 and index % 2 == 0:  # Индексация с нуля, 0, 2, 4 - нечетные позиции
                if number[0] == '-':  # Если число отрицательное, работаем со второй цифрой
                    return '-' + digit_to_word[number[1]] + number[2:]
                else:
                    return digit_to_word[number[0]] + number[1:]
            else:
                return number  # Остальные числа остаются без изменений
        
        # Преобразуем все числа в списке
        transformed_objects = [
            transform_number(obj, i) for i, obj in enumerate(objects)
        ]
        
        # Выводим результат
        result = ' '.join(transformed_objects)
        print("Результат преобразования:")
        print(result)
    
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Указываем путь к файлу
file_path = "input.txt"
process_numbers(file_path)



