n = 6
pascalTri = []

for x in range(n):
    row = []
    # print("x",x)
    for y in range(x+1):
        # print("y",y)
        if y ==0 :
            row.append(1)
        elif y==x:
            row.append(1)
        else:
            row.append(pascalTri[x-1][y-1] + pascalTri[x-1][y])

    pascalTri.append(row)        
print(pascalTri)