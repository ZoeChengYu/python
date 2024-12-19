def inputsut():
    gift=input().split()
    gift[-1]=gift[-1].split(',')
    gift[-1][-1]=gift[-1][0][0:5]+gift[-1][-1]
    serve=gift[:-1]
    time=gift[-1][:]
    data=[input().split() for _ in range(int(input()))]
    return serve,time,data

def checkprice(iten,prise):
    '''
    prise_special=prise[0]
    prise_grand=prise[1]
    prise_1=prise[2:]
    prise_2=[i[1:] for i in prise[2:]]
    prise_3=[i[2:] for i in prise_1]
    prise_4=[i[3:] for i in prise_1]
    prise_5=[i[4:] for i in prise_1]
    prise_6=[i[5:] for i in prise_1]
    '''
    if iten[0] in prise[0]:
        return 'Special',10000000
    elif iten[0] in prise[1]:
        return 'Grand',2000000
    elif iten[0] in prise[2:]:
        return '1st',200000
    elif iten[0][1:] in [i[1:] for i in prise[2:]]:
        return '2nd',40000
    elif iten[0][2:] in [i[2:] for i in prise[2:]]:
        return '3rd',10000
    elif iten[0][3:] in [i[3:] for i in prise[2:]]:
        return '4th',4000
    elif iten[0][4:] in [i[4:] for i in prise[2:]]:
        return '5th',1000
    elif iten[0][5:] in [i[5:] for i in prise[2:]]:
        return '6th',200
    else:
        return ' did not win anything.',0

def main():
    shop={}
    buy={}
    prise,time,data=inputsut()
    for iten in data:
        if len(iten[0])!=8:
            print(iten[0]+' has an invalid format.')
        elif time[0] in iten[2] or time[1] in iten[2]:
            prive,number=checkprice(iten,prise)
            if prive ==' did not win anything.':
                print(iten[0]+prive)
            else:
                print(iten[0]+' won: '+prive+' Prize: '+str(number)+' TWD Profit: '+str(number-int(iten[3]))+' TWD')
                shop[iten[1]]=(shop.get(iten[1],0)+1)
                buy[(number-int(iten[3]))]=buy.get((number-int(iten[3])),[])+iten
        else:
            print(iten[0]+' is outside the prize period.')
    if shop!={}:
        shops=sorted(shop.items(),key=lambda x:x[1],reverse=True)
        buyer=sorted(buy.items(),reverse=True)
        print('Store '+shops[0][0]+' opened the most winning invoices: '+str(shops[0][1]))
        print('Invoice with the highest profit: '+buyer[0][1][0]+', from store '+buyer[0][1][1]+', purchase date '+buyer[0][1][2]+', total prize '+str(buyer[0][0]+int(buyer[0][1][3]))+' TWD, profit '+str(buyer[0][0])+' TWD')
    else:
        print('No invoices won any prize.')

main()