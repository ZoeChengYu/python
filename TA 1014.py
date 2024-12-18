def nMark(n,mark):
    for j in range(n):
        print(mark,end='')

def f(N):
    for i in range(0,N):
        nMark(N-i-1, '○')
        nMark(2*i+1, '●')
        nMark(N-i-1, '○')
        print('\n')

f(6)
    