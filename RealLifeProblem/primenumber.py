def primeno(a):
    x = 0
    for i in range(1,a):
        if a%i==0:
            x += 1
    if x == 1:
        return(a)

t = int(input())
tn = int(input())

for _ in range(t, tn+1):
    if primeno(_) != None:
        print(primeno(_))
 # if you decrrease the number of variable you can cecrease the code