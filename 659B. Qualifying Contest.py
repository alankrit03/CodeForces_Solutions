n , m = map(int,input().split())

data = []
for i in range(n):
    temp = input().split()
    data.append((temp[0], int(temp[1]) , int(temp[2])))

info = {}
for x in data:
    if not info.get(x[1]):
        info[x[1]] = [(x[0],x[2])]
        flag=1
    else:
        flag = len(info.get(x[1]))
        i=flag-1
        while i>=0 and info[x[1]][i][1]<x[2]:
            i-=1
        info[x[1]].insert(i+1,(x[0],x[2]))
    if flag+1>3:
        info[x[1]].pop()

for i in range(1,m+1):
    team = info.get(i)
    if len(team) == 2:
        print(team[0][0],team[1][0])
    else:
        if team[1][1]==team[2][1]:
            print('?')
        else:print(team[0][0],team[1][0])