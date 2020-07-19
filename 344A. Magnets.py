n = int(input())
groups = 1
prev = input()[1]
for i in range(n-1):
    mag = input()
    if prev==mag[0]:
        groups+=1
    prev = mag[1]

print(groups)