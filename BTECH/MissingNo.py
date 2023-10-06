l = [0,5,3,1,2,4,7]
a = l
l.sort()

for i in range(l[0],l[-1]+1):
    if i != l[i]:
        print("The missing the number is :",i)
        break