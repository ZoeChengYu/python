def input_Q():
    N,M,C=int(input()),int(input()),int(input())
    return N,M,C

def fish(N,M):
    if M%2==0:
        for i in range(N):
            fish_tail(N,i,M)
            fish_head(N,i)
            print()
        for i in range(N-2,-1,-1):
            fish_tail(N,i,M)
            fish_head(N,i)
            print()
    else:
        for i in range(N):
            fish_head(N,i)
            fish_tail(N,i,M)
            print()
        for i in range(N-2,-1,-1):
            fish_head(N,i)
            fish_tail(N,i,M)
            print() 

def fish_head(N,i):
    print('_'*(N-i-1),end='')
    print('*'*(2*i+1),end='')
    print('_'*(N-i-1),end='')

def fish_tail(N,i,M):
    if M%2==1:
        print('_'*(N-i-1),end='')
    print('*'*(i+1),end='')
    if M%2==0:
        print('_'*(N-i-1),end='')

def triangle(N,M):
    if M%2==0:
        for i in range(N,0,-1):
            print('_'*(N-i),end='')
            triangle_number(i)
            print('_'*(N-i),end='')
            print()
    else:
        for i in range(1,N+1,1):
            print('_'*(N-i),end='')
            triangle_number(i)
            print('_'*(N-i),end='')
            print()

def triangle_number(i):
    for j in range(i,0,-1):
        print(j,end='')
    for j in range(2,i+1,1):
        print(j,end='')

def main():
    N,M,C=input_Q()
    if C%2==1:
        fish(N,M)
    else:
        triangle(N,M)

main()