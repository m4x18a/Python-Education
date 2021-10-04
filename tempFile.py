def matrix(n=1, m=0, value=0):
    if m == 0:
        m = n
    return [[value for i in range(m)] for i in range(n)]

print(matrix(3, 1))