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

# Рекурсивная версия функции
def recursive_f(n):
    if n < 2:
        return 5
    elif n == 2:
        return (-1)**n * (recursive_f(n - 1) / math.factorial(n) * recursive_f(n - 5) / math.factorial(2 * n))
    else:
        # Вычисляем рекуррентную формулу с учетом базовых значений
        fn_minus_5 = recursive_f(n - 5) if n >= 5 else 5  # Для n < 5 используем F(x < 2) как 5
        return (-1) ** n * (recursive_f(n - 1) / math.factorial(n) * fn_minus_5 / math.factorial(2 * n))

# Итеративная версия функции
def iterative_f(n):
    if n < 2:
        return 5
    elif n == 2:
        f_prev = 5  # F(1)
        f_curr = 5  # F(2)
        factorial_prev = math.factorial(1)
        factorial_2n = math.factorial(2 * 2)
        return (-1)**n * (f_prev / factorial_prev * f_curr / factorial_2n)
    else:
        f_prev = 5  # F(1)
        f_curr = 5  # F(2)
        factorial_prev = math.factorial(1)
        factorial_2n = math.factorial(2 * 2)
        for i in range(3, n + 1):
            factorial_now = math.factorial(i)
            factorial_2now = math.factorial(2 * i)
            fn_minus_5 = 5 if i < 5 else f_curr  # For i < 5, use F(x<2) as 5
            f_next = (-1) ** i * (f_prev / factorial_now * fn_minus_5 / factorial_2now)
            f_prev = f_curr
            f_curr = f_next
            factorial_prev = factorial_now
            factorial_2n = factorial_2now
        return f_curr

# Сравнительное время вычислений
p = 1
while p == 1:
    n = int(input("Введите n: "))

    # Итеративное вычисление
    result_iterative = iterative_f(n)
    time_iterative = timeit.timeit("iterative_f(n)", globals=globals(), number=1)
    print(f"F({n}) (итеративно): {result_iterative}, время: {time_iterative} сек.")

    # Рекурсивное вычисление
    try:
        result_recursive = recursive_f(n)
        time_recursive = timeit.timeit("recursive_f(n)", globals=globals(), number=1)
        print(f"F({n}) (рекурсивно): {result_recursive}, время: {time_recursive} сек.")
    except RecursionError:
        print(f"Ошибка рекурсии при n = {n} (переполнение стека)")

    print("=" * 100)

    # Ввод для продолжения или завершения работы
    p = int(input("0/1: "))



