x = int(input())
n = x-1
for i in range(x):
    print(" "*(n*2)+" *"*(x-n))
    n-=1