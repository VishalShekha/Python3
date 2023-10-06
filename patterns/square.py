n = 5
i=1
while i<=n:
    if i==1 or i==n:
        print("* "*n)
    else:
        print("*{}*".format(" "*((n*2)-3)))
    i+=1