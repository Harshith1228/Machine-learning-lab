a=int(input("Enter the number of rows in the matrix: "))
b=int(input("Enter the number of columns in the matrix: "))

matrix = []

for i in range(a):
    row = []
    for j in range(b):
        element = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
        row.append(element)
    matrix.append(row)

print("User input matrix:")
for row in matrix:
    print(row)


print(matrix)

def transpose(matrix):
    tmatrix=[]
    for i in range(a):
        for j in range (b):
            tmatrix[i][j]=matrix[j][i]


    for i in range(a):
        for j in range (b):
            matrix[i][j]=tmatrix[i][j]
    return matrix
result=transpose(matrix)
print(result)