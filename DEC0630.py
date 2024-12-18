def inputdata():
    num=int(input())
    data=[input().split() for _ in range(num)]
    put=int(input())
    meta=[(input().split(sep=' + ')) for _ in range(put)]
    suno=int(input())
    for iso in meta:
        for cold in iso:
            meta[meta.index(iso)][iso.index(cold)]=set(cold.split(' '))
    if suno==1:
        xmas=[]
        fos=[]
        for i in range(len(meta)):
            fos.append([mori for kiara in meta[i] for mori in kiara])
            xmas.append(set(fos[i]))
        meta=xmas
    gosed=dict()
    for ict in data:
        gosed[ict[0]]=set(ict[1:])
    return gosed,meta,suno
    
def  odd(school:dict,search:list):
    result=[]
    for monkey in search:
        chat={}
        for god in school.items():
            odd_emo(god,monkey,chat)
        inv=odd_inver(chat)
        inhi=max(inv.items())
        for jack in inhi[1]:
            print(jack,end='')
            if inhi[1].index(jack) != -1:
                print(' ',end='')
        print()
    
def odd_emo(god,monkey,chat:dict):
    for does in god: 
        for banana in monkey:
            if banana in does:
                chat[god[0]]=chat.get(god[0],0)+1

def odd_inver(chat:dict):
    easy={}
    for go,back in chat.items():
        if back not in easy:
            easy[back] =[go]
        else:
            easy[back].append(go)
    return easy

def  even(school,search):
    for dos in search:
        big=[]
        for pive,pove in school.items():
            esf=1
            for ddos in dos:
                poi=1
                for youge in ddos:
                    if youge not in pove:
                        poi*=0
                if poi==1 and esf==1:
                    big.append(pive)
                    esf*=0
        sop=list(big)
        for iso in sop:
            print(iso,end='')
            if sop.index(iso)!=-1:
                print(' ',end='')
        print()
       

def main():
    school,search,types=inputdata()
    if types==1:
        odd(school,search)
    else:
        even(school,search)

main()