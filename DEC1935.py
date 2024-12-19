def inputer_1():
    top={'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15', 'G': '16', 'H': '17', 'I': '34', 'J': '18', 'K': '19', 'L': '20', 'M': '21', 'N': '22', 'O': '35', 'P': '23', 'Q': '24', 'R': '25', 'S': '26', 'T': '27', 'U': '28', 'V': '29', 'W': '32', 'X': '30', 'Y': '31', 'Z': '33'}
    numlist=''
    unit=input()
    huge=set(chr(ord('A')+i) for i in range(26))
    if unit[0] not in huge:
        return 'Wrong area code'
    elif unit[1] not in '12':
        return 'Wrong gender code'
    else:
        for j in unit:
            numlist+=top[j]
        data=numlist[0:-1]
        chip=int(numlist[-1])
        ssum=sum(list(map(lambda a,b:int(a)*int(b),list(data),[1,9,8,7,6,5,4,3,2,1])))
        K=(10-(ssum%10))%10
        if K==chip:
            return 'Pass'
        else:
            return 'Illegal'
    

def checkpassword(data,num):
    qer=len(list(filter(lambda x:True if x in num else False,data)))
    gate=1
    for i in range(len(data)-1):
        if data[i] in num and data[i+1] in num:
            gate*=0
    if gate==0 or qer<5:
        return 0
    else:
        return 15


def inputer_2():
    data=input()
    small=set(chr(ord('a')+i) for i in range(26))
    huge=set(chr(ord('A')+i) for i in range(26))
    num=set(chr(ord('0')+i) for i in range(10))
    spword=set(list('([{?/-:;,. ~!@#$%^&*<>_+=}])'))
    bonuspoint=checkpassword(data,num)
    smallpoint=len(list(filter(lambda x:True if x in small else False,data)))
    hugepoint=len(list(filter(lambda x:True if x in huge else False,data)))*3
    numpoint=len(list(filter(lambda x:True if x in num else False,data)))*2
    spwordpoint=len(list(filter(lambda x:True if x in spword else False,data)))*5
    point=bonuspoint+smallpoint+hugepoint+numpoint+spwordpoint
    return point

def main():
    numlist=inputer_1()
    point=inputer_2()
    print(numlist)
    print(point,end='')
    if point<30:
        print(' Not strong enough')

main()