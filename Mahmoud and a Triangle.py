def is_triangle_possible(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

n=int(input())

arr=[int(x) for x in input().split()]

arr.sort()
i=n-1
while(i>1):
    if is_triangle_possible(arr[i],arr[i-1],arr[i-2]):
        print('YES')
        break
    i-=1
else:
    print('NO')