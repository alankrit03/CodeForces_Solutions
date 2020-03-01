a ,b = map(int ,input().split())
year =0
while b>= a:
    b *= 2
    a *= 3
    year += 1

print(year)