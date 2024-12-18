def input_str():
    Base=str(input())
    Base=Base.split()
    for i in range(len(Base)):
       Base[i]=int(Base[i])
    return Base

def sol(data):
    Ans=list(0 for i in range(len(data)-1))
    for local_Ans in range(len(Ans)):
        Ans[local_Ans]=data[local_Ans]+data[local_Ans+1]
    return Ans

def main():
    data=input_str()
    print(sol(data))
    
main()
