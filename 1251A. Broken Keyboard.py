for _ in range(int(input())):
    inp = input()
    cache = set()
    n = len(inp)

    i=0
    j=0
    while j<n:
        if j+1 < n:
            if inp[j+1]==inp[i]:
                j +=1
            else:
                if (j-i+1) % 2:
                    cache.add(inp[i])
                i = j+1
                j = i
        else:
            if (j - i + 1) % 2:
                cache.add(inp[i])
            i = j + 1
            j = i

    print("".join(sorted(list(cache))))