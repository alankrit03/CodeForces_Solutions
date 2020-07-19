data = input()

l=u = 0

for x in data:
    if x.islower():
        l+=1
    else:
        u+=1

if l>=u:
    print(data.lower())
else:
    print(data.upper())