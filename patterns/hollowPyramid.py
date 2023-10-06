n = 16
for i in range(n):
    if i == 0:
        print(" "*(n)+"*")
    elif i == n-1:
        print(" *"*n)
    else:
        print(" "*(n-i)+"*"+" "*((i*2)-1)+"*")