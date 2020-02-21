n, t = map(int, input().split())

data = [int(x) for x in input().split()]

i = 0
j = -1
sum_ = 0

while j < n - 1:

    if sum_ + data[j + 1] <= t:
        sum_ += data[j + 1]
        j += 1

    else:
        j += 1
        sum_ += data[j]
        sum_ -= data[i]
        i += 1

print(j - i + 1)