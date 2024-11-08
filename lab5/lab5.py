"""
Задана рекуррентная функция. Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить в табличной форме.
Обязательное требование – минимизация времени выполнения и объема памяти.

Вариант 6:	F(x<2) = 5; F(n) =(-1)^n*(F(n-1)/n! * F(n-5) /(2n)!)
"""

import time
import math

# Рекурсивный метод с использованием стека для минимизации глубины рекурсии и памяти
memo = {0: 5, 1: 5}  # Кеш для уже вычисленных значений

def F_rec_stack(n):
    if n in memo:
        return memo[n]  # Возвращаем значение, если оно уже в кеше
    
    stack = [n]  # Инициализируем стек
    while stack:
        top = stack[-1]
        # Начальные условия
        if top < 2:
            memo[top] = 5
            stack.pop()
        elif top not in memo:
            # Проверяем, есть ли необходимые промежуточные значения
            if top - 1 in memo and top - 5 in memo:
                # Вычисляем значение и сохраняем в кеше
                memo[top] = (-1) ** top * (memo[top - 1] / math.factorial(top) * memo[top - 5] / math.factorial(2 * top))
                stack.pop()
            else:
                # Добавляем отсутствующие промежуточные значения в стек
                if top - 1 not in memo:
                    stack.append(top - 1)
                if top - 5 not in memo:
                    stack.append(top - 5)
        else:
            stack.pop()
    return memo[n]

# Итерационный метод
def F_iter(n):
    if n < 2:
        return 5  # Начальные условия
    values = [5, 5]  # Начальные значения для F(0) и F(1)
    for i in range(2, n + 1):
        # Проверяем, доступны ли индексы для значений i-1 и i-5
        if i - 5 >= 0:
            current_value = (-1) ** i * (values[i - 1] / math.factorial(i) * values[i - 5] / math.factorial(2 * i))
        else:
            current_value = (-1) ** i * (values[i - 1] / math.factorial(i))  # Если i-5 недоступен, вычисляем только с i-1
        values.append(current_value)  # Сохраняем значение
    return values[n]

# Функция для усредненного замера времени выполнения
def measure_time(n, repetitions=10000):
    # Замер времени для рекурсивного метода
    start_time = time.perf_counter()
    for _ in range(repetitions):
        F_rec_stack(n)
    rec_time = (time.perf_counter() - start_time) / repetitions  # Среднее время

    # Замер времени для итерационного метода
    start_time = time.perf_counter()
    for _ in range(repetitions):
        F_iter(n)
    iter_time = (time.perf_counter() - start_time) / repetitions  # Среднее время

    return rec_time, iter_time

# Вывод таблицы результатов
print(f"{'n':>5} | {'Рекурсивный (с)':>15} | {'Итеративный (с)':>15}")
print("-" * 40)
for n in range(2, 21):
    rec_time, iter_time = measure_time(n)
    print(f"{n:>5} | {rec_time:>15.8f} | {iter_time:>15.8f}")
