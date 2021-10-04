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

"""Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
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
состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной последовательностью и False в противном случае."""

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
    se = ['','один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
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
















































































