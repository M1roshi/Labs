# Словарь для преобразования цифр в английские слова
digit_to_word = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}

# Функция для замены первой цифры на нечётной позиции на английское слово
def replace_digit_with_word(number):
    number_str = str(number)
    # Если число чётное, заменяем первую цифру на нечётной позиции
    if int(number) % 2 == 0:
        new_number = ""
        for i, digit in enumerate(number_str):
            if i % 2 == 0:  # нечётная позиция (по индексу)
                new_number += digit_to_word[digit]  # заменяем цифру на слово
            else:
                new_number += digit  # оставляем цифру как есть
        return new_number
    return number_str  # нечётные числа не изменяются

# Функция для обработки последовательности из файла
def process_sequence_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:  # читаем файл построчно
            numbers = line.split()  # разделяем строку на числа
            for number in numbers:
                if int(number) % 2 != 0:
                    print(number)  # выводим нечётные числа как есть
                else:
                    print(replace_digit_with_word(number))  # для чётных чисел заменяем первую цифру

# Пример использования программы
file_path = 'input.txt'  # путь к файлу с данными
process_sequence_from_file(file_path)
