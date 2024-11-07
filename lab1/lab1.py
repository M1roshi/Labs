"""
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N) заполняется случайным образом целыми числами в интервале [-10,10]. 
Для тестирования использовать не случайное заполнение, а целенаправленное, введенное из файла. Условно матрица имеет вид:

1 2
3 4


Библиотечными методами (NumPy) пользоваться нельзя.

Вариант 6:

6.	Формируется матрица F следующим образом: Скопировать в нее матрицу А и если количество нулевых элементов в нечетных столбцах в области 4 больше, чем количество нулевых элементов в четных столбцах в области 1,
то поменять симметрично области 2 и 3 местами, иначе 1 и 2 поменять местами несимметрично.
При этом матрица А не меняется. После чего вычисляется выражение: ((F*A)– (K * AT). Выводятся по мере формирования А, F и все матричные операции последовательно.

"""




import random

# Функция для загрузки матрицы из файла
def load_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix

# Запрос на ввод значений для K и N
K = int(input("Введите значение K: "))
N = int(input("Введите размер матрицы N (NxN): "))

# Инициализация матрицы A
A = load_matrix_from_file("matr.txt")

# Вывод начальной матрицы A
print("Матрица A:")
for row in A:
    print(row)

# Копируем матрицу A в матрицу F
F = [row[:] for row in A]  # Глубокое копирование матрицы A

# Функция для подсчета нулевых элементов в заданной области
def count_zeros_in_region(matrix, start_row, end_row, start_col, end_col, col_parity):
    count = 0
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if (j % 2 == col_parity) and matrix[i][j] == 0:
                count += 1
    return count

# Функция для обмена областей в матрице F
def swap_regions(F, region1, region2, symmetric):
    N = len(F)  # Размер матрицы F

    # Определяем границы областей в зависимости от их номера
    def get_region_indices(region):
        indices = []
        if region == 1:  # Область 1: нижний левый треугольник
            for i in range(N):
                for j in range(i):
                    indices.append((i, j))
        elif region == 2:  # Область 2: верхний треугольник
            for i in range(N//2):
                for j in range(i, N-i):
                    indices.append((i, j))
        elif region == 3:  # Область 3: нижний правый треугольник
            for i in range(N):
                for j in range(i+1, N):
                    indices.append((i, j))
        elif region == 4:  # Область 4: весь нижний треугольник
            for i in range(N//2, N):
                for j in range(N - i - 1, i + 1):
                    indices.append((i, j))
        return indices

    # Получаем индексы для областей
    indices1 = get_region_indices(region1)
    indices2 = get_region_indices(region2)
    
    # Если требуется симметричный обмен, зеркально отразим индексы второй области
    if symmetric:
        for (i1, j1), (i2, j2) in zip(indices1, reversed(indices2)):
            F[i1][j1], F[i2][j2] = F[i2][j2], F[i1][j1]
    else:
        for (i1, j1), (i2, j2) in zip(indices1, indices2):
            F[i1][j1], F[i2][j2] = F[i2][j2], F[i1][j1]



# Проверка условия и обмен областей в F
odd_zeros_region4 = count_zeros_in_region(A, N//2, N, N//2, N, 1)  # Нечетные столбцы в области 4
even_zeros_region1 = count_zeros_in_region(A, 0, N//2, 0, N//2, 0)  # Четные столбцы в области 1

if odd_zeros_region4 > even_zeros_region1:
    swap_regions(F, 2, 3, symmetric=True)
else:
    swap_regions(F, 1, 2, symmetric=False)

# Вывод матрицы F после условного обмена
print("\nМатрица F после обмена областей:")
for row in F:
    print(row)

# Вычисление транспонированной матрицы A
A_T = [[A[j][i] for j in range(N)] for i in range(N)]

# Вычисление выражения (F * A) - (K * A^T)
result = [[sum(F[i][k] * A[k][j] for k in range(N)) - K * A_T[i][j] for j in range(N)] for i in range(N)]

# Вывод результата
print("\nРезультат вычисления (F * A) - (K * A^T):")
for row in result:
    print(row)

