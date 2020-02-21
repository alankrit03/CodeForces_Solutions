n = int(input())

arr = [int(x) for x in input().split()]

res = arr[-1]
i = n - 1
while (i > 1):

    if arr[i - 2] >= arr[i - 1]:
        i = i - 2
    else:
        i -= 1

    res = min(arr[i], res)

res = min(res, arr[0])
print(res)