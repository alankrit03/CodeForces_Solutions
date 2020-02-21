# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Example
# # input
# # ababcba
# # abb
# # 5 3 4 1 7 6 2
# # output
# # 3
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def is_pattern_present(s):
    pat_req = pattern
    while s:
        if not pat_req:
            return 1
        if s[0] == pat_req[0]:
            pat_req.pop(0)
        s.pop(0)

    if not pat_req:
        return 1
    else:
        return 0


def create_list(x):
    temp = original
    for i in range(x + 1):
        temp.pop(sequence[i] - 1)
    return temp


original = list(input())
pattern = list(input())
len_pattern = len(pattern)
sequence = [int(x) for x in input().split()]
n = len(sequence)

l = 0
h = n

while h - l > 1:
    m = (l + h) // 2

    new_str = create_list(m)
    if n - m >= len_pattern and is_pattern_present(new_str):
        l = m
    else:
        h = m

print(l)
