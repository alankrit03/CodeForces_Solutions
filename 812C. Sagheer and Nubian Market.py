def give_cost(sov):
    temp = [0] * n
    c = 0
    for i in range(n):
        temp[i] = arr[i] + (i + 1) * m
    temp.sort()
    for i in range(m):
        c += temp[i]

    return c


n, cost = map(int, input().split())

arr = [int(x) for x in input().split()]

l = 0
h = n + 1
final_cost = 0
while (h - l > 1):
    m = (l + h) // 2
    c = give_cost(m)

    if c <= cost:
        final_cost = c
        l = m
    else:
        h = m

print(l, final_cost)