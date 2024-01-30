import numpy as np

a=[[1, 0],
     [0, 1]]
b=[[1, 0],
     [0, 1]]

s1=np.shape(a)
s2=np.shape(b)
print(a[1][1])


def mult(a,b,s1,s2):
    if s1[1]==s2[0]:
        print("can be multiplied")
    else:
        print("cannot be multiplied")
        return None

    c=[[0, 0],
         [0, 0]]

    for i in range(s1[0]):
        for j in range(s2[1]):
            for k in range(s1[1]):
                c[i][j]+=a[i][k]*b[k][j]

    return c


result=mult(a,b,s1,s2)
if result:
    print("Result of multiplication:")
    for row in result:
        print(row)
