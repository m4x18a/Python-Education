# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).

a = float(input())
if a == 0:
    print('Обратного числа не существует')
else:
    b = 1 / a
    print(b)
    
# На вход программе подается число nn – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в человеческих годах. В течение первых двух лет собачий год равен 10.510.5 человеческим годам. После этого каждый год собаки равен 4 человеческим годам.

dog_age = float(input())
if dog_age <= 2:
    human_age = dog_age * 10.5
else:
    human_age = (dog_age - 2) * 4 + 21
print(human_age)

# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

a = float(input())
b = int((a - int(a)) * 10)
print(b)

# Напишите программу, которая упорядочивает три числа от большего к меньшему.

a, b, c = int(input()), int(input()), int(input())
maximum = max(a, b, c)
minimum = min(a, b, c)
print(maximum)
print(a + b + c - maximum - minimum)
print(minimum)

# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре. Напишите программу, которая определяет интересное число или нет. Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».

a = int(input())
a1 = a // 100
a2 = (a % 100) // 10
a3 = a % 10
if max(a1, a2, a3) - min(a1, a2, a3) == a1 + a2 + a3 - max(a1, a2, a3) - min(a1, a2, a3):
    print('Число интересное')
else:
    print('Число неинтересное')

# На плоскости евклидово расстояние между двумя точками

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
p = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print(p)

# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу RR.

import math
r = float(input())
s = math.pi * math.pow(r, 2)
c = 2 * math.pi * r
print(s, c, sep='\n')

# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

import math
a, b = float(input()), float(input())
print((a + b) / 2)
print(math.sqrt(a * b))
print((2 * a * b) / (a + b))
print(math.sqrt((math.pow(a, 2) + math.pow(b, 2)) / 2))

# Напишите программу, вычисляющую значение ⌈x⌉ +⌊x⌋ по заданному вещественному числу x.

from math import floor, ceil
x = float(input())
print(floor(x) + ceil(x))

# Даны три вещественных числа aa, bb, cc. Напишите программу, которая находит вещественные корни квадратного уравнения 

from math import sqrt
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep='\n')
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Нет корней')

# Даны два числа: натуральное число nn и вещественное число aa. Напишите программу, которая находит площадь указанного правильного многоугольника.

from math import pi, tan
n, a = int(input()), float(input())
s = (n * a ** 2) / (4 * tan(pi / n))
print(s)

#Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу: «Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».

team_name = input()
print('Футбольная команда ' + team_name + ' имеет длину ' + str(len(team_name)) + ' символов')

# Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.

a, b, c = len(input()), len(input()), len(input())
maximum = max(a, b, c)
minimum = min(a, b, c)
if a + b + c == maximum + minimum + ((maximum - minimum) / 2 + minimum):
    print('YES')
else:
    print('NO')

# Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.

a = input()
if 'синий' in a:
    print('YES')
else:
    print('NO')

# Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.

a = input()
if '@' in a and '.' in a:
    print('YES')
else:
    print('NO')


# STRING

# На вход программе подается натуральное число, записанное в десятичной системе счисления. Напишите программу, которая переводит данное число в двоичную систему счисления.

n = int(input())
binary = str()
while n > 0:
    binary = str(n % 2) + binary
    n //= 2
print(binary)

# На вход программе подается одно слово, записанное в нижнем регистре. Напишите программу, которая определяет является ли оно палиндромом.

s = input()
if s == s[::-1]:
    print('YES')
else:
    print('NO')На вход программе подается одно слово, записанное в нижнем регистре. Напишите программу, которая определяет является ли оно палиндромом.

# На вход программе подается строка текста. Напишите программу, которая разрежет ее на две равные части, переставит их местами и выведет на экран.

s = input()
q = len(s) // 2
if len(s) % 2 != 0:
    print(s[q + 1:] + s[:q + 1])
else:
    print(s[q:] + s[:q])

# На вход программе подаются два числа a и b. Напишите программу, которая для каждого кодового значения в диапазоне от a до b (включительно), выводит соответствующий ему символ из таблицы символов Unicode.

a, b = int(input()), int(input())
for i in range(a, b + 1):
    print(chr(i), end=' ')

# Напишите программу для декодирования шифра Цезаря.

a, s = int(input()), input()
for c in s:
    num = ord(c) - a
    if num > 122:
        num = num - 26
    elif num < 97:
        num = num + 26
    print(chr(num), end='')

# На вход программе подается строка текста. Напишите программу, которая удаляет из нее все символы с индексами кратными 3

s = input()
for i in range(len(s)):
    if i % 3 != 0:
        print(s[i], end='')

# На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f». Если буква «f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.

s = input()
count = 0
for i in range(len(s)):
    if s[i] == 'f':
        count += 1
        if count == 2:
            print(i)
            break
if count == 1:
    print(-1)
elif count == 0:
    print(-2)
    
# На вход программе подается строка текста в которой буква «h» встречается как минимум два раза. Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов, заключенную между первым и последним вхождением буквы «h».

s = input()
print(s[:s.find('h')] + s[s.rfind('h'):s.find('h'):-1] + s[s.rfind('h'):])

# Decimal числа, разделенные символом пробела, хранятся в строковой переменной s. Дополните приведенный код, чтобы он вывел на первой строке сумму всех чисел, а на второй строке 5 самых больших чисел в порядке убывания, разделенных символом пробела.

s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
from decimal import *

a =[Decimal(str(i)) for i in s.split()]
print(sum(a))
print(*sorted(a, reverse=True)[:5])

# Десятичные числа хранятся в списке numbers в виде строк. Дополните приведенный код, чтобы он для каждого десятичного числа вывел его представление в виде обыкновенной дроби в формате: десятичное число = обыкновенная дробь

from fractions import Fraction

numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
for num in numbers:
    print(num, '=', Fraction(num))

# Десятичные числа разделенные символом пробела хранятся в строковой переменной s. Дополните приведенный код, чтобы он вывел сумму наибольшего и наименьшего числа в виде обыкновенной дроби.

from fractions import Fraction

s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
list1 = s.split()
for i in range(len(list1)):
    list1[i] = Fraction(str((list1[i])))
print(((max(list1) + min(list1))))

# На вход программе подается натуральное число n. Напишите программу, которая вычисляет и выводит рациональное число, равное сумме элементов ряда обратных квадратов от 1/(1^2) до 1/(n^2).

from fractions import Fraction as F
n = int(input())
total = 0
for i in range(1, n + 1):
    num = F(1, i**2)
    total += num
print(F(total))

# На вход программе подается натуральное число n. Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения 1/(1!) + ... + 1/(n!)

import math
from fractions import Fraction as F

n = int(input())

total = 0
for i in range(1, n + 1):
    num = F(1, math.factorial(i))
    total += num
print(F(total))

# На вход программе подается натуральное число n. Напишите программу, которая выводит в порядке возрастания все несократимые дроби, заключённые между 0 и 1, знаменатель которых не превосходит n.

from fractions import Fraction
import math

n = int(input())
ans = set()

for k in range(1, n+1):
    for i in range(1, n):
        a = (Fraction(str(i) + '/' + str(k)))
        if a < 1:
            ans.add(a)

list1 = sorted(ans)
print(*list1, sep='\n')

# Комплексные числа хранятся в списке numbers. Дополните приведенный код так, чтобы он вывел комплексное число с наибольшим модулем и сам модуль числа на отдельных строках.

numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
z_max = complex(numbers[0])
max_abs = abs(z_max)

for z in numbers:
    if abs(complex(z)) > max_abs:
        z_max = complex(z)
        max_abs = abs(z_max)
print(z_max, max_abs, sep='\n')

# Дано натуральное число n и два комплексных числа z1, z2. Вычислите:

n, z1, z2 = int(input()), complex(input()), complex(input())
ans = z1**n + z2**n + z1.conjugate()**n + z2.conjugate()**(n+1)
print(ans)