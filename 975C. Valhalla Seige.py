def get_pos(curr, strength_left, arrow):
    l = curr
    h = n - 1

    while (l < h):
        m = (l + h) // 2
        strength_req = strength[m] - strength[curr] + strength_left
        if strength_req > arrow:
            h = m
        elif strength_req == arrow:
            return m
        else:
            if m == n - 1:
                return m
            l = m + 1

    return l


n, minutes = map(int, input().split())
strength = [int(x) for x in input().split()]
arrows = [int(x) for x in input().split()]
res = [0] * minutes

for i in range(1, n):
    strength[i] = strength[i] + strength[i - 1]

curr = 0
strength_left = strength[0]

for i in range(minutes):
    arrow = arrows[i]
    new_pos = get_pos(curr, strength_left, arrow)

    temp = strength[new_pos] - strength[curr] + strength_left

    if temp > arrow:
        curr = new_pos
        strength_left = temp - arrow
        res[i] = n - curr
    else:
        curr = (new_pos + 1) % n
        if curr:
            strength_left = strength[curr] - strength[curr - 1]
        else:
            strength_left = strength[curr]
        res[i] = n - curr

print(*res, sep='\n')
