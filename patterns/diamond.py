n = 10

i = 1
n+=1
while i<n-1:
    print(" "*(n-i),"* "*i)
    i+=1
i = 0
n-=1
while i<n:
    print(" "*i," *"*(n-i))
    i+=1