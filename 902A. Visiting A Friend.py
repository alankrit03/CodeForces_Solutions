## Taking advantage of the ultra small bounds.

n, m = map(int, input().split())

arr = [0] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))

if arr[0][0]:
    limit = -1
else:
    limit = arr[0][1]
    for i in range(1, n):
        if limit >= arr[i][0]:
            limit = max(limit, arr[i][1])
        else:
            break

if limit >= m:
    print('YES')
else:
    print('NO')
