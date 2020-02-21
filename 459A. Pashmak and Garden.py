x1, y1, x2, y2 = map(int, input().split())

if x1 == x2:
    side = abs(y2 - y1)
    y3 = y1
    y4 = y2
    x3 = x1 + side
    x4 = x2 + side
    print(x3, y3, x4, y4)

elif y1 == y2:
    print(x1, y1 + abs(x2 - x1), x2, y1 + abs(x2 - x1))

elif abs(x1 - x2) == abs(y1 - y2):

    x3 = x1
    y3 = y2
    y4 = y1
    x4 = x2

    print(x3, y3, x4, y4)

else:
    print(-1)