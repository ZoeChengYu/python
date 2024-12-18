def input_f():
    n=int(input())
    if n<1 or n>10:
        print('ERROR')
        return 0,[0]
    else:
        m=[int(input())]
        while m[-1]!=-1:
            m=m+[int(input())]
        return n,m

def result(n,m):
    for i in range(len(m)-1):
        if m[i]==0 or m[i]==1 or m[i]==2:
            address(n,m[i])
        else:
            print('ERROR')

def address(n,m):
    for i in range(n):
        Call(n,m,i)
        print()

def Call(n,m,i):
    for j in range(n):
        if m==0:
            print('%3d' %(i*n+j),end='')
        elif m==1:
            print('%3d' %((n-i-1)*n+j),end='')
        else:
            print('%3d' %(i+(n-j-1)*n),end='')

def main():
    n,m=input_f()
    result(n,m)

main()