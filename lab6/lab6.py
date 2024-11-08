"""
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию
для нахождения оптимального  решения.

Вариант 6: Кафе набирает сотрудников:  2 посудомойки (женщины), 5 грузчиков (мужчины),  5 официантов (независимо от пола).
Сформировать все возможные варианты заполнения вакантных мест, если имеются 5 женщин и 5 мужчин.
"""
    
import itertools
import time

# Данные по кандидатам
males = ["M1", "M2", "M3", "M4", "M5"]
females = ["F1", "F2", "F3", "F4", "F5"]

# Функция для алгоритмического подхода
def generate_combinations_algorithmic():
    combinations = []
    for dishwashers in itertools.combinations(females, 2):  # 2 посудомойки (женщины)
        remaining_females = set(females) - set(dishwashers)
        for loaders in itertools.combinations(males, 5):  # 5 грузчиков (мужчины)
            remaining_males = set(males) - set(loaders)
            waiters = list(remaining_females) + list(remaining_males)  # 5 официантов (любой пол)
            combinations.append((dishwashers, loaders, waiters))
    return combinations

# Функция для подхода с использованием Python функций
def generate_combinations_pythonic():
    # Все возможные наборы позиций, используя готовые функции
    dishwashers_combinations = list(itertools.combinations(females, 2))
    loaders_combinations = list(itertools.combinations(males, 5))
    combinations = [
        (dishwashers, loaders, list(set(females) - set(dishwashers)) + list(set(males) - set(loaders)))
        for dishwashers in dishwashers_combinations
        for loaders in loaders_combinations
    ]
    return combinations

# Измерение времени выполнения обоих методов с использованием time.perf_counter()
start_time = time.perf_counter()
algorithmic_combinations = generate_combinations_algorithmic()
algorithmic_time = time.perf_counter() - start_time

start_time = time.perf_counter()
pythonic_combinations = generate_combinations_pythonic()
pythonic_time = time.perf_counter() - start_time

print("Время выполнения алгоритмического метода:", algorithmic_time)
print("Время выполнения метода с использованием Python:", pythonic_time)

# Усложнение задачи: ограничение и целевая функция
def generate_optimized_combinations():
    best_combination = None
    min_length_waiters = float('inf')
    for dishwashers, loaders, waiters in generate_combinations_pythonic():
        # Ограничение: количество официантов, которые не заняты на других должностях, должно быть минимальным
        if len(waiters) < min_length_waiters:
            min_length_waiters = len(waiters)
            best_combination = (dishwashers, loaders, waiters)
    return best_combination

optimized_combination = generate_optimized_combinations()
print("Оптимальное сочетание (учитывая ограничения):", optimized_combination)
