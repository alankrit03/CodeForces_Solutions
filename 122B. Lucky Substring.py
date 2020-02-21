s = input()
n = len(s)

count_4 = 0
count_7 = 0

for i in range(n):
    if s[i] == '4':
        count_4 += 1
    if s[i] == '7':
        count_7 += 1

if count_4 == 0 and count_7 == 0:
    print(-1)
elif count_7 > count_4:
    print(7)
else:
    print(4)