def gavedata(data:list,N):
    for k in range(len(data)):
        data[k]=int(data[k])
    lists=[]
    if sum(data)==N:
        return [data]
    else:
        lists=finddata(data,N)
        if type(lists) != None:
            for j in lists:
                data.remove(j)
            return [lists]+gavedata(data,N)

def finddata(data:list,N:int)->list:
    sega=[(i) for i in data[::]]
    sega.sort(reverse=True)
    gate=N
    j=[]
    for i in range(len(sega)):
        if gate==sega[i]:
            j=j+[sega[i]]
            return j
        else:
            if sega[i]<=gate:
                j=j+[sega[i]]
                gate-=sega[i]

a=gavedata(input().split(),int(input()))
print(a)