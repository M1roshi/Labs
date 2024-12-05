"""
Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса.
Допускается использовать любую графическую библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона  tkinter.

В программе должны быть реализованы минимум одно окно ввода, одно окно вывода (со скролингом), одно текстовое поле, одна кнопка.
"""

import tkinter as tk
from tkinter import scrolledtext

# Список женщин и мужчин
women = ['W1', 'W2', 'W3', 'W4', 'W5']
men = ['M1', 'M2', 'M3', 'M4', 'M5']

# Функция для генерации всех возможных комбинаций
def generate_combinations_with_restrictions():
    dishwashers = [(women[i], women[j]) for i in range(len(women)) for j in range(i + 1, len(women))]
    movers = [(men[m1], men[m2], men[m3], men[m4], men[m5]) for m1 in range(len(men)) for m2 in range(m1 + 1, len(men)) 
              for m3 in range(m2 + 1, len(men)) for m4 in range(m3 + 1, len(men)) for m5 in range(m4 + 1, len(men))]
    
    all_combinations = []
    for dishwasher in dishwashers:
        for mover in movers:
            remaining_women = [w for w in women if w not in dishwasher]
            remaining_men = [m for m in men if m not in mover]
            waiters = remaining_women  # Официанты — это оставшиеся женщины
            all_combinations.append((dishwasher, mover, waiters))
    
    return all_combinations

# Функция для обработки нажатия кнопки
def on_button_click(output_text):
    # Генерация всех возможных комбинаций
    combinations = generate_combinations_with_restrictions()
    
    # Очищаем текстовое поле перед выводом новых данных
    output_text.delete(1.0, tk.END)
    
    # Вывод всех вариантов в текстовое поле
    output_text.insert(tk.END, f"Количество вариантов с ограничениями: {len(combinations)}\n\n")
    for combination in combinations:
        dishwashers, movers, waiters = combination
        output_text.insert(tk.END, f"Посудомойки: {dishwashers}, Грузчики: {movers}, Официанты: {waiters}\n")
    
    # Прокрутка вниз, чтобы увидеть последние результаты
    output_text.yview(tk.END)

# Основная функция для создания графического интерфейса
def create_gui():
    # Создание основного окна
    window = tk.Tk()
    window.title("Программа для распределения работников по вакансиям")

    # Создаем окно ввода
    input_label = tk.Label(window, text="Нажмите кнопку для генерации вариантов.")
    input_label.pack(padx=10, pady=10)

    # Создаем кнопку для начала вычислений
    generate_button = tk.Button(window, text="Генерировать варианты", command=lambda: on_button_click(output_text))
    generate_button.pack(padx=10, pady=10)

    # Создаем окно для вывода данных с прокруткой
    output_label = tk.Label(window, text="Результаты:")
    output_label.pack(padx=10, pady=10)

    output_text = scrolledtext.ScrolledText(window, width=80, height=20, wrap=tk.WORD)
    output_text.pack(padx=10, pady=10)

    # Запуск главного цикла приложения
    window.mainloop()

# Запуск программы
if __name__ == "__main__":
    create_gui()
