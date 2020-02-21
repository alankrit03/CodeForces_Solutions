T = int(input())

for i in range(T):
    word=input()
    n = len(word)
    if n>10:
        print(word[0],n-2,word[-1],sep='')
    else:
        print(word)