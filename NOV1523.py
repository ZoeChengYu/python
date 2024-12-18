def indata():
    data=[input().split() for i in range(3)]
    T=[input(),input(),input()]
    for i in range(3):
        data[i]=deleter(data[i])
    return data,T
    
def deleter(data):
    for i in range(len(data)):
        for j in range(0,i):
            if data[i][1]==data[j][1]:
                del data[i]
                del data[j]
                return deleter(data)
        for j in range(i+1,len(data)):
            if data[i][1]==data[j][1]:
                del data[j]
                del data[i]
                return deleter(data)
    return data

def transcard(data,T):
    for i in range(3):
        if i==0:
            data[i].append(T[i])
            data[i]=deleter(data[i])
            if T[i-1] in data[i]:
                data[i].remove(T[i-1])
            else:
                return 'Error'
        else:
            if T[i-1] in data[i]:
                data[i].remove(T[i-1])
            else:
                return 'Error'
            data[i].append(T[i])
            data[i]=deleter(data[i])
    return data

def spite(result:list):
    if result=='Error':
        print(result)
    else:
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=' ')
            print()

def main():
    data,T=indata()
    result=transcard(data,T)
    spite(result)
    
main()