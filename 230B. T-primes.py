def my_sqrt(x):
    l = 0
    h = x + 1
    while (h - l > 1):
        m = (l + h) // 2

        if m * m <= x:
            l = m
        else:
            h = m
    return l


def SieveOfEratosthenes(n):
    p = 2
    while (p * p <= n):

        if (prime[p]):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False


n = int(input())
arr = [int(x) for x in input().split()]
prime = [True] * 1000001
SieveOfEratosthenes(1000000)

for x in arr:
    root = my_sqrt(x)
    if root * root == x and prime[root]:
        print('YES')
    else:
        print('NO')