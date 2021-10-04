from datetime import datetime

fib1 = fib2 = 1

n = int(input())
ans = [0, 1, 1]
print(datetime.utcnow())
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    ans.append(fib2)
print(datetime.utcnow())
print(len(ans))