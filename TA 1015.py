def nMark2(n):
    for i in range(n,1,-2):
        print(i,end='')
        
def nMark3(n):
    for j in range(1,n+1,2):
        print(j,end='')

def nMark1(n):
        print('#'*n,end='')
    
        
def f(N):
    for h in range(N):
        nMark1(N-h-1)
        nMark2(2*h+1)
        nMark3(2*h+1)
        print('')

f(5)