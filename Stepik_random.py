# Напишите программу, которая с помощью модуля random генерирует случайный пароль. Программа принимает на вход длину пароля и выводит случайный пароль, содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).

import random

length = int(input()) # длина пароля
for i in range(length):
    if random.randint(0, 1) == 1:
        print(chr(65 + random.randint(0, 25)), end='')
    else:
        print(chr(97 + random.randint(0, 25)), end='')

"""Лотерейный билет содержит 777 чисел из диапазона от 111 до 494949 (включительно).
Напишите программу, которая с помощью модуля random генерирует 777 различных случайных чисел для лотерейного билета. 
Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела.
Убедитесь, что сгенерированные числа не содержат дубликатов."""

import random
a = []
b = []
while len(b) != 7:
    a.append(random.randint(1, 49))
    b = set(a)
print(*sorted(b))

# Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.

def generate_ip():
    import random
    return(str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.'+ str(random.randint(0, 255)))

"""Напишите функцию generate_index(), которая с помощью модуля random, 
генерирует и возвращает случайный корректный почтовый индекс Латверии. 
Пример правильного (неправильного) индекса Латверии:AB23_56VG"""

def generate_index():
    import random, string
    L = string.ascii_uppercase
    N = string.digits
    return(random.choice(L) + random.choice(L) + random.choice(N) + random.choice(N) + '_' + random.choice(N) + random.choice(N) + random.choice(L) + random.choice(L))

"""Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью системы неравенств:
{−2≤x≤2; −2≤y≤2; x^3+y^4+2≥0; 3x+y^2≤2}"""

import random
n = 10**6       # количество испытаний
k = 0
s0 = 16
for _ in range(n):
    x = random.randint(-2, 2)
    y = random.randint(-2, 2)
    if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2:
        k += 1
print((k/n)*s0)