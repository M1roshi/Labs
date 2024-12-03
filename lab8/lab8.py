
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
***


import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import math


class Circle:
    def __init__(self, x, y, radius, color="black"):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def intersects_with(self, other_circle):
        """Проверка пересечения с другим кругом."""
        distance = math.sqrt((self.x - other_circle.x)**2 + (self.y - other_circle.y)**2)
        return distance < self.radius + other_circle.radius

    def move(self, dx, dy):
        """Перемещение круга на заданное смещение."""
        self.x += dx
        self.y += dy


class CircleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Circle Manager")
        
        # Элементы управления
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        control_frame = tk.Frame(root)
        control_frame.pack()

        tk.Button(control_frame, text="Загрузить", command=self.load_circles).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(control_frame, text="Сохранить", command=self.save_circles).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(control_frame, text="Добавить круг", command=self.add_circle).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(control_frame, text="Проверить пересечения", command=self.check_intersections).grid(row=0, column=3, padx=5, pady=5)
        
        self.circles = []  # Список объектов Circle

    def load_circles(self):
        """Загрузка кругов из CSV-файла."""
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        try:
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                self.circles.clear()
                self.canvas.delete("all")
                for row in reader:
                    x, y, radius, color = int(row[0]), int(row[1]), int(row[2]), row[3]
                    self.add_circle_to_canvas(Circle(x, y, radius, color))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка загрузки файла: {e}")

    def save_circles(self):
        """Сохранение кругов в CSV-файл."""
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        try:
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                for circle in self.circles:
                    writer.writerow([circle.x, circle.y, circle.radius, circle.color])
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка сохранения файла: {e}")

    def add_circle(self):
        """Добавление нового круга через диалоговое окно."""
        dialog = tk.Toplevel(self.root)
        dialog.title("Добавить круг")

        tk.Label(dialog, text="X:").grid(row=0, column=0)
        x_entry = tk.Entry(dialog)
        x_entry.grid(row=0, column=1)

        tk.Label(dialog, text="Y:").grid(row=1, column=0)
        y_entry = tk.Entry(dialog)
        y_entry.grid(row=1, column=1)

        tk.Label(dialog, text="Радиус:").grid(row=2, column=0)
        radius_entry = tk.Entry(dialog)
        radius_entry.grid(row=2, column=1)

        tk.Label(dialog, text="Цвет:").grid(row=3, column=0)
        color_entry = tk.Entry(dialog)
        color_entry.grid(row=3, column=1)

        def add():
            try:
                x = int(x_entry.get())
                y = int(y_entry.get())
                radius = int(radius_entry.get())
                color = color_entry.get() or "black"
                self.add_circle_to_canvas(Circle(x, y, radius, color))
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Ошибка", "Некорректный ввод данных.")

        tk.Button(dialog, text="Добавить", command=add).grid(row=4, columnspan=2)

    def add_circle_to_canvas(self, circle):
        """Добавление круга на canvas и в список."""
        self.circles.append(circle)
        self.canvas.create_oval(
            circle.x - circle.radius, circle.y - circle.radius,
            circle.x + circle.radius, circle.y + circle.radius,
            fill=circle.color, outline="black"
        )

    def check_intersections(self):
        """Проверка пересечений между кругами."""
        intersections = []
        for i, circle1 in enumerate(self.circles):
            for j, circle2 in enumerate(self.circles[i + 1:], start=i + 1):
                if circle1.intersects_with(circle2):
                    intersections.append((i + 1, j + 1))
        
        if intersections:
            messagebox.showinfo("Пересечения", f"Пересекаются круги: {intersections}")
        else:
            messagebox.showinfo("Пересечения", "Нет пересекающихся кругов.")


if __name__ == "__main__":
    root = tk.Tk()
    app = CircleApp(root)
    root.mainloop()
