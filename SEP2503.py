def ins() :
    Class_All=[[int(input()),int(input()),int(input())],[int(input()),int(input()),int(input())],[int(input()),int(input()),int(input())]]
    Class_All=sorted(Class_All)
    for x in range(0,2):
        if Class_All[x][1]>Class_All[x][2]:
            regist=Class_All[x][2]
            Class_All[x][2]=Class_All[x][1]
            Class_All[x][1]=regist
    '''
    Line 4~8 將各主矩陣內的矩陣由小到大重新排列
    '''
    return Class_All

def compare(All_Class) :
    flag = 0#錯誤旗標，當flag=0時，代表無衝堂，當flag=1時，則代表發生衝堂了
    for a in (0,1):
        flag=call_b(All_Class,a)
    return flag

def call_b(All_Class,a):
    for b in (1,2):
        flag=call_c(All_Class,a,b)
    return flag

def call_c(All_Class,a,b):
    for c in (1,2) :
        flag=call_d(All_Class,a,b,c)
    return flag

def call_d(All_Class,a,b,c):
    for d in (1,2):
        if (All_Class[a][c] == All_Class[b][d])and(All_Class[a][0]!=All_Class[b][0]):#避免自己衝自己堂
            flag=1
            print('%d and %d conflict on %d' %(All_Class[a][0],All_Class[b][0],All_Class[a][c]))
    return flag

def outs(flag):
    if flag ==0:
        print('correct')
    return 0

def main() :
    All_Class=ins()
    flag=compare(All_Class)
    outs(flag)

main()