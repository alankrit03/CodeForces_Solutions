n , fence = map( int , input().split())
arr = [int(x) for x in input().split()]

total = 0
for x in arr:
    if x>fence:
        total += 2
    else:
        total += 1

print(total)