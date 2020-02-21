n = int(input())

data = input().split()
count_odd = 0
count_even = 0
for i in range(n):
    data[i] = int(data[i])
    if data[i] % 2 == 0:
        count_even += 1
        if count_even == 1:
            res_even = data[i]

    else:
        count_odd += 1
        if count_odd == 1:
            res_odd = data[i]

if count_even > count_odd:
    print(data.index(res_odd) + 1)
else:
    print(data.index(res_even) + 1)