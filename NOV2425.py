def inputs():
    N=int(input())
    Lv=int(input())
    poka=[input() for i in range(N)]
    return poka,Lv,N

def find_keyword(data):
    up=['(','[','{']
    down=[')',']','}']
    stable=[]
    for i in range(len(data)):
        if data[i] in up:
            stable.append(data[i])
        if data[i] in down:
            if data[i]==')' and stable[-1]=='(':
                stable.pop(-1)
            elif data[i]==']' and stable[-1]=='[':
                stable.pop(-1)
            elif data[i]=='}' and stable[-1]=='{':
                stable.pop(-1)
            else:
                stable.insert(0,data[i])
    return stable

def find_answer(data,Lv):
    regist=''
    uper=['(','[','{']
    down=[')',']','}']
    Lv_now=0
    for i in range(len(data)):
        if data[i] in uper:
            Lv_now+=1
        elif data[i] in down:
            Lv_now-=1
        elif Lv_now==Lv:
            regist+=data[i]
        else:
            regist+=''
    if regist=='':
        print('EMPTY')
    else:
        print(regist)

def main():
    data,Lv,N=inputs()
    for i in range(N):
        if N>=1 and N<=3 and len(data[i])>=1 and len(data[i])<=50 and Lv>=1 and Lv<=6:
            point=find_keyword(data[i])
            if point != []:
                print('fail')
            else:
                print('pass',end=',')
                find_answer(data[i],Lv)
        else:
            print('fail')

main()