n , q = map(int,input().split())

data = input().split()

for i in range(q):
    data[i] = int(data[i])

sum_=0
house=1
for x in data:
    if x>=house:
        sum_ = sum_ + (x-house)
        house=x
    else:
        sum_ = sum_ + (n-house) + x
        house = x

print(sum_)