def check_config(s):
    i = n - 1
    j = 0
    box_left = k
    while j <= i:
        if (i - j + 1) // box_left == 2:
            if size[i] + size[j] > s:
                return False
            else:
                j += 1

        else:
            if size[i] > s:
                return False

        i -= 1
        box_left -= 1
    return True


n, k = map(int, input().split())
size = [int(x) for x in input().split()]

l = size[-1] - 1
h = (2 * (l + 1))

while (h - l > 1):

    m = (l + h) // 2

    if check_config(m):
        h = m
    else:
        l = m

print(h)