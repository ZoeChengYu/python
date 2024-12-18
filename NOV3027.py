def starlist(n,s,data:list):
    if len(s)==n:
      data.append(s)
      return
    else:
       for i in range(10):
            if str(i) not in s:
                starlist(n,s+str(i),data)

def ABlardor(ssd,data):
    a,b=0,0
    for j in range(len(data)):
        if data[j]==ssd[j]:
            a+=1
        elif data[j] in ssd:
            b+=1
    word=str(a)+'A'+str(b)+'B'
    return word

def chanal(ssd,data):
    result=[]
    if ABlardor(ssd,data[0])=='5A0B':
        print(data[0])
        return
    else:
        av=ABlardor(ssd,data[0])
        for i in range(len(data)):
            if ABlardor(data[0],data[i])==av:
                result.append(data[i])
        chanal(ssd,result)

def main():
    ssd=input()
    data=[]
    starlist(5,'',data)
    chanal(ssd,data)

main()