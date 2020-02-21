def cut_ribbon(size, cuts):
    if size < 0:
        return 0
    if size % c == 0:
        return cuts + (size // c)
    c1 = cut_ribbon(size - a, cuts + 1)
    c2 = cut_ribbon(size - b, cuts + 1)

    return max(c1, c2)


n, a, b, c = map(int, input().split())

if c > a:
    c, a = a, c
if b > a:
    b, a = a, b
if c > b:
    b, c = c, b

cut = cut_ribbon(n, 0)
print(cut)
