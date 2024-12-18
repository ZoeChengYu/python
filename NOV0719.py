def input_data():
    n=int(input())
    data=list(input().split() for i in range(n))
    return data

def Unfor(register,data):
    for Un in range(len(data)):
         Bifor(register,data,Un)

def Bifor(register,data,Un):
    for Bi in range(len(data[Un])):
        if data[Un][Bi]=='0':
            Trifor(register,data,Un,Bi)

def Trifor(register,data,Un,Bi):
    for Tri in range(Un-1,Un+2,1):
        if (Tri >=0)and(Tri<len(data)):
            Quadfor(register,data,Un,Bi,Tri)

def Quadfor(register,data,Un,Bi,Tri):
    for Quad in range(Bi-1,Bi+2,1):
        if (Quad>=0)and(Quad<len(data[Un])):
            (register[Un][Bi])+=int(data[Tri][Quad])

def print_Re(register):
    for i in range(len(register)):
        register[i]=' '.join(register[i])
    stry='\n'.join(register)
    print(stry)

def typr_str(register):
    for i in range(len(register)):
        for j in range(len(register[i])):
            register[i][j]=str(register[i][j])

def main():
    data=input_data()
    register=list(list(0 for j in range(len(data[i])))for i in range(len(data)))
    Unfor(register,data)
    typr_str(register)
    print_Re(register)

main()