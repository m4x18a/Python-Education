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