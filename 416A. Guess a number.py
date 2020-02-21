n = int(input())
limit = [-2000000000, 2000000000]

for i in range(n):
    query = input().split()

    if (query[0] == '>=' and query[2] == 'Y') or (query[0] == '<' and query[2] == 'N'):
        x = (int(query[1]))
        if limit[1] < x:
            print('Impossible')
            break
        limit[0] = max(limit[0], x)

    elif (query[0] == '>' and query[2] == 'Y') or (query[0] == '<=' and query[2] == 'N'):
        x = (int(query[1]))
        if limit[1] <= x:
            print('Impossible')
            break
        limit[0] = max(limit[0], x + 1)

    elif (query[0] == '<=' and query[2] == 'Y') or (query[0] == '>' and query[2] == 'N'):
        x = (int(query[1]))
        if limit[0] > x:
            print('Impossible')
            break
        limit[1] = min(limit[1], x)


    elif (query[0] == '<' and query[2] == 'Y') or (query[0] == '>=' and query[2] == 'N'):
        x = (int(query[1]))
        if limit[0] >= x:
            print('Impossible')
            break
        limit[1] = min(limit[1], x - 1)

else:
    print(limit[0])