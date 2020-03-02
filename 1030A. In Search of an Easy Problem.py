n = int(input())

arr= [int(x) for x in input().split()]

if sum(arr):
    print('HARD')
else:print('EASY')