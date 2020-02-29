n = int(input())

rooms = 0

for i in range(n):
    present , capacity = map(int , input().split())
    if capacity-present >= 2:
        rooms += 1

print(rooms)