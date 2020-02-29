n = int(input())

min_val = 0
current = 0
for i in range(n):
    exit , entry = map(int , input().split())
    current =  current - exit + entry
    min_val = max(current , min_val)

print(min_val)