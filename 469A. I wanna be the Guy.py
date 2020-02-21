n = int(input())

temp = input().split()

x = int(temp[0])
x_data = temp[1:]

for i in range(x):
    x_data[i] = int(x_data[i])

temp = input().split()

y = int(temp[0])
y_data = temp[1:]
for i in range(y):
    y_data[i] = int(y_data[i])

# for i in range(1,n+1):

new_ = x_data + y_data
if len(set(new_)) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
