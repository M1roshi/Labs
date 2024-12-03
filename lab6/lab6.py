"""
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию
для нахождения оптимального  решения.

Вариант 6: Кафе набирает сотрудников:  2 посудомойки (женщины), 5 грузчиков (мужчины),  5 официантов (независимо от пола).
Сформировать все возможные варианты заполнения вакантных мест, если имеются 5 женщин и 5 мужчин.
"""
    
import itertools
import timeit

# Исходные данные
women = ['W1', 'W2', 'W3', 'W4', 'W5']  # 5 женщин
men = ['M1', 'M2', 'M3', 'M4', 'M5']  # 5 мужчин

# Генерация всех возможных вариантов
def generate_all_combinations(women, men):
    results = []
    # 1. Комбинации для посудомоек (2 женщины)
    for dishwashers in itertools.combinations(women, 2):
        # Оставшиеся женщины
        remaining_women = set(women) - set(dishwashers)
        
        # 2. Комбинации для грузчиков (5 мужчин)
        for movers in itertools.combinations(men, 5):
            
            # 3. Комбинации для официантов (5 любых из оставшихся женщин и всех мужчин)
            potential_waiters = remaining_women.union(men)  # Оставшиеся женщины + мужчины
            for waiters in itertools.combinations(potential_waiters, 5):
                results.append({
                    'Dishwashers': dishwashers,
                    'Movers': movers,
                    'Waiters': waiters
                })
    return results


# Алгоритмическое решение
def generate_combinations_algorithmic(women, men):
    results = []
    for dishwashers in itertools.combinations(women, 2):
        remaining_women = set(women) - set(dishwashers)
        for movers in itertools.combinations(men, 5):
            for waiters in itertools.combinations(remaining_women.union(men), 5):
                results.append({
                    'Dishwashers': dishwashers,
                    'Movers': movers,
                    'Waiters': waiters
                })
    return results

# Решение с использованием Python-функций
def generate_combinations_pythonic(women, men):
    return [
        {
            'Dishwashers': dishwashers,
            'Movers': movers,
            'Waiters': waiters
        }
        for dishwashers in itertools.combinations(women, 2)
        for movers in itertools.combinations(men, 5)
        for waiters in itertools.combinations(set(women) - set(dishwashers) | set(men), 5)
    ]

# Усложнение: ограничение и целевая функция
def generate_combinations_with_constraints(women, men):
    optimal_combinations = []
    min_movers = float('inf')
    for dishwashers in itertools.combinations(women, 2):
        remaining_women = set(women) - set(dishwashers)
        for movers in itertools.combinations(men, 5):
            for waiters in itertools.combinations(remaining_women.union(men), 5):
                # Проверяем условие: официанты из разного пола
                women_waiters = len(set(waiters) & set(women))
                men_waiters = len(set(waiters) & set(men))
                if women_waiters == men_waiters:  # Равное количество мужчин и женщин
                    if len(movers) < min_movers:
                        min_movers = len(movers)
                        optimal_combinations = [{
                            'Dishwashers': dishwashers,
                            'Movers': movers,
                            'Waiters': waiters
                        }]
                    elif len(movers) == min_movers:
                        optimal_combinations.append({
                            'Dishwashers': dishwashers,
                            'Movers': movers,
                            'Waiters': waiters
                        })
    return optimal_combinations

# Замеры времени выполнения с использованием timeit
algo_time = timeit.timeit(lambda: generate_combinations_algorithmic(women, men), number=1)
pythonic_time = timeit.timeit(lambda: generate_combinations_pythonic(women, men), number=1)
constraint_time = timeit.timeit(lambda: generate_combinations_with_constraints(women, men), number=1)

# Генерация комбинаций
all_combinations = generate_all_combinations(women, men)

# Вывод результатов
print(f"Часть 1: Сравнение алгоритмического и Pythonic решений")
print(f"Алгоритмическое решение: {algo_time:.8f} сек")
print(f"Pythonic решение: {pythonic_time:.8f} сек")

print("\nЧасть 2: Генерация с ограничением и целевой функцией")
print(f"С ограничением: {constraint_time:.8f} сек")

# Вывод количества вариантов и примера комбинации
print(f"Количество всех возможных комбинаций: {len(all_combinations)}")
print("Пример одной комбинации:")
print(all_combinations[0])
