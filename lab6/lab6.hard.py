import itertools

# Женщины и мужчины с возрастом
women = [('w1', 25), ('w2', 30), ('w3', 28), ('w4', 23), ('w5', 35)]
men = [('m1', 40), ('m2', 45), ('m3', 38), ('m4', 27), ('m5', 33)]

# Оптимизированный подход с целевой функцией и ограничением на возраст
def optimized_approach_with_conditions():
    optimal_combination = None
    min_average_age = float('inf')  # Инициализируем средний возраст бесконечностью
    
    # Перебираем все возможные комбинации для 2 посудомоек из 5 женщин
    for dishwashers in itertools.combinations(women, 2):
        remaining_women = [w for w in women if w not in dishwashers]

        # Перебираем все возможные комбинации для 5 грузчиков из мужчин
        for loaders in itertools.combinations(men, 5):
            # Проверка условия: все грузчики старше 25 лет
            if all(loader[1] > 25 for loader in loaders):
                remaining_men = [m for m in men if m not in loaders]

                # Определяем официантов: выбираем до 3 женщин (самых молодых) + оставшихся мужчин
                sorted_remaining_women = sorted(remaining_women, key=lambda x: x[1])
                women_waiters = sorted_remaining_women[:3]
                waiters = women_waiters + remaining_men

                # Целевая функция: минимизировать средний возраст официантов
                average_age = sum(person[1] for person in waiters) / len(waiters)
                
                if average_age < min_average_age:
                    min_average_age = average_age
                    optimal_combination = (dishwashers, loaders, waiters)

    return optimal_combination, min_average_age


# Функция для вывода результата
def print_optimized_solution(result):
    dishwashers, loaders, waiters = result[0]
    min_average_age = result[1]

    print("\nОптимальное распределение сотрудников:")
    print("Посудомойки:")
    for d in dishwashers:
        print(f"  {d[0]} (возраст: {d[1]})")

    print("\nГрузчики:")
    for l in loaders:
        print(f"  {l[0]} (возраст: {l[1]})")

    print("\nОфицианты:")
    for w in waiters:
        print(f"  {w[0]} (возраст: {w[1]})")

    print(f"\nСредний возраст официантов: {min_average_age:.2f} лет")


# Запускаем оптимизацию
optimal_combination, min_average_age = optimized_approach_with_conditions()

# Выводим результат
print_optimized_solution((optimal_combination, min_average_age))
