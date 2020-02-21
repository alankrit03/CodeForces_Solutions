n , k = map(int,input().split())

data = list(input())

for i in range(k):
    j=0
    while j <n-1:
        if data[j] == 'B' and data[j+1] == 'G':
            data[j],data[j+1]=data[j+1],data[j]
            j+=1
        j+=1

print(*data,sep='') 