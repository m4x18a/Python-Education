from functools import reduce

def evaluate(coefficients, x):
    list1 = [x**i for i in range(len(coefficients) - 1, -1, -1)]
    list2 = list(map(lambda c, l1: c*l1, coefficients, list1))
    return reduce(lambda num1, num2: num1 + num2, list2, 0)


coefficient = [int(c) for c in input().split()]
x = int(input())

print(evaluate(coefficient, x))




