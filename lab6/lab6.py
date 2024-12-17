"""
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию
для нахождения оптимального  решения.

Вариант 6: Кафе набирает сотрудников:  2 посудомойки (женщины), 5 грузчиков (мужчины),  5 официантов (независимо от пола).
Сформировать все возможные варианты заполнения вакантных мест, если имеются 5 женщин и 5 мужчин.
"""
    
import timeit
import itertools

# Данные
women = ['Женщина1', 'Женщина2', 'Женщина3', 'Женщина4', 'Женщина5']
men = ['Мужчина1', 'Мужчина2', 'Мужчина3', 'Мужчина4', 'Мужчина5']

# 1. Алгоритмическое решение
def algorithmic_solution(women, men):
    # Перебор женщин для посудомоек
    dishwashers = []
    for i in range(len(women)):
        for j in range(i+1, len(women)):
            dishwashers.append([women[i], women[j]])
    
    # Перебор мужчин для грузчиков
    loaders = []
    for i in range(len(men)):
        for j in range(i+1, len(men)):
            for k in range(j+1, len(men)):
                for l in range(k+1, len(men)):
                    for m in range(l+1, len(men)):
                        loaders.append([men[i], men[j], men[k], men[l], men[m]])
    
    # Формируем все возможные варианты для официантов
    all_workers = women + men
    waiters_combinations = []
    for i in range(len(all_workers)):
        for j in range(i+1, len(all_workers)):
            for k in range(j+1, len(all_workers)):
                for l in range(k+1, len(all_workers)):
                    for m in range(l+1, len(all_workers)):
                        waiters_combinations.append([all_workers[i], all_workers[j], all_workers[k], all_workers[l], all_workers[m]])
    
    return dishwashers, loaders, waiters_combinations

# Измерение времени для алгоритмического решения
def time_algorithmic_solution():
    return timeit.timeit(lambda: algorithmic_solution(women, men), number=1)

# 2. Решение с использованием Python функций (itertools)

def python_function_solution(women, men):
    # Перебор женщин для посудомоек
    dishwashers = list(itertools.combinations(women, 2))

    # Перебор мужчин для грузчиков
    loaders = list(itertools.combinations(men, 5))

    # Формируем все возможные варианты для официантов
    all_workers = women + men
    waiters_combinations = list(itertools.combinations(all_workers, 5))

    return dishwashers, loaders, waiters_combinations

# Измерение времени для решения с использованием itertools
def time_python_function_solution():
    return timeit.timeit(lambda: python_function_solution(women, men), number=1)

# 3. Усложненное решение с ограничениями (не более 3 женщин среди официантов)
def complex_solution(women, men, max_women_in_waiters=3):
    # Перебор женщин для посудомоек
    dishwashers = []
    for i in range(len(women)):
        for j in range(i+1, len(women)):
            dishwashers.append([women[i], women[j]])
    
    # Перебор мужчин для грузчиков
    loaders = []
    for i in range(len(men)):
        for j in range(i+1, len(men)):
            for k in range(j+1, len(men)):
                for l in range(k+1, len(men)):
                    for m in range(l+1, len(men)):
                        loaders.append([men[i], men[j], men[k], men[l], men[m]])
    
    # Формируем все возможные варианты для официантов с ограничениями
    all_workers = women + men
    valid_waiters_combinations = []
    for i in range(len(all_workers)):
        for j in range(i+1, len(all_workers)):
            for k in range(j+1, len(all_workers)):
                for l in range(k+1, len(all_workers)):
                    for m in range(l+1, len(all_workers)):
                        combination = [all_workers[i], all_workers[j], all_workers[k], all_workers[l], all_workers[m]]
                        women_count = sum(1 for worker in combination if worker in women)
                        if women_count <= max_women_in_waiters:
                            valid_waiters_combinations.append(combination)
    
    return dishwashers, loaders, valid_waiters_combinations

# Измерение времени для усложненного решения
def time_complex_solution():
    return timeit.timeit(lambda: complex_solution(women, men), number=1)

# 4. Формирование всех возможных вариантов для каждой категории

# 4.1. Посудомойки (2 женщины из 5)
dishwashers = list(itertools.combinations(women, 2))

# 4.2. Грузчики (5 мужчин из 5)
loaders = list(itertools.combinations(men, 5))

# 4.3. Официанты (5 человек из 10: женщин и мужчин)
all_workers = women + men
waiters_combinations = list(itertools.combinations(all_workers, 5))

# Запуск и вывод времени выполнения для каждого решения
algorithmic_time = time_algorithmic_solution()
python_function_time = time_python_function_solution()
complex_solution_time = time_complex_solution()

print(f"Время выполнения алгоритмического решения: {algorithmic_time:.6f} секунд.")
print(f"Время выполнения решения с использованием функций Python: {python_function_time:.6f} секунд.")
print(f"Время выполнения усложненного решения с ограничениями: {complex_solution_time:.6f} секунд.")

# Вывод результатов
print(f"Все возможные варианты для посудомоек (2 женщины): {dishwashers}")
print(f"Все возможные варианты для грузчиков (5 мужчин): {loaders}")
print(f"Все возможные варианты для официантов (5 человек): {waiters_combinations}")


