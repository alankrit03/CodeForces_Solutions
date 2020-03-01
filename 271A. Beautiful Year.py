def check(num):
    d = dict()
    while num:
        if d.get(num % 10):
            return False
        d[num%10] = 1
        num //= 10
    return True

year = int(input())

while 1:
    year += 1
    if check(year):
        print(year)
        break