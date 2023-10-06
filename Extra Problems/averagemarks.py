total_marks = 0
noofstud = int(input())
for i in range(noofstud):
    mark = int(input())
    if mark<0:
        print("Invalid input")
    else:
        total_marks += mark

average = total_marks/noofstud
print(format(average,".2f"))
