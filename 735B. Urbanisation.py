"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
INPUT : 2 1 1
........1 5
OUTPUT: 6.0000000000
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

def divide_people(c_n1 , c_n2 , sum_n1 , sum_n2 , idx):
    if n-idx < n1+n2 - c_n2-c_n1:
        return 0
    elif c_n1==n1 and c_n2 == n2:
        return (sum_n1/n1) + (sum_n2/n2)

    if c_n2!=n2 and c_n1!=n1:
        x = divide_people(c_n1 , c_n2+1 , sum_n1 , sum_n2+arr[idx] , idx+1)
        y = divide_people(c_n1+1, c_n2, sum_n1 + arr[idx], sum_n2 , idx + 1)
        z = divide_people(c_n1, c_n2, sum_n1, sum_n2 , idx + 1)
        return max(x,y,z)

    elif c_n2!=n2:
        z = divide_people(c_n1, c_n2, sum_n1, sum_n2, idx + 1)
        x=divide_people(c_n1, c_n2 + 1, sum_n1, sum_n2 + arr[idx], idx + 1)
        return max(x,z)

    else:
        z = divide_people(c_n1, c_n2, sum_n1, sum_n2, idx + 1)
        x=divide_people(c_n1 +1, c_n2, sum_n1 + arr[idx], sum_n2, idx + 1)
        return max(x,z)


n , n1, n2 = map(int,input().split())
arr=[int(x) for x in input().split()]

ans = divide_people(0,0,0,0,0)

print(ans)