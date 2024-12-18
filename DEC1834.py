def inport():
    top=input()
    bottom=input().split()
    data=input()
    return top,bottom,data

def findanswer(top,bottom,data:str,result:list):
    if len(data)>7:
        for i in range(len(data)-7):
            if data[i:i+4] in top:
                for j in range(i+4,len(data)):
                    if data[j:j+3] in bottom:
                        result.append(data[i+4:j])
                        sega=data[j+3:]
                        return findanswer(top,bottom,sega,result)
    else:
        return

def printresult(result):
    num=sorted(result,key=lambda x:x[::])
    monkey=sorted(num,key=lambda y:len(y))
    for i in monkey:
        print(i)

def main():
    top,bottom,data=inport()
    result=[]
    findanswer(top,bottom,data,result)
    if result==[]:
        print('No gene')
    else:
        printresult(result)

main()