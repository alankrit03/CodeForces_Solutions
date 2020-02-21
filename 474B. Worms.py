def get_dorm(x):
    l = 0
    h = len(room)

    while (h - l > 1):
        m = (l + h) // 2

        if room[m] >= x:
            h = m
        else:
            l = m

    return h


n = int(input())
room = input().split()

q = int(input())
query = [int(x) for x in input().split()]

for i in range(n):
    room[i] = int(room[i])
    if i:
        room[i] = room[i] + room[i - 1]
room.insert(0, 0)

for x in query:
    dorm = get_dorm(x)
    print(dorm)
