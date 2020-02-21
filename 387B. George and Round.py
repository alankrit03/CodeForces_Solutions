n , m = map(int , input().split())

good_prob = [int(x) for x in input().split()]
problems = [int(x) for x in input().split()]

good_prob.sort()
problems.sort()

result = 0

while good_prob:
    if not problems:
        result += len(good_prob)
        break
    elif good_prob[0] > problems[0]:
        problems.pop(0)
    else:
        problems.pop(0)
        good_prob.pop(0)

print(result)