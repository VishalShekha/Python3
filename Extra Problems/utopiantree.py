intiH = 1
def firstCycle(x):
    return x*2
def secondCycle(y):
    return y+1
n = int(input())
n += 1
for _ in range(1,n):
    if _%2!=0:
        intiH = firstCycle(intiH)
    else:
        intiH = secondCycle(intiH)

print(intiH)
