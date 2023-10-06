if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = sum(student_marks[query_name])
    avg = total/3
    x= 0
    print(format(avg,".2f"),format(x,".3f"))
