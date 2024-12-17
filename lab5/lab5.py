"""
Задана рекуррентная функция. Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить в табличной форме.
Обязательное требование – минимизация времени выполнения и объема памяти.

Вариант 6:	F(x<2) = 5; F(n) =(-1)^n*(F(n-1)/n! * F(n-5) /(2n)!)
"""

import timeit

# Рекурсивная версия с мемоизацией
def F_recursive(n, memo=None):
    if memo is None:
        memo = {1: 5}  # базовый случай F(x < 2) = 5
    if n < 2:
        return 5
    if n in memo:
        return memo[n]
    
    # Факториал через предыдущее значение
    factorial_n = 1
    factorial_2n = 1
    for i in range(2, n + 1):
        factorial_n *= i
        factorial_2n *= 2 * i
        factorial_2n *= (2 * i - 1)

    # Основная формула для рекурсивного вычисления
    result = (-1) ** n * (F_recursive(n - 1, memo) / factorial_n) * (F_recursive(n - 5, memo) / factorial_2n)
    memo[n] = result
    return result

# Итеративная версия
def F_iterative(n):
    if n == 1:
        return 5
    elif n == 2:
        return 5
    
    values = {1: 5, 2: 5}  # базовый случай F(x < 2) = 5
    f_prev = 5  # Значение F(1)
    f_curr = 5  # Значение F(2)
    minus = -1
    
    # Инициализация факториалов
    factorial_back = 1
    factorial_now = 2
    
    for i in range(3, n + 1):
        factorial_now = factorial_back * (2 * i) * (2 * i - 1)
        f_next = minus * (f_prev / factorial_now) * (f_curr / factorial_now)
        
        # Обновляем переменные для следующей итерации
        f_prev = f_curr
        f_curr = f_next
        factorial_back = factorial_now
        minus *= -1
    
    return f_curr

# Функции для замера времени
def measure_recursive_time(n):
    return timeit.timeit(lambda: F_recursive(n), number=1)

def measure_iterative_time(n):
    return timeit.timeit(lambda: F_iterative(n), number=1)

# Сравнение времени выполнения
def compare_times(n_max):
    print(f"{'n':<5}{'Recursive Time (s)':<25}{'Iterative Time (s)'}")
    print("-" * 50)
    
    for n in range(1, n_max + 1):
        # Рекурсивное время
        recursive_time = measure_recursive_time(n)
        
        # Итеративное время
        iterative_time = measure_iterative_time(n)
        
        # Выводим результаты
        print(f"{n:<5}{recursive_time:<25}{iterative_time}")

# Выполнение эксперимента для n от 1 до 20
n_max = 20
compare_times(n_max)




