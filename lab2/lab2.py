"""
С клавиатуры вводится два числа K и N. Квадратная матрица А(N, N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. 
Для отладки использовать не случайное заполнение, а целенаправленное (ввод из файла и генератором). Вид матрицы А: 
В	Е
С	D
На основе матрицы А формируется матрица F. По матрице F необходимо вывести не менее 3 разных графика. Программа должна использовать функции библиотек numpy и matplotlib

Вариант 6:

6.	Формируется матрица F следующим образом: скопировать в нее А и если А симметрична относительно побочной диагонали, то поменять местами симметрично В и D, иначе D и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A-1*AT – K * F-1, иначе вычисляется выражение (AТ +G-FТ) * K,
где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""



import numpy as np
import matplotlib.pyplot as plt

# Функция для чтения матрицы из файла
def read_matrix_from_file(filename):
    try:
        with open(filename, 'r') as file:
            matrix = [list(map(int, line.split())) for line in file]
        return np.array(matrix)
    except Exception as e:
        print("Ошибка при чтении файла:", e)
        return None

# Функция для проверки симметрии относительно побочной диагонали
def is_anti_diagonal_symmetric(matrix):
    N = matrix.shape[0]
    for i in range(N):
        for j in range(N):
            if matrix[i, j] != matrix[N - j - 1, N - i - 1]:
                return False
    return True

# Основная функция
def main():
    # Ввод значений K и N
    K = int(input("Введите значение K: "))
    N = int(input("Введите размер матрицы N: "))

    # Проверка, что матрица квадратная
    if N <= 0:
        print("Размер матрицы N должен быть положительным.")
        return

    # Загрузка матрицы из файла
    A = read_matrix_from_file('matr.txt')
    if A is None or A.shape != (N, N):
        print("Ошибка: некорректная матрица.")
        return
    
    print("Матрица A:")
    print(A)

    # Определение границ подматриц
    half = N // 2
    B = A[:half, :half]
    E = A[:half, half:] if N % 2 == 0 else A[:half, half+1:]
    C = A[half:, :half]
    D = A[half:, half:] if N % 2 == 0 else A[half:, half+1:]

    # Создание матрицы F как копии матрицы A
    F = np.copy(A)

    # Проверка на симметрию относительно побочной диагонали и перестановка подматриц
    if is_anti_diagonal_symmetric(A):
        # Симметрично меняем подматрицы B и D
        F[:half, :half] = D[:half, :half]
        F[half:, half:] = B
    else:
        # Несимметрично меняем подматрицы D и E
        if N % 2 == 0:
            F[half:, half:], F[:half, half:] = E, D
        else:
            F[half:, half+1:], F[:half, half+1:] = E, D

    print("Матрица F после перестановки подматриц:")
    print(F)

    # Вычисление определителя A и суммы диагональных элементов F
    det_A = np.linalg.det(A)
    diag_sum_F = np.trace(F)

    print("Определитель матрицы A:", det_A)
    print("Сумма диагональных элементов матрицы F:", diag_sum_F)

    # Вычисление матрицы G - нижней треугольной матрицы из A
    G = np.tril(A)
    print("Нижняя треугольная матрица G из A:")
    print(G)

    # Проверка условия и выполнение соответствующего выражения
    try:
        if det_A > diag_sum_F:
            # A^-1 * A^T – K * F^-1
            result = np.linalg.inv(A).dot(A.T) - K * np.linalg.inv(F)
            print("Результат выражения A^-1 * A^T – K * F^-1:")
        else:
            # (A^T + G - F^T) * K
            result = (A.T + G - F.T) * K
            print("Результат выражения (A^T + G - F^T) * K:")
        
        print(result)

    except np.linalg.LinAlgError:
        print("Ошибка: невозможно вычислить обратную матрицу, возможно, матрица F или A вырождена.")

    # Построение графиков
    plt.figure(figsize=(15, 5))

    # График 1 - Исходная матрица A
    plt.subplot(1, 3, 1)
    plt.imshow(A, cmap='viridis', interpolation='none')
    plt.colorbar()
    plt.title("Матрица A")

    # График 2 - Модифицированная матрица F
    plt.subplot(1, 3, 2)
    plt.imshow(F, cmap='plasma', interpolation='none')
    plt.colorbar()
    plt.title("Матрица F")

    # График 3 - Результат вычисления
    plt.subplot(1, 3, 3)
    plt.imshow(result, cmap='inferno', interpolation='none')
    plt.colorbar()
    plt.title("Результат выражения")

    plt.show()

# Запуск программы
if __name__ == "__main__":
    main()
