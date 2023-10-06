#  Write a Python program to generate a 3*4*6 3D array whose each element is *

x = int(input())
y = int(input())
z = int(input())
lt = []
for a in range(x):
    lt.append([])
    for b in range(y): 
        lt[a].append([]) 
        for c in range(z):
            lt[a][b].append("*")    

print(lt)