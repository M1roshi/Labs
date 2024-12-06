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

# Рекурсивная функция
def recursive_f(n):
    if n < 2:
        return 5
    else:
        sign = 1 if n % 2 == 0 else -1
        return sign * (recursive_f(n - 1) / math.factorial(n) * recursive_f(n - 5) / math.factorial(2 * n))


# Итеративная функция
def iterative_f(n):
    if n < 2:
        return 5
    else:
        f_values = [5, 5]  # F(0) и F(1) равны 5
        factorials = [1, 1]  # Начальные значения для 0! и 1!
        
        # Рассчитываем факториалы для n и 2n
        for i in range(2, n + 1):
            factorials.append(factorials[-1] * i)
        
        # Рассчитываем итеративно значения функции F(n)
        for i in range(2, n + 1):
            f_n_minus_1 = f_values[i - 1]  # F(n-1)
            f_n_minus_5 = f_values[i - 5] if i - 5 >= 0 else 5  # F(n-5), если n-5 < 0, то берем 5
            factorial_n = factorials[i]  # n!
            factorial_2n = factorials[2 * i] if 2 * i < len(factorials) else math.factorial(2 * i)  # (2n)!
            
            f_next = (-1) ** i * (f_n_minus_1 / factorial_n * f_n_minus_5 / factorial_2n)
            f_values.append(f_next)

        return f_values[n]

# Основной цикл
p = 1
while p == 1:
    n = int(input("Введите n: "))
    
    # Вычисление и время выполнения для итеративного метода
    result_iterative = iterative_f(n)
    time_iterative = timeit.timeit("iterative_f(n)", globals=globals(), number=1)
    print(f"F({n}) (итеративно): {result_iterative}, время: {time_iterative} сек.")
    
    # Вычисление и время выполнения для рекурсивного метода
    result_recursive = recursive_f(n)
    time_recursive = timeit.timeit("recursive_f(n)", globals=globals(), number=1)
    print(f"F({n}) (рекурсивно): {result_recursive}, время: {time_recursive} сек.")
    
    print("=" * 100)
    
    # Прекращение или повторение вычислений
    p = int(input("0/1: "))




