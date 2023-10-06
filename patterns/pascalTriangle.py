n = int(input("Enter the lenght of pascal triangle : "))
pascalTri = []

def firstlayer():
    lt = []
    ltz = [0]
    lto = [1]
    for _ in range(2):
        for p in range(n):
            lt += ltz
            if p==n-1:
                lt += lto
    lt.pop()
    return lt

def layers(alt):
    nlt = []
    for i in range(1, len(alt)):
        x = alt[i-1]+alt[i]
        nlt += [x] 
    return nlt

lt = firstlayer()
wlt = layers(lt)
pascalTri.append(lt)

for i in range(n-1):
    wlt = layers(wlt)
    pascalTri.append(wlt)

print(pascalTri[::-1])

#[[1],[1,1],[1,2,1],[1,3,3,1]]