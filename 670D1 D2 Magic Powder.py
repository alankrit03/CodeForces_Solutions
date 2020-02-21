def check_cookie(x):
    m = 0
    for i in range(n):
        if a[i] * x > b[i]:
            m += a[i] * x - b[i]
    if m > k:
        return False

    return True


n, k = map(int, input().split())

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

l = 0
h = 200000000001

while (h - l > 1):
    m = (l + h) // 2

    if check_cookie(m):
        l = m
    else:
        h = m

print(l)