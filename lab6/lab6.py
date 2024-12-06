"""
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию
для нахождения оптимального  решения.

Вариант 6: Кафе набирает сотрудников:  2 посудомойки (женщины), 5 грузчиков (мужчины),  5 официантов (независимо от пола).
Сформировать все возможные варианты заполнения вакантных мест, если имеются 5 женщин и 5 мужчин.
"""
    
import timeit

# Список женщин и мужчин
women = ['W1', 'W2', 'W3', 'W4', 'W5']
men = ['M1', 'M2', 'M3', 'M4', 'M5']

# Вариант 1: Алгоритмическое решение (без использования itertools)
def generate_combinations_algorithmic():
    all_combinations = []
    
    # Перебираем все возможные пары женщин для посудомоек
    for i in range(len(women)):
        for j in range(i + 1, len(women)):  # Выбираем пару без повторений
            # Выбираем всех мужчин для грузчиков (1 способ)
            for m1 in range(len(men)):
                for m2 in range(m1 + 1, len(men)):
                    for m3 in range(m2 + 1, len(men)):
                        for m4 in range(m3 + 1, len(men)):
                            for m5 in range(m4 + 1, len(men)):
                                # Генерируем всех официантов (оставшихся женщин)
                                remaining_women = [w for k, w in enumerate(women) if k != i and k != j]
                                # Мужчины уже все заняты, поэтому официанты это оставшиеся женщины
                                waiters = remaining_women
                                
                                # Добавляем текущую комбинацию в список
                                all_combinations.append(((women[i], women[j]), (men[m1], men[m2], men[m3], men[m4], men[m5]), waiters))
    
    return all_combinations

# Вариант 2: Использование функций Python
def choose_dishwashers(women):
    return [(women[i], women[j]) for i in range(len(women)) for j in range(i + 1, len(women))]

def choose_movers(men):
    return [(men[m1], men[m2], men[m3], men[m4], men[m5]) for m1 in range(len(men)) for m2 in range(m1 + 1, len(men)) for m3 in range(m2 + 1, len(men)) for m4 in range(m3 + 1, len(men)) for m5 in range(m4 + 1, len(men))]

def generate_all_combinations(dishwashers, movers, women, men):
    all_combinations = []
    
    for dishwasher in dishwashers:
        for mover in movers:
            remaining_women = [w for w in women if w not in dishwasher]
            remaining_men = [m for m in men if m not in mover]
            waiters = remaining_women + remaining_men
            all_combinations.append((dishwasher, mover, waiters))
    
    return all_combinations

# Вариант 3: Усложнённое решение с ограничениями
def generate_combinations_with_restrictions():
    dishwashers = [(women[i], women[j]) for i in range(len(women)) for j in range(i + 1, len(women))]
    movers = [(men[m1], men[m2], men[m3], men[m4], men[m5]) for m1 in range(len(men)) for m2 in range(m1 + 1, len(men)) for m3 in range(m2 + 1, len(men)) for m4 in range(m3 + 1, len(men)) for m5 in range(m4 + 1, len(men))]
    
    all_combinations = []
    for dishwasher in dishwashers:
        for mover in movers:
            remaining_women = [w for w in women if w not in dishwasher]
            remaining_men = [m for m in men if m not in mover]
            waiters = remaining_women  # Официанты — это оставшиеся женщины
            all_combinations.append((dishwasher, mover, waiters))
    
    return all_combinations

# Основная функция для выполнения
def main():
    # Алгоритмическое решение
    start_time = timeit.default_timer()
    combinations_algorithmic = generate_combinations_algorithmic()
    end_time = timeit.default_timer()
    print(f"Количество вариантов (алгоритмический): {len(combinations_algorithmic)}")
    print(f"Время выполнения (алгоритмический): {end_time - start_time:.6f} секунд")
    
    # Решение с использованием функций
    start_time = timeit.default_timer()
    dishwashers = choose_dishwashers(women)
    movers = choose_movers(men)
    combinations_functions = generate_all_combinations(dishwashers, movers, women, men)
    end_time = timeit.default_timer()
    print(f"Количество вариантов (с использованием функций): {len(combinations_functions)}")
    print(f"Время выполнения (с использованием функций): {end_time - start_time:.6f} секунд")
    
    # Решение с ограничениями
    start_time = timeit.default_timer()
    combinations_restricted = generate_combinations_with_restrictions()
    end_time = timeit.default_timer()
    print(f"Количество вариантов с ограничениями: {len(combinations_restricted)}")
    print(f"Время выполнения (с ограничениями): {end_time - start_time:.6f} секунд")
    
    # Вывод всех вариантов с ограничениями
    print("\nВсе возможные комбинации работников, если имеются 5 женщин и 5 мужчин:")
    for combination in combinations_restricted:
        dishwashers, movers, waiters = combination
        print(f"\nПосудомойки: {dishwashers}, Грузчики: {movers}, Официанты: {waiters}")

# Запуск программы
if __name__ == "__main__":
    main()

