n , k = map(int ,input().split())

while k:
    digit = n%10
    if digit >= k:
        n -=k
        k -=k
    else:
        n //= 10
        k -= digit+1

print(n)