import numpy as np
from random import randint as ri
try:
    print("Input N")
    n = int(input())
    if (n % 2) | (n < 1):
        raise Exception("The dimension must be even")
    print("Input K")
    k = int(input())


    a = np.array([[ri(-10, 10) for j in range(n)] for i in range(n)])
    print("Matrix A")
    print(a)
    f = a.copy()

    middle=n//2
    e = f[0:middle,0:middle]
    b = f[0:middle, middle:]
    d = f[middle:, 0:middle]
    c = f[middle:, middle:]
    print("Matrix Е")
    print(e)
    print("Matrix B")
    print(b)
    print("Matrix D")
    print(d)
    print("Matrix C")
    print(c)

    sum=0
    count=0
    i = 0
    for row in e:
        j = 0
        for value in row:
            if i % 2:
                sum += value
            if j % 2 == 0:
                if value > k:
                    count += 1
            j += 1
        i += 1

    i = 0
    print("sum =",sum,"count =",count)
    if sum < count:
        print("Symmetric exchange of A and C")
        for row in e:
            j = 0
            for value in row:
                e[i,j],c[middle-1-i,middle-1-j]=c[middle-1-i,middle-1-j],e[i,j]
                j += 1
            i += 1
        print("Matrix Е")
        print(e)
        print("Matrix C")
        print(c)
    else:
        print("Asymmetric exchange of B and C")
        for row in b:
            j = 0
            for value in row:
                b[i, j], c[i, j] = c[i,j], b[i, j]
                j += 1
            i += 1
        print("Matrix C")
        print(c)
        print("Matrix B")
        print(b)
    print("Matrix F \n",f)
    det=np.linalg.det(a)
    print("The determinant of the matrix A \n",det)
    sum=np.trace(f)
    print("The sum of the diagonal elements of the matrix F \n", sum)
    aT = np.transpose(a)
    print("The transposed matrix A \n", aT)
    if det>sum:
        fT = np.transpose(f)
        print("The transposed matrix F \n", fT)
        ans=a.dot(aT)-k*fT
        print("The final answer \n",ans)
    else:
        fInv=np.linalg.inv(f)
        print("The inverse matrix F \n", fInv)
        g=np.tril(a)
        print("lower triangular matrix A \n", g)
        gInv = np.linalg.inv(g)
        print("The inverse matrix G \n", gInv)
        ans=(aT+gInv-fInv)*k
        print("The final answer \n", ans)
except Exception as exc:
        print(exc)
