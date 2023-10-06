def leftadd(lt,i):
    sum1 =0
    for _ in range(i):
        sum1+=lt[_]
    return sum1
def rightadd(lt,i):
    sum = 0
    for __ in range(i+1,len(lt)):
        sum +=lt[__]
    return sum
lt = map(list,input().split())
for ii in range(1,len(lt)-1):
    if leftadd(lt,ii)==rightadd(lt,ii):
        print(ii)
