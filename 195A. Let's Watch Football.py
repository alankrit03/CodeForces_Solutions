n, m, k = map(int, input().split())

total_data = n * k
if total_data % m == 0:
    time_req = (total_data // m)
    # print(time_req-k)
else:
    time_req = (total_data // m) + 1


print(time_req - k)