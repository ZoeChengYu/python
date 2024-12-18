def print_odd(NUM):
    sign_A=list(list('#' for A1 in range(NUM-A0-1)) for A0 in range(NUM))
    sign_B=list(list('*' for B1 in range(2*B0+1)) for B0 in range(NUM))
    for s in range(NUM):
        st=''
        for i in range(NUM-s-1):
            st=st+sign_A[s][i]
        for j in range(2*s+1):
            st=st+sign_B[s][j]
        print(st)

def print_even(NUM):
    sign_A=list(['*']+list('#' for A1 in range(NUM-2))+['*'] for A0 in range(NUM-2))
    for s in range(NUM):
        if (s==0) or (s==NUM-1):
            st='*'*NUM
        else:
            st=''
            for i in range(NUM):
                st=st+sign_A[s-1][i]
        print(st)
    
def input_size():
    size=int(input())
    if size % 2 == 0:
        print_even(size)
    else:
        print_odd(size)
    
input_size()