def data(n:int):
    if n==0:
        datas='qwertyuioplkjhgfdsazxcvbnm'
    else:
        datas='QWERTYUIOPLKJHGFDSAZXCVBNM'
    datas=list(datas)
    return datas

def f(s:str):
    s=list(s)
    n=len(s)-1
    BIG,SMALL=0,0
    BIG,SMALL=X(s,n,1),X(s,n,0)
    print('大寫:%d\n小寫:%d' %(BIG,SMALL))

def X(s:list,n:int,t:int)->int:
    if n==-1:
        return 0
    else:
        if s[n] in data(t):
            x=(1+X(s,n-1,t))
        else:
            x=(0+X(s,n-1,t))
    return x

f(input())