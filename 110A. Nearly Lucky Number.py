number = input()

total = 0

n = len(number)

for i in range(n):
    if number[i] == '4' or number[i] == '7':
        total += 1

if total==4 or total==7:
    print('YES')
else:
    print('NO')