# Дано натуральное число n (n <= 9). Напишите программу, которая печатает таблицу размером n × 3 состоящую из данного числа (числа отделены одним пробелом).

n = int(input())
for i in range(n):
    for i in range(3):
        print(n, end=' ')
    print()
    
# Дано натуральное число n (n <= 9). Напишите программу, которая печатает таблицу размером n × 5, где в i-ой строке указано число i (числа отделены одним пробелом).

n = int(input())
for i in range(n):
    a = i + 1
    for i in range(5):
        print(a, end=' ')
    print()

# Дано натуральное число n (n <= 9). Напишите программу, которая печатает таблицу сложения для всех чисел от 1 до n в соответствии с примером.

n = int(input())
for i in range(1, n + 1):
    for k in range(1, 10):
        print(i, '+', k, '=', i + k)
    print()
    
# Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным n.

n = int(input())
for i in range(n // 2 + 1):
    for k in range(i + 1):
        print('*', end='')
    print()
for l in range(n // 2, 0, -1):
    for m in range(l):
        print('*', end='')
    print()
    
# Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, если плата за быка – 10 рублей, за корову – 5 рублей, за теленка – 0.5 рубля и надо купить 100 голов скота?

for bull in range(1, 11):
    for cow in range(1, 21):
        for calf in range(1, 201):
            if 10 * bull + 5 * cow + 0.5 * calf == bull + cow + calf == 100:
                print(bull, cow, calf)

"""Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной nn, в соответствии с примером:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21"""

n = int(input())
count = 0
for i in range(1, n + 1):
    for k in range(i):
        count += 1
        print(count, end=' ')
    print()

"""Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной nn, в соответствии с примером:
1
121
12321
1234321
123454321
..."""

n = int(input())
for i in range(1, n + 1):
    count = 1
    flag = True
    for k in range(1, i * 2):
        print(count, end='')
        if flag == True:
            count += 1
        else:
            count -= 1
        if count == i:
            flag = False
        elif count == 1:
            flag = True
    print()
    
# На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит натуральное число из отрезка [a; b] с максимальной суммой делителей. Если таких чисел несколько, то выведите наибольшее из них.

a, b = int(input()), int(input())
x = 0
sum_x = 0
for i in range (a, b + 1):
    sum_i = 0
    for k in range(1, b + 1):
        if i % k == 0:
            sum_i += k
    if sum_i >= sum_x:
        x = i
        sum_x = sum_i
print(x, sum_x)

# На вход программе подается натуральное число n. Напишите программу, выводящую графическое изображение делимости чисел от 1 до n включительно. В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.

n = int(input())
for i in range(1, n + 1):
    count = 0
    for k in range(1, i + 1):На вход программе подается два натуральных числа aa и bb (a < ba< b). Напишите программу, которая находит все простые числа от aa до bb включительно.
        if i % k == 0:
            count += 1
    print(i, '+' * count, sep='')

# На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит все простые числа от a до b включительно.

a, b = int(input()), int(input())
flag = True
for i in range(a, b + 1):
    for k in range(2, i):
        if i % k == 0:
            flag = False
            break
    if flag == True and i != 1:
        print(i)
    flag = True

"""Сриниваса Рамануджан – индийский математик, славившийся своей интуицией в области чисел. Когда английский математик Годфри Харди навестил его однажды в больнице, он обмолвился, что номером такси, на котором он приехал, было 17291729, такое скучное и заурядное число. На что Рамануджан ответил: "Нет, нет! Это очень интересное число. Это наименьшее число, выражаемое как сумма двух кубов двумя разными способами". Другими словами:
1729 = 1^3 + 12^3 = 9^3 + 10^3.
Напишите программу, которая находит аналогичные интересные числа. В ответе запишите первые 5 чисел в порядке возрастания, включая число 1729."""

maximum = 34
for a in range(1, maximum):
    for b in range(1, a):
        for c in range(b, a):
            for d in range(b, c):
                if a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != b and a != c and a != d and b != c and b != d and c != d:
                    print(a ** 3 + b ** 3)
