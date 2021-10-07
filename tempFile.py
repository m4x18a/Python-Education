n = int(input())
list1 = [[input().split()[1] for _ in range(int(input()))] for _ in range(n)]
list2 = list(map(lambda l: '5' in l, list1))
print('YES' if all(list2) else 'NO')
