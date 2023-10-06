def takeTerrain(n):
    lt = []
    for x in range(n+2):
        lt.append([])
        for y in range(n+2):
            if x == 0 or y ==0 or x == n+1 or y ==n+1:
                lt[x].append(0)
            else:
                lt[x].append(int(input()))
    return lt

def ilCounter(island,px,py):
    if island[px][py] == 1:
        island[px][py] = 0 
        if island[px+1][py] == 1:
            island,temp = ilCounter(island,px+1,py)
        if island[px-1][py] == 1:
            island,temp = ilCounter(island,px-1,py)
        if island[px][py+1] == 1:
            island,temp = ilCounter(island,px,py+1)
        if island[px][py-1] == 1:
            island,temp = ilCounter(island,px,py-1)
        return island, 1
            
    else:
        return island, 0

n = int(input())
island = takeTerrain(n)

count =0 
for x in range(1,n+1):
    for y in range(1,n+1):
        island,temp=ilCounter(island,x,y)
        count += temp

print("No of island :",count)