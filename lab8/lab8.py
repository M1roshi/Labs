"""
Требуется написать ООП с графическим интерфейсом в соответствии со своим вариантом. 
Должны быть реализованы минимум один класс, три атрибута, четыре метода (функции). 
Ввод данных из файла с контролем правильности ввода. 
Базы данных не использовать. При необходимости сохранять информацию в файлах, разделяя значения запятыми (CSV файлы) или пробелами. Для GUI и визуализации использовать библиотеку tkinter.

Вариант 6
Объекты – круги
Функции:	проверка пересечения
            визуализация
            раскраска
            перемещение на плоскости
"""


import tkinter as tk
from tkinter import messagebox, simpledialog, colorchooser, filedialog
import math
import csv

class Circle:
    def __init__(self, x, y, radius, color="black"):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def intersects(self, other):
        # Проверка пересечения двух кругов
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance < (self.radius + other.radius)

    def move(self, dx, dy):
        # Перемещение круга на плоскости
        self.x += dx
        self.y += dy

    def change_color(self, new_color):
        # Изменение цвета круга
        self.color = new_color

    def draw(self, canvas):
        # Отображение круга на холсте
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius,
                           outline=self.color, width=2, fill=self.color)


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Circle App")
        self.geometry("800x600")

        self.circles = []

        # Создание холста
        self.canvas = tk.Canvas(self, width=800, height=500, bg="white")
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Создание фрейма для кнопок
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.create_buttons()

    def create_buttons(self):
        # Кнопки для добавления и работы с кругами
        self.add_button = tk.Button(self.button_frame, text="Добавить круг", command=self.add_circle)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.move_button = tk.Button(self.button_frame, text="Переместить круг", command=self.move_circle)
        self.move_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.color_button = tk.Button(self.button_frame, text="Изменить цвет", command=self.change_color)
        self.color_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.check_button = tk.Button(self.button_frame, text="Проверить пересечение", command=self.check_intersection)
        self.check_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.load_button = tk.Button(self.button_frame, text="Загрузить из файла", command=self.load_from_file)
        self.load_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = tk.Button(self.button_frame, text="Сохранить в файл", command=self.save_to_file)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

    def add_circle(self):
        # Добавление круга с введёнными параметрами через диалоговые окна
        try:
            x = simpledialog.askinteger("Ввод", "Введите x координату центра круга:", parent=self)
            if x is None:
                return
            y = simpledialog.askinteger("Ввод", "Введите y координату центра круга:", parent=self)
            if y is None:
                return
            radius = simpledialog.askinteger("Ввод", "Введите радиус круга:", parent=self, minvalue=1)
            if radius is None:
                return
            color = colorchooser.askcolor(title="Выберите цвет круга")[1]
            if color is None:
                color = "black"

            new_circle = Circle(x, y, radius, color)
            self.circles.append(new_circle)
            self.redraw_circles()
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный ввод данных!")

    def move_circle(self):
        # Перемещение круга через диалоговые окна
        if not self.circles:
            messagebox.showinfo("Информация", "Нет кругов для перемещения.")
            return

        try:
            index = simpledialog.askinteger("Перемещение", f"Введите номер круга (0 - {len(self.circles)-1}):", parent=self)
            if index is None:
                return
            if not (0 <= index < len(self.circles)):
                messagebox.showerror("Ошибка", "Неверный номер круга.")
                return
            dx = simpledialog.askinteger("Перемещение", "Введите смещение по X:", parent=self)
            if dx is None:
                return
            dy = simpledialog.askinteger("Перемещение", "Введите смещение по Y:", parent=self)
            if dy is None:
                return

            self.circles[index].move(dx, dy)
            self.redraw_circles()
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный ввод данных!")

    def change_color(self):
        # Изменение цвета круга через диалоговые окна
        if not self.circles:
            messagebox.showinfo("Информация", "Нет кругов для изменения цвета.")
            return

        try:
            index = simpledialog.askinteger("Изменение цвета", f"Введите номер круга (0 - {len(self.circles)-1}):", parent=self)
            if index is None:
                return
            if not (0 <= index < len(self.circles)):
                messagebox.showerror("Ошибка", "Неверный номер круга.")
                return
            new_color = colorchooser.askcolor(title="Выберите новый цвет")[1]
            if new_color is None:
                return

            self.circles[index].change_color(new_color)
            self.redraw_circles()
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный ввод данных!")

    def check_intersection(self):
        # Проверка пересечения всех кругов
        intersections = []
        for i in range(len(self.circles)):
            for j in range(i + 1, len(self.circles)):
                if self.circles[i].intersects(self.circles[j]):
                    intersections.append(f"Круг {i} и круг {j} пересекаются.")
        if intersections:
            messagebox.showinfo("Пересечения", "\n".join(intersections))
        else:
            messagebox.showinfo("Пересечения", "Пересечений нет.")

    def redraw_circles(self):
        # Перерисовка всех кругов
        self.canvas.delete("all")
        for circle in self.circles:
            circle.draw(self.canvas)

    def load_from_file(self):
        # Загрузка данных из файла через диалоговое окно
        file_path = filedialog.askopenfilename(title="Выберите файл", filetypes=[("CSV файлы", "*.csv")])
        if not file_path:
            return
        try:
            with open(file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                self.circles.clear()
                for row in reader:
                    if len(row) != 4:
                        continue
                    x, y, radius, color = int(row[0]), int(row[1]), int(row[2]), row[3]
                    circle = Circle(x, y, radius, color)
                    self.circles.append(circle)
            self.redraw_circles()
            messagebox.showinfo("Успех", "Круги успешно загружены из файла.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл.\n{e}")

    def save_to_file(self):
        # Сохранение данных в файл через диалоговое окно
        if not self.circles:
            messagebox.showinfo("Информация", "Нет кругов для сохранения.")
            return
        file_path = filedialog.asksaveasfilename(title="Сохранить файл", defaultextension=".csv",
                                                 filetypes=[("CSV файлы", "*.csv")])
        if not file_path:
            return
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                for circle in self.circles:
                    writer.writerow([circle.x, circle.y, circle.radius, circle.color])
            messagebox.showinfo("Успех", "Круги успешно сохранены в файл.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл.\n{e}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()

