def input_base():
    m,n=int(input()),int(input())
    if (n<1)or(n>9):
        return 0,0
    return m,n

def p1(n):
    for i in range(n):
        print(str(i+1)*(i+1),end='')
        print('#'*(n-i-1),end='')
        print()

def p2(n):
    for i in range(n):
        print('#'*(2*(n-i-1)),end='')
        sub2(n,i)
        print()

def sub2(n,i):
    for j in range(i+1):
        print(j+1,end='')
    for j in range(i,0,-1):
        print(j,end='')

def p3(n):
    for i in range(n):
        sub3(n,i,0)
        print('^'*(n-i-1),end='')
        print()
    for i in range(n,0,-1):
        sub3(n,i,1)
        print('^'*(n-i),end='')
        print()

def sub3(n,i,r):
    if r%2==0:
        for j in range(i+1):
            print(j+1,end='')
    else:
        for j in range(i,0,-1):
            print(j,end='')

def p4(n):
    for i in range(n):
        print('^'*(n-i-1),end='')
        sub4(n,i)
        print('^'*(n-i-1),end='')
        print()
    for i in range(n-2,-1,-1):
        print('^'*(n-i-1),end='')
        sub4(n,i)
        print('^'*(n-i-1),end='')
        print()

def sub4(n,i):
    for j in range(i+1):
        print(j+1,end='')
    for j in range(i,0,-1):
        print(j,end='')

def main():
    m,n=input_base()
    if m==1:
        p1(n)
    elif m==2:
        p2(n)
    elif m==3:
        p3(n)
    elif m==4:
        p4(n)
    else:
        return

main()