import numpy as np
import matplotlib.pyplot as plt

# Ввод значений K и N
K = int(input("Введите значение K: "))
N = int(input("Введите значение N: "))

if N % 2 != 0:
    raise ValueError("N должно быть четным числом!")

size = N // 2

# Чтение матрицы из файла
def read_matrix_from_file(filename):
    return np.loadtxt(filename, dtype=int)

# Генерация матрицы
def generate_matrix(size, start_value):
    return np.arange(start_value, start_value + size*size).reshape(size, size)

# Ввод имени файла и чтение матрицы B
filename = input("Введите имя файла для матрицы B: ")
B = read_matrix_from_file(filename)

# Генерация матриц C, D, E
C = generate_matrix(size, 10)
D = generate_matrix(size, 50)
E = generate_matrix(size, 100)

# Проверка размеров
if B.shape != (size, size):
    raise ValueError("Матрица B должна иметь размер (N/2, N/2)!")

# Создание матрицы A
A = np.block([[B, E], [C, D]])

# Копирование A в F
F = A.copy()

# Проверка симметрии относительно побочной диагонали
if np.allclose(A, np.fliplr(np.flipud(A))):  # Если симметрична
    B, D = D, B  # Меняем местами B и D
else:
    D, E = E, D  # Иначе меняем местами D и E

# Расчет выражений в зависимости от определителя и суммы диагональных элементов
det_A = np.linalg.det(A)
diag_sum_F = np.trace(F)

if det_A > diag_sum_F:
    result_matrix = np.linalg.inv(A).T @ A - K * np.linalg.inv(F)
else:
    G = np.tril(A)  # Нижняя треугольная матрица
    result_matrix = (A.T + G - F.T) * K

# Вывод матрицы результата
print("\nРезультирующая матрица:")
print(result_matrix)

# Построение графиков
plt.figure(figsize=(10, 6))

# График матрицы A
plt.subplot(1, 3, 1)
plt.imshow(A, cmap='viridis')
plt.title('Матрица A')
plt.colorbar()

# График матрицы F
plt.subplot(1, 3, 2)
plt.imshow(F, cmap='plasma')
plt.title('Матрица F')
plt.colorbar()

# График результирующей матрицы
plt.subplot(1, 3, 3)
plt.imshow(result_matrix, cmap='inferno')
plt.title('Результирующая матрица')
plt.colorbar()

plt.tight_layout()
plt.show()
