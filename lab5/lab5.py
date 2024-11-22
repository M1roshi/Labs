"""
Задана рекуррентная функция. Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить в табличной форме.
Обязательное требование – минимизация времени выполнения и объема памяти.

Вариант 6:	F(x<2) = 5; F(n) =(-1)^n*(F(n-1)/n! * F(n-5) /(2n)!)
"""

import math
from datetime import datetime

# Рекурсивная реализация функции
def recursive_function(n):
    if n <= 2:  # Базовый случай: если n <= 2, возвращаем 5
        return 5
    return (-1)**n * (recursive_function(n - 1) * math.factorial(n) / (2 * n) * recursive_function(n - 5) / math.factorial(2 * n))

# Итеративная реализация функции
def iterative_function(n):
    if n <= 2:  # Если n <= 2, возвращаем 5
        return 5

    values = [5] * max(n + 1, 6)  # Создаем массив для промежуточных значений
    for i in range(3, n + 1):
        values[i] = (-1)**i * (values[i - 1] * math.factorial(i) / (2 * i) * values[i - 5] / math.factorial(2 * i))
    return values[n]  # Возвращаем результат для n

# Функция для сравнения времени выполнения двух методов
def compare_methods(n_values):
    results = []

    for n in n_values:
        # Рекурсивный метод
        start_time = datetime.now()  # Засекаем время
        try:
            recursive_result = recursive_function(n)
        except RecursionError:  # Если возникает ошибка переполнения стека
            recursive_result = None
        recursive_time = (datetime.now() - start_time).total_seconds()  # Вычисляем время выполнения

        # Итеративный метод
        start_time = datetime.now()  # Засекаем время
        iterative_result = iterative_function(n)
        iterative_time = (datetime.now() - start_time).total_seconds()  # Вычисляем время выполнения

        # Записываем результаты в список
        results.append({
            'n': n,
            'recursive_result': recursive_result,
            'recursive_time': recursive_time,
            'iterative_result': iterative_result,
            'iterative_time': iterative_time
        })

    return results

# Пример использования программы
n_values = range(1, 21)  # Проверяем значения n от 1 до 20
results = compare_methods(n_values)

# Выводим результаты в виде таблицы
print(f"{'n':<5}{'Рек. Результат':<15}{'Рек. Время (с)':<15}{'Итер. Результат':<15}{'Итер. Время (с)':<15}")
for result in results:
    print(f"{result['n']:<5}{str(result['recursive_result']):<15}{result['recursive_time']:<15.6f}{result['iterative_result']:<15}{result['iterative_time']:<15.6f}")
