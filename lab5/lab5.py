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
from functools import lru_cache

# Рекурсивное вычисление с мемоизацией
@lru_cache(None)  # Без ограничений на кэш
def recursive_F(n):
    if n < 2:
        return 5
    else:
        term1 = recursive_F(n - 1) / math.factorial(n)
        term2 = recursive_F(n - 5) / math.factorial(2 * n)
        return (-1)**n * term1 * term2

# Итеративное вычисление
def iterative_F(n):
    if n < 2:
        return 5
    
    values = [5, 5]  # Начальные значения F(0) и F(1)
    
    for i in range(2, n+1):
        term1 = values[i-1] / math.factorial(i)
        term2 = values[i-5] / math.factorial(2 * i) if i >= 5 else 0
        result = (-1)**i * term1 * term2
        values.append(result)
    
    return values[n]

# Измерение времени выполнения с использованием timeit
def measure_time(func, n):
    stmt = f"{func.__name__}({n})"  # Строка, которая вызывает функцию с аргументом
    setup = f"from __main__ import {func.__name__}"  # Подключение функции из основного модуля
    return timeit.timeit(stmt=stmt, setup=setup, number=100)  # Измеряем время выполнения 100 раз

# Основной блок
def main():
    try:
        n_max = int(input("Введите максимальное значение n: "))  # Запрос максимального значения n
        if n_max < 1:
            print("Значение n должно быть больше или равно 1.")
            return
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите целое число.")
        return
    
    results = []

    print("Измерения времени работы:")
    print(" n  | Recursive Time (s) | Iterative Time (s)")
    print("-----------------------------------------------")
    
    # Измеряем для всех значений от 1 до n_max
    for n in range(1, n_max + 1):
        # Измеряем время выполнения
        recursive_time = measure_time(recursive_F, n)
        iterative_time = measure_time(iterative_F, n)
        
        results.append((n, recursive_time, iterative_time))
    
    # Выводим результаты в табличной форме
    for result in results:
        print(f" {result[0]}  | {result[1]:.6f}        | {result[2]:.6f}")

if __name__ == "__main__":
    main()


