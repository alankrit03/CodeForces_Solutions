for _ in range(int(input())):
    n = int(input())
    arr = input().split()
    for i in range(n):
        arr[i]= int(arr[i])-1

    ans = [0]*n
    cache = [False]*n

    for i in range(n):
        print(ans)

        if not cache[i]:
            curr = []

            while not cache[i]:
                curr.append(i)
                cache[i]=True
                i = arr[i]
            x= len(curr)
            print(curr)
            for ele in curr:
                ans[ele] = x

    # print(*ans)