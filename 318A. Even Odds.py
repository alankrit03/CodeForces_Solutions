
n , k = map(int,input().split())

mid = n//2 if n%2==0 else (n//2)+1

if k> mid:
    if n%2==0:
        print(2*k - n)
    else:print(2*k -n -1)
else:
    print(2*k - 1)