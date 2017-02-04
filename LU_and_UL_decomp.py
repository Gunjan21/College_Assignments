#LU DECOMPOSOTION:
#UL DECOMPOSITION:
#INVERSE:
import pprint

def matrix():
    matrixA = [[1,2,3,4],[6,4,3,4],[2,3,6,1],[7,2,5,4]]
    return matrixA

def alpha(A,i,j,x):
    if A[x][x] == 0:
        raise RuntimeError("This matrix will not have an LU decomposition, it will have an PA=LU decomposition")
    else:
        l =  A[i][j] / A[x][x]
    return (-l)


def elementary_matrix(i,j,alpha,A):
    elem_matrix = [[1 if x == y else 0 for x in range(0,len(A[y]))]for y in range(0,len(A))];
    elem_matrix[i][j] = alpha
    return elem_matrix
    
def multiplication(A,B):

    m = len(A)
    n = len(A[0])
    p = len(B)
    q = len(B[0])
    result = [[0 for x in range(0,n)]for y in range(0,q)]
  
    for i in range(0,m):
        for j in range(0,q):
            for k in range(0,n):
                result[i][j] += A[i][k]*B[k][j]
    return result

def LU():
    A = matrix()
    L = [[1 if x == y else 0 for x in range(0,len(A[y]))]for y in range(0,len(A))]
    for i in range(0,len(A)-1):
        for j in range(i,len(A[i])):
            if i == j :
                a = i
            else:    
                b = alpha(A,j,i,a)
                row_operation = elementary_matrix(j,i,b,A)
                A = multiplication(row_operation,A)

                L[j][i] += b
                
    print("U:")
    pprint.pprint(A)
    print("L:")
    pprint.pprint(L)


def UL():
    A = matrix()
    U = [[1 if x == y else 0 for x in range(0,len(A[y]))]for y in range(0,len(A))]
    for i in range(len(A)-1,-1,-1):
        for j in range(i,-1,-1):
            if i == j :
                a = i
            else:    
                b = alpha(A,j,i,a)
                row_operation = elementary_matrix(j,i,b,A)
                A = multiplication(row_operation,A)
                U[j][i] += b
    print("U:")
    pprint.pprint(U)
    print("L:")
    pprint.pprint(A)    


def Inverse():
    A = matrix()
    try:
        I = [[1 if x == y else 0 for x in range(0,len(A[y]))]for y in range(0,len(A))]
        print("The matrix is : ")
        pprint.pprint(A)
        for i in range(0,len(A)-1):
            for j in range(i,len(A[i])):
                if i == j :
                    a = i
                else:    
                    b = alpha(A,j,i,a)
                    row_operation = elementary_matrix(j,i,b,A)
                    I = multiplication(row_operation,I)
                    A = multiplication(row_operation,A)

        for i in range(len(A)-1,-1,-1):
            for j in range(i,-1,-1):
                if i == j :
                    d = i
                else:    
                    f = alpha(A,j,i,d)
                    row_operation = elementary_matrix(j,i,f,A)
                    I = multiplication(row_operation,I)
                    A = multiplication(row_operation,A)

        for i in range(0,len(A)):
            for j in range(i,len(A[i])):
                if i==j:
                    c=A[i][j]
            for k in range(0,len(I[i])):
                I[i][k]=I[i][k]/c
    
        print("The Inverse is  :")
        pprint.pprint(I)
    except:
        raise RuntimeError("Inverse does not exist")
    
