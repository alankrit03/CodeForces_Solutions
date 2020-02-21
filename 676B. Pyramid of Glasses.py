"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Input
The only line of the input contains two integers n and t (1 ≤ n ≤ 10, 0 ≤ t ≤ 10 000) —
the height of the pyramid and the number of seconds Vlad will be pouring champagne from the bottle.
''''''''''''''''''''''''''''''''''''''''''''''''''''
Output
Print the single integer — the number of completely full glasses after t seconds.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


def fill_wine(x, y , val):
    if x==n or y==n:
        return 0
    if arr[x][y] == 1:
        fill_wine(x+1 , y , val/2)
        fill_wine(x+1 , y+1 , val/2)
        return 0
    if arr[x][y] + val <= 1:
        arr[x][y]+=val
    else:
        extra = arr[x][y] + val -1
        arr[x][y] = 1
        fill_wine(x+1 , y , extra/2)
        fill_wine(x+1 , y+1 , extra/2)


def print_matrix():
    for i in range(n):
        print(*arr[i])
def check_full():
    res=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                res+=1
    return res


n , t = map(int,input().split())

arr = [[0]*n for i in range(n)]

for i in range(t):
    fill_wine(0,0,1)

ans = check_full()
# print_matrix()

print(ans)