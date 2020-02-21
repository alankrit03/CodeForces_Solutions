n = int(input())

arr = [int(x) for x in input().split()]

res = 0

cur_high = arr[0]
i = 1
cur_min = arr[0]
while i < n:
    if arr[i] >= arr[i - 1]:
        res += cur_high - cur_min
        cur_high = arr[i]
        cur_min = arr[i]

    else:
        if cur_min > arr[i]:
            cur_min = arr[i]
    i += 1
res += cur_high - cur_min
print(res)