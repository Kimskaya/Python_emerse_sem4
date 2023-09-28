'''Напишите функцию для транспонирования матрицы.
Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]'''

def transposition(M):
    '''Функция транспонирует матрицу M'''
    result = []
    for i in range(len(M[1])):
        L = []
        for j in range(len(M)):
            L.append(M[j][i])
        result.append(L)
    return result

def input_matr(rows,cols):
    '''Функция вводит матрицу, rows - количество строк, cols - количество столбцов'''
    result = []
    for i in range(rows):
        print(f'Введите {i+1}-ую строку матрицы ({cols} чисел в строку через пробел):')
        result.append([int(x) for x in input().split()])
    return result

def print_matr(M,width_col=4):
    '''Функция выводит на экран матрицу M (двумерный масссив)
    width_col - ширина столбца'''
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(str(M[i][j]).rjust(width_col),end='')
        print()

m = int(input('Количество строк в матрице: '))
n = int(input('Количество столбцов в матрице: '))
Mmxn = input_matr(m,n)      #Ввод исходной матрицы
print('Исходная матрица:')
print_matr(Mmxn)            #Вывод исходной матрицы
print('Транспонированная матрица:')
print_matr(transposition(Mmxn))     #Вывод транспонированной матрицы