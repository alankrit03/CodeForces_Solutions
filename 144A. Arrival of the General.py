n = int(input())

arr = [int(x) for x in input().split()]
smallest = 0
largest = 0

for i in range(1,n):
    if arr[i]<=arr[smallest]:
        smallest=i
    if arr[i]>arr[largest]:
        largest = i

total = (n-smallest-1) + largest

if smallest>largest:
    print(total)
else:
    print(total-1)