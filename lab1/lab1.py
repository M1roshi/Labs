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




# Функция для чтения матрицы из файла
def read_matrix_from_file(filename, N):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.split()))  # Преобразуем строку в список целых чисел
            matrix.append(row)
    
    # Проверка, что матрица имеет размер NxN
    if len(matrix) != N or any(len(row) != N for row in matrix):
        raise ValueError(f"Неверный размер матрицы в файле. Ожидался размер {N}x{N}.")
    
    return matrix

# Функция для транспонирования матрицы
def transpose_matrix(matrix, N):
    return [[matrix[j][i] for j in range(N)] for i in range(N)]

# Ввод чисел K и N
K = int(input("Введите число K: "))
N = int(input("Введите размерность матрицы N: "))

# Считывание матрицы A из файла
filename = input("Введите имя файла с матрицей: ")
A = read_matrix_from_file(filename, N)

# Вывод матрицы A
print("Матрица A:")
for row in A:
    print(row)

# Функция для подсчета нулей в определенной области
def count_zeros(matrix, cols, rows):
    count = 0
    for i in rows:
        for j in cols:
            if matrix[i][j] == 0:
                count += 1
    return count

# Формирование матрицы F (копируем матрицу A)
F = [row[:] for row in A]

# Области
# Область 1: Верхний левый угол
area_1_rows = range(N//2)
area_1_cols = range(N//2)
# Область 2: Верхний правый угол
area_2_rows = range(N//2)
area_2_cols = range(N//2, N)
# Область 3: Нижний правый угол
area_3_rows = range(N//2, N)
area_3_cols = range(N//2, N)
# Область 4: Нижний левый угол
area_4_rows = range(N//2, N)
area_4_cols = range(N//2)

# Подсчет нулевых элементов
zeros_in_area_4 = count_zeros(A, area_4_cols, [i for i in area_4_rows if i % 2 == 0])
zeros_in_area_1 = count_zeros(A, area_1_cols, [i for i in area_1_rows if i % 2 != 0])

# Замена областей
if zeros_in_area_4 > zeros_in_area_1:
    # Меняем местами области 2 и 3 симметрично
    for i in range(N//2):
        for j in range(N//2, N):
            F[i][j], F[N//2 + i][j] = F[N//2 + i][j], F[i][j]
else:
    # Меняем местами области 1 и 2 нессимметрично
    for i in range(N//2):
        for j in range(N//2):
            F[i][j], F[i][N//2 + j] = F[i][N//2 + j], F[i][j]

# Вывод матрицы F
print("\nМатрица F:")
for row in F:
    print(row)

# Транспонирование матрицы A
A_T = transpose_matrix(A, N)

# Вывод транспонированной матрицы A^T
print("\nТранспонированная матрица A^T:")
for row in A_T:
    print(row)

# Вычисление выражения (F * A) - (K * A^T)
result = [[F[i][j] * A[i][j] - K * A_T[i][j] for j in range(N)] for i in range(N)]

# Вывод результата
print("\nРезультат выражения (F * A) - (K * A^T):")
for row in result:
    print(row)
