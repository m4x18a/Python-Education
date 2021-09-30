import random
a = []
b = []
while len(b) != 7:
    a.append(random.randint(1, 49))
    b = set(a)
print(*sorted(b))