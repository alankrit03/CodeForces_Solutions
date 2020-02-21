def get_dorm(x):
    l = 0
    h = len(room)

    while (h - l > 1):
        m = (l + h) // 2

        if room[m] >= x:
            h = m
        else:
            l = m
    # print(f"h={h}, for x={x}")
    return h


n, q = map(int, input().split())

room = input().split()
query = input().split()

for i in range(n):
    room[i] = int(room[i])
    if i:
        room[i] = room[i] + room[i - 1]
room.insert(0, 0)
for i in range(q):
    query[i] = int(query[i])

for x in query:
    dorm = get_dorm(x)
    print(dorm, x - room[dorm - 1])

# print(room)
# print(query)