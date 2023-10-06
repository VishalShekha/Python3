def In():
    r = int(input())
    c = int(input())
    X = []

    X1 = list(map(int,input().split()))
    i=0
    for x in range(r):
        X.append([])
        for y in range(c):
            X[x].append(X1[i])
            i+=1
    return X

A,B = [],[]
A = In()
B = In()

def matrix_multiply(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum_element = 0
            for k in range(len(matrix2)):
                sum_element += matrix1[i][k] * matrix2[k][j]
            row.append(sum_element)
        result.append(row)

    return result

print(matrix_multiply(A,B))
