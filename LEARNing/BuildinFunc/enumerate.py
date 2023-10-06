lis = [1,"Visha",3]
new_var = enumerate(lis)
print(new_var)
print(type(new_var))
print(list(new_var))
print(dict(new_var))

lis1 = [1,2,3]
for i,j in enumerate(lis,lis1):
    print(i,j)