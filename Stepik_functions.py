# Напишите функцию draw_triangle(fill, base), которая принимает два параметра: fill – символ заполнитель; base – величина основания равнобедренного треугольника; а затем выводит его.

def draw_triangle(fill, base):
    for i in range((base + 1) // 2):
        print(fill * (i + 1))
    for j in range(base // 2, 0, -1):
        print(fill * j)


fill = input()
base = int(input())
draw_triangle(fill, base)

# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра: name – имя человека; surname – фамилия человека; patronymic – отчество человека; а затем выводит на печать ФИО человека.

def print_fio(name, surname, patronymic):
    print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')


name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)

# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

def print_digit_sum(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
    print(sum)


n = int(input())
print_digit_sum(n)

# Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.

def find_all(target, symbol):
    list_index = []
    a = 0
    for i in range(len(target)):
        if target[i] == symbol:
            list_index.append(i)
    return list_index
        

s = input()
char = input()
print(find_all(s, char))

# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True если число является простым и False в противном случае.

def is_prime(num): # объявление функции
    count = 0
    for i in range (1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


n = int(input()) # считываем данные
print(is_prime(n)) # вызываем функцию

# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.


def get_next_prime(num): # объявление функции
    for i in range(num + 1, num * 2 + 1):
        count = 0
        for k in range(1, i + 1):
            if i % k == 0:
                count += 1
        if count == 2:
            return i


n = int(input()) # считываем данные
print(get_next_prime(n)) # вызываем функцию

# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.

def is_one_away(a, b):
    count = 0
    if len(a) != len(b):
        return False
    if a == b:
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
        if count > 1:
            return False
    return True

txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))

# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True если указанный текст является палиндромом и False в противном случае.

def is_palindrome(text):
    text = text.lower()
    a = []
    b = []
    for c in text:
        if c in 'abcdefghyjklmnopqrstuvwxyz' or c in 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя':
            a.append(c)
    b = a[::-1]
    if a == b:
        return True
    else:
        return False


txt = input()

print(is_palindrome(txt))

"""Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. 
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password 
и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае."""

def is_valid_password(password):
    list_a = []
    count = 0
    abc = password.split(':')
    if len(abc) != 3:
        return False
    a = abc[0]
    b = int(abc[1])
    c = int(abc[2])
    if a != a[::-1]:
        return False
    for i in range(1, b + 1):
        if b % i == 0:
            count += 1
        if count > 2:
            return False   
    if c % 2 != 0:
        return False
    return True
        

psw = input()

print(is_valid_password(psw))

"""Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, 
состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной 
последовательностью и False в противном случае."""

def is_correct_bracket(text):
    count = 0
    for c in text:
        if c not in '()':
            return False
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False
    if count > 0:
        return False
    return True

txt = input()

print(is_correct_bracket(txt))

# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

def convert_to_python_case(text):
    a = []
    a.append(text[0].lower())
    text = text[1:]
    for c in text:
        if c.isupper() is True:
            a.append('_' + c.lower())
        else:
            a.append(c)
    return a


txt = input()

print(*convert_to_python_case(txt), sep='')

# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты квадратного уравнения ax^2+bx+c=0 и возвращает его корни в порядке возрастания.

def solve(a, b, c):
    from math import sqrt
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        if x1 > x2:
            x1, x2 = x2, x1
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x, x


a, b, c = float(input()), float(input()), float(input())

x1, x2 = solve(a, b, c)
print(x1, x2)

# Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num и возвращает его словесное описание на русском языке. Считайте, что число 1 ≤ num ≤ 99.

def number_to_words(num):
    se = ['','один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
          'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
          'девятнадцать']
    sd = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num < 20:
      return se[num]
    elif num < 100:
      return (sd[num // 10] + ' ' + se[num % 10])

n = int(input())

print(number_to_words(n))

"""print(matrix())                   # матрица 1 × 1 из 0
   print(matrix(3))                  # матрица 3 × 3 из 0
   print(matrix(2, 5))               # матрица 2 × 5 из 0
   print(matrix(3, 4, 9))            # матрица 3 × 4 из 9"""

def matrix(n=1, m=0, value=0):
    if m == 0:
        m = n
    return [[value for i in range(m)] for i in range(n)]

# Напишите функцию mean(), которая принимает произвольное количество аргументов и возвращает среднее арифметическое переданных в нее числовых (int или float) аргументов.

def mean(*args):
    quantity = 0
    total = 0
    for c in args:
        if type(c)==int or type(c) == float:
            quantity += 1
            total += c
    return total / quantity

# Напишите функцию print_products(), которая принимает произвольное количество аргументов и выводит список продуктов. Если среди переданных аргументов нет ни одного продукта, необходимо вывести текст Нет продуктов.

def print_products(*args):
    count = 1
    for c in args:
        if type(c) == str and len(c) > 0:
            print(count, ') ', c, sep='')
            count += 1

# Дан список numbers, содержащий кортежи чисел. Напишите программу, которая с помощью встроенных функций min() и max() выводит те кортежи (каждый на отдельной строке), которые имеют минимальное и максимальное среднее арифметическое значение элементов.

numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
           (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
           (90, 1, -45, -21)]
def comparator(myturple):\
    return sum(myturple) / len(myturple)
print(min(numbers, key=comparator))
print(max(numbers, key=comparator))

# Напишите программу, которая сортирует список points координат точек плоскости в соответствии с расстоянием от начала координат (точки (0;0)). Программа должна вывести отсортированный список.

points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
def comparator(myTurple):
    return (myTurple[0]**2 + myTurple[1]**2)**0.5
points.sort(key=comparator)
print(points)

# На вход программе подается натуральное число от 1 до 4 – номер поля по которому требуется отсортировать список.

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
def name(myTurple):
    return myTurple[0]

def age(myTurple):
    return myTurple[1]

def height(myTurple):
    return myTurple[2]

def weight(myTurple):
    return myTurple[3]

parameter = [name, age, height, weight]

athletes.sort(key=parameter[int(input())])

for i in range(len(athletes)):
    print(*athletes[i])

# Напишите программу, которая принимает число и название функции, а выводит результат применения функции к данному числу.

import math

def square(x):
    return x**2

def cube(x):
    return x**3

def root(x):
    return math.sqrt(x)

def funcAbs(x):
    return math.fabs(x)

def sin(x):
    return math.sin(x)

func = {'квадрат': square, 'куб': cube, 'корень': root, 'модуль': funcAbs, 'синус': sin}

n = int(input())
print(func[input()](n))

"""Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. 
При этом, если два числа имеют одинаковую сумму цифр, следует сохранить их взаиморасположение в начальном списке."""

def comparator(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum

myList = [int(num) for num in input().split()]

myList.sort(key=comparator)
print(*myList)

"""Напишите программу, которая с помощью функции map() округляет все элементы списка numbers до 2 десятичных знаков, 
а затем выводит их, каждый на отдельной строке."""

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

def fround(num):
    return round(num, 2)

numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
ans = map(fround, numbers)
print(*ans, sep='\n')

"""Напишите программу, которая с помощью функций filter() и map() отбирает из заданного списка numbers трёхзначные числа, 
дающие при делении на 5 остаток 2, и выводит их кубы, каждый в отдельной строке."""

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434,
           1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289,
           1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013,
           898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336,
           1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

def is_dev(num):
    return num % 5 == 2 and num > 99 and num < 1000

def cube(num):
    return num**3

print(*map(cube, filter(is_dev, numbers)), sep='\n')

"""Напишите программу для вычисления и вывода суммы квадратов элементов списка numbers."""

def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc


numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
           11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36,
           72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35,
           7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

def add(x, y):
    return x + y**2

print(reduce(add, numbers, 0))

"""Напишите программу для вычисления и вывода суммы квадратов двузначных чисел, которые делятся на 777 без остатка."""

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270,
           219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35,
           152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5,
           187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35,
           211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2,
           79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234,
           10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]

def is_2_digit(num):
    return abs(num) % 7 == 0 and 9 < abs(num) < 100

def square(num):
    return num**2

print(sum(map(square, filter(is_2_digit, numbers))))

"""Напишите функцию func_apply(), принимающую на вход функцию и список значений и возвращающую список, 
в котором каждое значение будет результатом применения переданной функции к переданному списку."""

def func_apply(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

"""Требовалось написать программу, которая:
преобразует список floats в список чисел, возведенных в квадрат и округленных с точностью до одного десятичного знака;
фильтрует список words  и оставляет только палиндромы длиной более 4 символов;
находит произведение чисел из списка numbers."""

from functools import reduce

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
map_result = list(map(lambda num: round(num**2, 1), floats))
filter_result = list(filter(lambda name: name if name == name[::-1] and len(name) > 4 else False, words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)








































































