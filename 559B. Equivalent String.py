def func(s):
    n = len(s)
    if(n%2==1):
        return s
    s1=func(s[:n//2])
    s2=func(s[n//2:])
    if(s1<s2):
        return s1+s2
    else:
        return s2+s1

a=input()
b=input()

if func(a)==func(b):
    # print(func(a),func(b))
    print('YES')
else:
    # print(func(a),func(b))
    print('NO')