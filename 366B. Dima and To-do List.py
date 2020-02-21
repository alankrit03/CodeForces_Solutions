def get_power(i):
    power=0
    while i<n:
        power+=arr[i]
        i+=k
    return power



n , k = map(int, input().split())

arr= [int(x) for x in input().split()]

min_power=get_power(0)
start =0

for i in range(k):
    power = get_power(i)
    # print(f'start={i+1} power={power}')
    if power < min_power:
        min_power=power
        start=i
    i+=1
print(start+1)