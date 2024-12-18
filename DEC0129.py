def inputing():
    data=input()
    size=int(input())
    return data,size

def Permutation(data:str,si,zip:list):
    if len(data)==1:
        si=si+data[0]
        zip.append(si)
    else:
        for i in range(len(data)):
            shelter=data[:i]+data[i+1:]
            Permutation(shelter,si+data[i],zip)

def Combination(data,size,so,rar:list):
    if size==1:
        for i in range(len(data)):
            re=so+data[i]
            rar.append(re)
    else:
        for i in range(len(data)):
            sanctuary=data[i+1:]
            Combination(sanctuary,size-1,so+data[i],rar)

def main():
    zip=[]
    rar=[]
    data,size=inputing()
    Permutation(data,'',zip)
    Combination(data,size,'',rar)
    for i in range(len(zip)):
        print(zip[i],end='')
        if i==(len(zip)-1):
            print()
        else:
            print(', ',end='')
    for i in range(len(rar)):
        print(rar[i],end='')
        if i==(len(rar)-1):
            print()
        else:
            print(', ',end='')

main()