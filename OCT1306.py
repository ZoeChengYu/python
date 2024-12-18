def data_size_definition():
    data=list([] for i in range(int(input())))
    return data
    
def Class_data_definition():
    main=[input()]
    main=main+list(input() for i in range(int(input())))
    return main

def Class_date_judge(text,flag):
    data=text
    list_data=list(data)
    for i in range(1,6):
        if int(list_data[0])== i:
            S=Class_time_judge(data,list_data,flag)
            return S
    return 0
    

def Class_time_judge(data,list_data,flag):
    true_data=['1','2','3','4','5','6','7','8','9','a','b','c']
    for i in range(len(true_data)):
        if list_data[1]==true_data[i]:
            return 1
    return 0

def data_full():
    data=data_size_definition()
    for i in range(len(data)):
        data[i]=Class_data_definition()
    return data

def Error():
    print(-1)

def pair(data,LV1,LV2,LV3,LV4,flag):
    if data[LV1][LV2]==data[LV3][LV4]:
        flag*=0
        print('%s,%s,%s' %(data[LV1][0],data[LV3][0],data[LV1][LV2]))
    return flag

def pair_LV4(data,LV1,LV2,LV3,flag):
    for LV4 in range(1,len(data[LV3])):
        flag=pair(data,LV1,LV2,LV3,LV4,flag)
    return flag

def pair_LV3(data,LV1,LV2,flag):
    for LV3 in range(LV1+1,len(data)):
        flag=pair_LV4(data,LV1,LV2,LV3,flag)
    return flag

def pair_LV2(data,LV1,flag):
    for LV2 in range(1,len(data[LV1])):
        flag=pair_LV3(data,LV1,LV2,flag)
    return flag

def pair_LV1(data):
    flag=1
    for LV1 in range(len(data)-1):
        flag=pair_LV2(data,LV1,flag)
    if flag==1:
        print('correct')

def main():
    data=data_full()
    flag=1
    for i in range(len(data)):
        flag=next_leval(data,i,flag)
    if flag ==0:
        Error()
    else:
        pair_LV1(data)
    
def next_leval(data,i,flag):
    for j in range(1,len(data[i])):
        flag=flag*Class_date_judge(data[i][j],flag)
    return flag
        
main()