def add(N):
    if N==1:
        return 1
    else:
        return sub(N-1)+N
    
def sub(N):
    if N==1:
        return 1
    else:
        return mux(N-1)-N
    
def mux(N):
    if N==1:
        return 1
    else:
        return dex(N-1)*N
    
def dex(N):
    if N==1:
        return 1
    else:
        return add(N-1)/N