li = [[1,2,3,4],[4,5,6,8]]
li1 = []
for _ in range(len(li[0])):
    li1.append([])
    for p in range(_):
        li1[p].append(p)

for y in range(len(li[0])):
    for x in range(len(li)):
        li1[y][x] =li[x][y] 

print(li1)