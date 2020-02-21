def get_pos(x):
    l = 0
    h = n

    while (h - l > 1):
        m = (l + h) // 2

        if a[m] > x:
            h = m
        else:
            l = m
    return l


n, m = map(int, input().split())

a = input().split()
b = input().split()

for i in range(n):
    a[i] = int(a[i])
for i in range(m):
    b[i] = int(b[i])
a.sort()

for x in b:
    pos = get_pos(x)
    if x < a[0]:
        print(0)
    else:
        print(pos + 1)