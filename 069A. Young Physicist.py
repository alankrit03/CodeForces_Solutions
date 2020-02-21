n = int(input())

total_x =0
total_y = 0
total_z =0

for i in range(n):
    x,y,z=map(int,input().split())
    total_x +=x
    total_y +=y
    total_z +=z

if (not total_x) and (not total_y) and (not total_z) :
    print('YES')
else:
    print('NO')
