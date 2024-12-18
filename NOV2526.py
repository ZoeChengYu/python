def inputer():
    base=input().split()
    M=int(input())
    return base,M

def target(data:list,M):
    goal=[]
    fever=0
    for i in range(len(data)):
        fever+=int(data[i][0])
    if fever==M:
        goal=[i[1] for i in data]
        return[goal]
    elif domain(data,M)=="Load limit exceeded":
        return "Load limit exceeded"
    elif fever%M!=0 or domain(data,M)=="Cannot be delivered":
        return "Cannot be delivered"
    else:
        #goal,datas=
        goal,datas=domain(data,M)
        for j in range(len(datas)):
            data.remove(datas[j])
        return [goal]+target(data,M)

def domain(data,M):
    copy=[(i) for i in data[::]]
    lists=[]
    datas=[]
    n=M
    ghost=[]
    for i in range(len(copy)):
        noon=''
        ty=copy[i][:-1]
        for j in range(len(ty)):
            noon=noon+ty[j]
        noon=int(noon)
        ghost.append(noon)
    for i in range(len(ghost)):
        if ghost[i] > M:
            return "Load limit exceeded"
    if min(ghost)>n:
        return "Cannot be delivered"
    for i in range(len(copy)):
        if ghost[i]==n:
            lists.append(copy[i][-1])
            datas.append(copy[i])
            return lists,datas
        else:
            if ghost[i]<n:
                lists.append(copy[i][-1])
                datas.append(copy[i])
                n-=ghost[i]
                
def transport(dss):
    lendss=[]
    result=[]
    for i in range(len(dss)):
        lendss.append(len(dss[i]))
    maxdss=max(lendss)
    for x in range(1,maxdss+1):
        regist=[]
        for i in range(len(dss)):
            if len(dss[i])==x:
                dss[i].sort()
                regist.append(dss[i])
        regist.sort()
        result.append(regist)
    for i in range(maxdss):
        for j in range(len(result[i])):
            last(result,i,j)

def last(result:list,i,j):
    for k in range(len(result[i][j])):
                if k == len(result[i][j])-1:
                    print(result[i][j][k])
                else:
                    print(result[i][j][k],end=' ')

def cheack(data:list):
    for i in range(len(data)):
        ssd=data[:i]
        ssd.append(data[i+1:])
        if data[i] in ssd:
            return True
    return False

def main():
    data,M=inputer()
    if M<1 or M>10:
        print("Input Error")
    elif cheack(data):
        print("Duplicated ID")
    else:
        novo=target(data,M)
        if novo=="Load limit exceeded":
            print("Load limit exceeded")
        elif novo=="Cannot be delivered":
            print("Cannot be delivered")
        else:
            print(len(novo))
            transport(novo)
    
main()