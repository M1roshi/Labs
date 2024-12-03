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

women = ['W1', 'W2', 'W3', 'W4', 'W5']
men = ['M1', 'M2', 'M3', 'M4', 'M5']


# Алгоритмическое решение: генерация комбинаций вручную
def combinations(lst, k):
    result = []
    n = len(lst)

    def helper(start, current_combination):
        if len(current_combination) == k:
            result.append(current_combination[:])  # Сохраняем копию текущей комбинации
            return
        for i in range(start, n):
            current_combination.append(lst[i])
            helper(i + 1, current_combination)
            current_combination.pop()  # Убираем последний элемент для следующей итерации

    helper(0, [])
    return result

def generate_combinations_algorithmic(women, men):
    results = []
    
    dishwashers_combinations = combinations(women, 2)

    for dishwashers in dishwashers_combinations:
        remaining_women = [w for w in women if w not in dishwashers]

        movers_combinations = combinations(men, 5)

        for movers in movers_combinations:
            potential_waiters = remaining_women + men
            waiters_combinations = combinations(potential_waiters, 5)

            for waiters in waiters_combinations:
                results.append({
                    'Dishwashers': dishwashers,
                    'Movers': movers,
                    'Waiters': waiters
                })

    return results

def generate_combinations_pythonic(women, men):
    results = []

    for dishwashers in itertools.combinations(women, 2):
        remaining_women = set(women) - set(dishwashers)
        
        for movers in itertools.combinations(men, 5):
            potential_waiters = remaining_women.union(men)
            for waiters in itertools.combinations(potential_waiters, 5):
                results.append({
                    'Dishwashers': dishwashers,
                    'Movers': movers,
                    'Waiters': waiters
                })

    return results

# Целевая функция: минимизация количества мужчин среди официантов
def objective_function(combination):
    men_waiters = len([w for w in combination['Waiters'] if w.startswith('M')])
    return men_waiters

# Таймеры для измерения времени
algo_time = timeit.timeit(lambda: generate_combinations_algorithmic(women, men), number=1)
pyth_time = timeit.timeit(lambda: generate_combinations_pythonic(women, men), number=1)

# Генерация всех комбинаций
all_combinations_algo = generate_combinations_algorithmic(women, men)
all_combinations_pyth = generate_combinations_pythonic(women, men)

# Нахождение оптимального решения (минимум мужчин среди официантов)
optimal_combination_algo = min(all_combinations_algo, key=objective_function)
optimal_combination_pyth = min(all_combinations_pyth, key=objective_function)

# Вывод результатов
print("Результаты алгоритмического решения:")
print(f"Количество комбинаций: {len(all_combinations_algo)}")
print(f"Оптимальная комбинация: {optimal_combination_algo}")
print(f"Время выполнения: {algo_time:.8f} секунд\n")

print("Результаты Pythonic решения:")
print(f"Количество комбинаций: {len(all_combinations_pyth)}")
print(f"Оптимальная комбинация: {optimal_combination_pyth}")
print(f"Время выполнения: {pyth_time:.8f} секунд")

