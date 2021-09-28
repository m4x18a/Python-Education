# Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы

n, m = int(input()), int(input())
arr = [[0] * m for c in range(n)]
for i in range(n):
    for j in range(m):
        arr[i][j] = input()
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()    

# На вход программе подаются два натуральных числа n и m. Напишите программу для создания матрицы размером n × m, заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами

size = [int(num) for num in input().split()]
arr = []
for i in range(size[0]):
    temp = []
    for j in range(size[1]):
        if i + j == 0:
            temp.append('.')
        elif (i + j) % 2 != 0:
            temp.append('*')
        else:
            temp.append('.')
    arr.append(temp)
for i in range(size[0]):
    for j in range(size[1]):
        print(arr[i][j], end=' ')
    print()
    
""" На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n × n и заполняет её по следующему правилу:
числа на побочной диагонали равны 1;
числа, стоящие выше этой диагонали, равны 0;
числа, стоящие ниже этой диагонали, равны 2.
Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом"""

n = int(input())
arr = []
for i in range(n):
    temp = []
    for j in range(n):
        if i < n - 1 - j:
            temp.append(0)
        elif i == n - 1 - j:
            temp.append(1)
        else:
            temp.append(2)
    arr.append(temp)
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()


# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n × m и заполняет её числами от 1 до n * m в соответствии с образцом

size = [int(num) for num in input().split()]
arr = []
count = 1
for i in range(size[0]):
    temp = []
    for j in range(size[1]):
        temp.append(count)
        count += 1
    arr.append(temp)
for i in range(size[0]):
    for j in range(size[1]):
        print(str(arr[i][j]).ljust(3), end=' ')
    print()
    
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n × m заполнив её в соответствии с образцом

size = [int(num) for num in input().split()]
arr = []
for i in range(size[0]):
    temp = []
    count = 0
    for j in range(size[1]):
        temp.append(i + 1 + count)
        count += size[0]
    arr.append(temp)
for i in range(size[0]):
    for j in range(size[1]):
        print(str(arr[i][j]).ljust(3), end=' ')
    print() 

# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n × m заполнив её в соответствии с образцом

n = int(input())
arr = []
for i in range(n):
    temp = []
    for j in range(n):
        if i == j or i == n - 1 - j:
            temp.append(1)
        else:
            temp.append(0)
    arr.append(temp)
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
    
# Напишите программу для вычисления суммы двух матриц

size = [int(num) for num in input().split()]
arr1 = []
arr2 = []
arr_result = []
for i in range(size[0]):
    temp = [int(num) for num in input().split()]
    arr1.append(temp)
input()
for i in range(size[0]):
    temp = [int(num) for num in input().split()]
    arr2.append(temp)
for i in range(size[0]):
    temp = []
    for j in range(size[1]):
        temp.append(arr1[i][j] + arr2[i][j])
    arr_result.append(temp)
for i in range(size[0]):
    for j in range(size[1]):
        print(arr_result[i][j], end=' ')
    print()

# Напишите программу, которая перемножает две матрицы

import numpy as np
arr1 = []
arr2 = []
arr_mult = []

size1 = [int(num) for num in input().split()]
for i in range(size1[0]):
    temp = [int(num) for num in input().split()]
    arr1.append(temp)
    
input()

size2 = [int(num) for num in input().split()]
for i in range(size2[0]):
    temp = [int(num) for num in input().split()]
    arr2.append(temp)
    

matrix1 = np.array(arr1)
matrix2 = np.array(arr2)
total = matrix1.dot(matrix2)
    
for i in range(size1[0]):
    for j in range(size2[1]):
        print(total[i][j], end=' ')
    print()

# Напишите программу, которая возводит квадратную матрицу в m-ую степень

import numpy as np
n = int(input())
arr = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    arr.append(temp)
m = int(input())

arr = np.array(arr)
result = np.linalg.matrix_power(arr, m)

for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()










































