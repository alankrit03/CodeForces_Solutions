n = input()

data = input()
a = data.count('A')
d = data.count('D')

if a>d:
    print('Anton')
elif d>a:
    print('Danik')
else:
    print('Friendship')