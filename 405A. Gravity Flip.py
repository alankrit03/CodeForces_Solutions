n = int(input())
arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])
print(*sorted(arr))