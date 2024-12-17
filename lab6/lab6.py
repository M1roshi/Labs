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

# Женщины и мужчины
women = ['w1', 'w2', 'w3', 'w4', 'w5']
men = ['m1', 'm2', 'm3', 'm4', 'm5']

# 1. Алгоритмический подход
def algorithmic_approach():
    combinations = []

    # Перебираем 2 женщины для посудомоек
    for i in range(len(women)):
        for j in range(i + 1, len(women)):
            dishwashers = [women[i], women[j]]
            remaining_women = [w for w in women if w not in dishwashers]

            # Перебираем 5 мужчин для грузчиков
            for k in range(len(men)):
                for l in range(k + 1, len(men)):
                    for m in range(l + 1, len(men)):
                        for n in range(m + 1, len(men)):
                            for o in range(n + 1, len(men)):
                                loaders = [men[k], men[l], men[m], men[n], men[o]]
                                remaining_men = [m for m in men if m not in loaders]

                                # Официанты: оставшиеся сотрудники
                                waiters = remaining_women + remaining_men
                                combinations.append((dishwashers, loaders, waiters))
    return combinations

# 2. Pythonic подход с использованием itertools
def pythonic_approach():
    combinations = []

    # Все комбинации для посудомоек (2 женщины)
    for dishwashers in itertools.combinations(women, 2):
        remaining_women = [w for w in women if w not in dishwashers]

        # Все комбинации для грузчиков (5 мужчин)
        for loaders in itertools.combinations(men, 5):
            remaining_men = [m for m in men if m not in loaders]

            # Официанты: оставшиеся сотрудники
            waiters = remaining_women + remaining_men
            combinations.append((dishwashers, loaders, waiters))
    return combinations

# Функция для вывода всех вариантов
def print_combinations(combinations, method_name):
    print(f"\n{method_name}: Всего {len(combinations)} вариантов\n")
    for i, (dishwashers, loaders, waiters) in enumerate(combinations):
        print(f"Вариант {i+1}:")
        print(f"  Посудомойки: {', '.join(dishwashers)}")
        print(f"  Грузчики: {', '.join(loaders)}")
        print(f"  Официанты: {', '.join(waiters)}")
        print('-' * 40)

# Замер времени с помощью timeit
algorithmic_time = timeit.timeit(algorithmic_approach, number=1)
pythonic_time = timeit.timeit(pythonic_approach, number=1)

# Запускаем функции и сохраняем результаты
algorithmic_result = algorithmic_approach()
pythonic_result = pythonic_approach()

# Сравнение времени
print(f"Время выполнения алгоритмического подхода: {algorithmic_time:.8f} секунд")
print(f"Время выполнения Pythonic подхода: {pythonic_time:.8f} секунд")

# Выводим все результаты
print_combinations(algorithmic_result, "Алгоритмический подход")
print_combinations(pythonic_result, "Pythonic подход")


