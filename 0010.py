import random
def X(A):
    S=[]
    for i in range(len(A)):
        if A[i]%2==0:
            S.append(A[i])
    return S

A=list((random.randint(0,1000))for i in range(0,300))
A=X(A)
W=list((i**2) for i in A)

print(W)