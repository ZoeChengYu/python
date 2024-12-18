def input_data():
    data=input().split()
    for i in range(len(data)):
        relay=data[i][0:-1]
        stable=data[i][-1]
        data[i]=[0,0]
        data[i][0]=relay
        data[i][1]=stable
    return data

def debug(data):
    number=list(0 for i in range(len(data)))
    color=list(0 for i in range(len(data)))
    truedata=['A']+list(str(i) for i in range(2,11))+['J','Q','K','S','H','D','C']
    pair_num=pair(data)
    for i in range(len(data)):
        number[i],color[i]=cheek(data,i,truedata)
        if number[i]==0 or color[i]==0:
            return -1
    if pair_num==1:
        return -2
    return 0

def pair(data):
    TV=0
    for i in range(len(data)-1):
        TV=TV+pair_2(data,i)
    if TV == 0:
        return 0
    else:
        return 1

def pair_2(data,i):
    for j in range(len(data)-i-1,i,-1):
        if data[i]==data[j]:
            return 1
    return 0

def cheek(data,i,truedata):
    num=0
    color=0
    for j in range(0,13,1):
        if data[i][0]==truedata[j]:
            num=1
    for j in range(13,17,1):
        if data[i][1]==truedata[j]:
            color=1
    return num,color

def sensor_color(data):#6,9
    set_data=list(set(data[i][1] for i in range(len(data))))
    return (len(set_data)==1)

def sensor_capal(data):
    data_list=list(data[i][0] for i in range(len(data)))
    data_num=list(set(data[i][0] for i in range(len(data))))
    num=len(data_num)
    data_list.sort()
    element=amount_element(data_list,data_num,num)
    if num==4:
        return 'pair'#2
    if num==3:
        if element==3:
            return 'three'#4
        else:
            return 'duo-pair'#3
    if num==2:
        if element==4:
            return 'four'#8
        else:
            return 'three-two'#7
    else:
        return 'singal'#1,5,6,9

def sensor_straight(data):
    test_data=list(data[i][0] for i in range(len(data)))
    truedata=['A']+list(str(i) for i in range(2,11))+['J','Q','K']
    sub=list(0 for i in range(len(test_data)))
    num=0
    for i in range(len(test_data)):
        sub[i]=truedata.index(test_data[i])
    sub.sort()
    if (sub[0]==0 and sub[-1]==12):
        for i in range(len(sub)):
            if sub[i]>8:
                sub[i]-=13
    sub.sort()
    for i in range(len(test_data)):
        test_data[i]=truedata[sub[i]]
    for i in range(13):
        if test_data[0]==truedata[i]:
            if i<=8:
                num=i
            else:
                num=i-13
    return(set([truedata[num],truedata[num+1],truedata[num+2],truedata[num+3],truedata[num+4]])==set(test_data))

def amount_element(data_list,data_num,num):
    data_ship=list(0 for i in range(num))
    for i in range(num):
        data_ship[i]=amount_element_2(data_list,data_num,num,i)
    return max(data_ship)

def amount_element_2(data_list,data_num,num,i):
    amount=0
    for j in range(len(data_list)):
        if(data_list[j]==data_num[i]):
            amount+=1
    return amount

def print_contal(bugcode,data):
    if bugcode==-1:
        return 'Error input'
    elif bugcode==-2:
        return 'Duplicate deal'
    else:
        if sensor_straight(data) and sensor_color(data):
            return 9
        elif sensor_capal(data)=='four':
            return 8
        elif sensor_capal(data)=='three-two':
            return 7
        elif  sensor_color(data):
            return 6
        elif sensor_straight(data):
            return 5
        elif sensor_capal(data)=='three':
            return 4
        elif sensor_capal(data)=='duo-pair':
            return 3
        elif sensor_capal(data)=='pair':
            return 2
        else:
            return 1

def main():
    data=input_data()
    bugcode=debug(data)
    print(print_contal(bugcode,data))

main()