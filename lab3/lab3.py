"""
Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом), распознает, преобразует и выводит на экран объекты по определенному правилу. Объекты разделены пробелами.
Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Регулярные выражения использовать нельзя.

Вариант 6:

Целые нечетные числа. Замена: первая цифра каждого четного числа на нечетном месте на английскую цифру прописью.

"""

# Словарь для преобразования цифр в английские слова
digit_to_word = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}

# Функция для замены первой цифры на нечётной позиции на английское слово
def replace_digit_with_word(number):
    number_str = str(number)
    is_negative = number_str[0] == '-'  # Проверяем, является ли число отрицательным
    number_str = number_str.lstrip('-')  # Убираем знак минуса для обработки цифр

    # Если число чётное, заменяем первую цифру на нечётной позиции
    if int(number_str) % 2 == 0:
        new_number = ""
        for i, digit in enumerate(number_str):
            if i % 2 == 0:  # нечётная позиция (по индексу)
                new_number += digit_to_word[digit]  # заменяем цифру на слово
            else:
                new_number += digit  # оставляем цифру как есть
        return '-' + new_number if is_negative else new_number
    return '-' + number_str if is_negative else number_str  # для нечётных чисел возвращаем оригинал

# Функция для проверки, является ли строка числом (с учётом отрицательных чисел)
def is_number(s):
    if s.startswith('-'):
        return s[1:].isdigit()  # проверяем, что символы после минуса являются цифрами
    return s.isdigit()

# Функция для обработки последовательности из файла
def process_sequence_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:  # читаем файл построчно
            numbers = line.split()  # разделяем строку на числа или слова
            for number in numbers:
                if is_number(number):  # проверяем, что это действительно число
                    if int(number) % 2 != 0:
                        print(number)  # выводим нечётные числа как есть
                    else:
                        print(replace_digit_with_word(number))  # для чётных чисел заменяем первую цифру
                else:
                    print(f"Not a number: {number}")  # если это не число, выводим сообщение

# Пример использования программы
file_path = 'input.txt'  # путь к файлу с данными
process_sequence_from_file(file_path)

