n = int(input())

names = [0] * n
names_dic = dict()
result = []
name_index = dict()


for i in range(n):
    old, new = input().split()
    names_dic[old] = new
    names[i] = [old, True]
    name_index[old] = i

# print(names)
# print()
# print(names_dic)
# print(name_index)

for name in names:
    if name[1]:
        curr=name[0]
        while names_dic[curr] in names_dic:
            curr = names_dic[curr]
            names[name_index[curr]][1] = False
        result.append(name[0]+' '+names_dic[curr])

print(len(result))
print(*result,sep='\n')