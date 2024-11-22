"""
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N) заполняется случайным образом целыми числами в интервале [-10,10]. 
Для тестирования использовать не случайное заполнение, а целенаправленное, введенное из файла. Условно матрица имеет вид:

  2
1   3
  4



Библиотечными методами (NumPy) пользоваться нельзя.

Вариант 6:

6.	Формируется матрица F следующим образом: Скопировать в нее матрицу А и если количество нулевых элементов в нечетных столбцах в области 4 больше, чем количество нулевых элементов в четных столбцах в области 1,
то поменять симметрично области 2 и 3 местами, иначе 1 и 2 поменять местами несимметрично.
При этом матрица А не меняется. После чего вычисляется выражение: ((F*A)– (K * AT). Выводятся по мере формирования А, F и все матричные операции последовательно.

"""




import random

# Функция для чтения матрицы из файла
def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

# Функция для формирования пустой матрицы N x N
def create_empty_matrix(N):
    return [[0] * N for _ in range(N)]

# Функция для проверки количества нулей в заданной области
def count_zeros_in_area(matrix, N, area):
    zeros = 0
    for i in range(N):
        for j in range(N):
            if area(i, j, N) and matrix[i][j] == 0:
                zeros += 1
    return zeros

# Условие для области 1 (левый треугольник)
def area_1(i, j, N):
    return i >= j

# Условие для области 2 (верхний треугольник)
def area_2(i, j, N):
    return i <= j

# Условие для области 3 (правый треугольник)
def area_3(i, j, N):
    return i + j >= N - 1

# Условие для области 4 (нижний треугольник)
def area_4(i, j, N):
    return i + j <= N - 1

# Функция для транспонирования матрицы
def transpose(matrix, N):
    transposed = create_empty_matrix(N)
    for i in range(N):
        for j in range(N):
            transposed[j][i] = matrix[i][j]
    return transposed

# Умножение двух матриц
def multiply_matrices(matrix1, matrix2, N):
    result = create_empty_matrix(N)
    for i in range(N):
        for j in range(N):
            result[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(N))
    return result

# Вычитание матриц
def subtract_matrices(matrix1, matrix2, N):
    result = create_empty_matrix(N)
    for i in range(N):
        for j in range(N):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    return result

# Основная программа
def main():
    # Ввод размерности и числа K
    K = int(input("Введите число K: "))
    N = int(input("Введите размерность матрицы N: "))

    # Чтение матрицы A из файла
    filename = input("Введите имя файла с матрицей A: ")
    A = read_matrix_from_file(filename)

    print("Матрица A:")
    for row in A:
        print(row)

    # Создание матрицы F
    F = [row[:] for row in A]

    # Подсчет нулей в нечетных столбцах области 4
    zeros_area_4 = sum(
        1 for j in range(0, N, 2) for i in range(N) if area_4(i, j, N) and A[i][j] == 0
    )

    # Подсчет нулей в четных столбцах области 1
    zeros_area_1 = sum(
        1 for j in range(1, N, 2) for i in range(N) if area_1(i, j, N) and A[i][j] == 0
    )

    # Замена областей в зависимости от условий
    if zeros_area_4 > zeros_area_1:
        # Симметричная замена областей 2 и 3
        for i in range(N):
            for j in range(N):
                if area_2(i, j, N) and area_3(i, j, N):
                    F[i][j], F[N-1-i][N-1-j] = F[N-1-i][N-1-j], F[i][j]
    else:
        # Несимметричная замена областей 1 и 2
        for i in range(N):
            for j in range(N):
                if area_1(i, j, N):
                    F[i][j], F[j][i] = F[j][i], F[i][j]

    print("Матрица F:")
    for row in F:
        print(row)

    # Вычисление ((F * A) - (K * AT))
    FA = multiply_matrices(F, A, N)
    AT = transpose(A, N)
    KAT = [[K * AT[i][j] for j in range(N)] for i in range(N)]
    result = subtract_matrices(FA, KAT, N)

    print("Результат ((F * A) - (K * AT)):")
    for row in result:
        print(row)

if __name__ == "__main__":
    main()

    print(row)

