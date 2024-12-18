def inf():
    cc=input()
    return cc

def happynum(strs:str,data:list):
    lists=list(strs)
    memory=0
    for sd in lists:
        memory+=int(sd)**2
    if memory==1:
        return 'Happy'
    elif memory in data:
        return 'unhappy'
    else:
        data.append(memory)
        return happynum(str(memory),data)

def selfnum(num):
    conum=int(num)
    for i in num:
        conum-=(int(i)**len(num))
    if conum==0:
        return 'myself'
    else:
        return 'not'

def F(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return F(n-1)+F(n-2)

def lab(n):
    if n==1:
        return 1
    else:
        return n*lab(n-1)

def Trans(num):
    nuc=0
    for i in num:
        nuc+=int(i)
    if nuc<10:
        return nuc
    else:
        return Trans(str(nuc))

def main():
    num=inf()
    dos=[]
    fos=happynum(num,dos)
    hos=selfnum(num)
    n=Trans(num)
    if fos=='Happy':
        if hos=='myself':
            print(num+' is both a happy number and a narcissistic number.')
        else:
            print(num+' is a happy number.')
        print('F('+str(n)+') = '+str(F(n)))
    else:
        if hos=='myself':
            print(num+' is a narcissistic number.')
        else:
            print(num+' is neither a happy number nor a narcissistic number.')
        print(str(n)+'! = '+str(lab(n)))

main()
