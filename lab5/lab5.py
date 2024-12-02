"""
Задана рекуррентная функция. Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить в табличной форме.
Обязательное требование – минимизация времени выполнения и объема памяти.

Вариант 6:	F(x<2) = 5; F(n) =(-1)^n*(F(n-1)/n! * F(n-5) /(2n)!)
"""

import math
import timeit

# Рекурсивная функция с мемоизацией
memo = {}

def F_recursive(n):
    if n < 2:
        return 5
    if n not in memo:
        memo[n] = ((-1) ** n) * (
            F_recursive(n - 1) / math.factorial(n) * F_recursive(n - 5) / math.factorial(2 * n)
        )
    return memo[n]

# Итеративная функция с уменьшением на постоянную величину
def F_iterative_optimized(n):
    if n < 2:
        return 5
    values = [5, 5, 5, 5, 5]  # Начальные значения F(0), F(1), ..., F(4)
    for i in range(2, n + 1):
        current = ((-1) ** i) * (
            values[-1] / math.factorial(i) * values[0] / math.factorial(2 * i)
        )
        # Обновляем массив значений (сдвигаем на 1 позицию)
        values = values[1:] + [current]
    return values[-1]

# Функция для измерения времени с использованием timeit
def measure_time_optimized(n, repeats=10):
    recursive_time = float('inf')
    iterative_time = float('inf')

    # Измерение рекурсивного метода
    try:
        recursive_time = timeit.timeit(lambda: F_recursive(n), number=repeats) / repeats
    except RecursionError:
        recursive_time = float('inf')  # Если превышена глубина стека

    # Измерение итеративного метода
    iterative_time = timeit.timeit(lambda: F_iterative_optimized(n), number=repeats) / repeats

    return recursive_time, iterative_time

# Вывод таблицы результатов
def print_results_optimized(max_n, repeats=10):
    print(f"{'n':<5}{'Rec Time (s)':<20}{'Iter Time (s)':<20}")
    print("-" * 45)
    for n in range(max_n + 1):
        rec_time, iter_time = measure_time_optimized(n, repeats)
        print(f"{n:<5}{rec_time:<20.10f}{iter_time:<20.10f}")

# Пример выполнения
if __name__ == "__main__":
    max_n = 50  # Максимальное значение n
    repeats = 1000  # Количество повторов для измерений
    print_results_optimized(max_n, repeats)


