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
        lines = file.readlines()
    
    # Шаблон: находим четные числа (положительные и отрицательные)
    pattern = re.compile(r'(?P<sign>-)?(?P<first_digit>[0-9])(?P<rest>\d*[02468])')

    def transform(match):
        # Преобразуем первую цифру в английское слово
        first_digit_word = digit_to_english(match.group('first_digit'))
        sign = match.group('sign') or ''  # Если нет знака, оставляем пустую строку
        rest = match.group('rest')
        return f"{sign}{first_digit_word}{rest}"

    # Преобразуем строки: только четные числа на нечетных позициях
    transformed_lines = []
    for line in lines:
        words = line.split()
        for i, word in enumerate(words):
            # Применяем замену только к четным числам на нечетных позициях
            if (i + 1) % 2 != 0:  # Нечетная позиция
                words[i] = pattern.sub(transform, word, count=1)
        transformed_lines.append(" ".join(words))
    
    # Выводим результат
    print("\n".join(transformed_lines))

# Пример вызова функции
if __name__ == "__main__":
    process_file('input.txt')



