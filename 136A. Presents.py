n = int(input())

data = input().split()
dict_ = {}

for i in range(n):
    data[i] = int(data[i])

for i in range(n):
    print(data.index(i + 1) + 1, end=' ')
