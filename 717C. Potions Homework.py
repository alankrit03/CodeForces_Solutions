"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
INPUT : 2 1 3
OUTPUT: 6
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

arr.sort()
total = 0


for i in range(n):
    total += (arr[i]*arr[n-i-1])
    total = total%10007
print(total)