"""
Задана рекуррентная функция. Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить в табличной форме.
Обязательное требование – минимизация времени выполнения и объема памяти.

Вариант 6:	F(x<2) = 5; F(n) =(-1)^n*(F(n-1)/n! * F(n-5) /(2n)!)
"""

import math
from functools import lru_cache
import timeit

# Рекурсивная функция с мемоизацией
@lru_cache(maxsize=None)
def F_recursive(n):
    if n < 2:
        return 5
    return (-1)**n * (F_recursive(n-1) / math.factorial(n) * F_recursive(n-5) / math.factorial(2*n))

# Итерационная функция
def F_iterative(n):
    if n < 2:
        return 5
    results = [5] * (n + 1)
    for i in range(2, n + 1):
        results[i] = (-1)**i * (results[i-1] / math.factorial(i) * (results[i-5] if i-5 >= 0 else 5) / math.factorial(2*i))
    return results[n]

# Функция для измерения времени через timeit
def measure_with_timeit(func, n, iterations=10):
    # Подготовка строки вызова функции
    setup_code = f"from __main__ import {func.__name__}, math"
    test_code = f"{func.__name__}({n})"
    # Измерение времени
    time = timeit.timeit(stmt=test_code, setup=setup_code, number=iterations)
    return time / iterations  # Возвращаем среднее время за одну итерацию

# Сравнение методов и вывод таблицы
def compare_methods_timeit(max_n, iterations=10):
    print(f"{'n':<5}{'Рек. Время (с)':<20}{'Итер. Время (с)':<20}{'Рек. Результат':<20}{'Итер. Результат':<20}")
    for n in range(max_n + 1):
        rec_time = measure_with_timeit(F_recursive, n, iterations)
        iter_time = measure_with_timeit(F_iterative, n, iterations)
        rec_result = F_recursive(n)
        iter_result = F_iterative(n)
        print(f"{n:<5}{rec_time:<20.6f}{iter_time:<20.6f}{rec_result:<20}{iter_result:<20}")

# Пример запуска
max_n = 15  # Максимальное значение n
iterations = 100  # Количество повторений для timeit
compare_methods_timeit(max_n, iterations)

