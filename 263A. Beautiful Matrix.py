n = 5
matrix = []

for i in range(n):
    matrix.append([int(x) for x in input().split()])

for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            pos = (i,j)
            break

ans = abs(pos[0]-2) + abs(pos[1]-2)
print(ans)