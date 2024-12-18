def input_normal():
    x=input()
    if x=='-1':
        return []
    else:
        return [x]+input_normal()
    
def data_int(data,n):
    if n==1:
        return int(data[n-1])
    else:
        return 2*data_int(data,n-1)+int(data[n-1])

def main():
    data=input_normal()
    for i in range(len(data)):
        n=len(data[i])
        num=data_int(data[i],n)
        bonus=0
        times=func(num,bonus)
        result=transtype(times,0)
        print(result)

def func(num,data):
    if num==0 or num==1:
        return data
    else:
        data+=1
        return func(num//2,data) if num%2==0 else func((num+1)//2,data)
    
def transtype(times,ect):
    if (times==0 or times==1) and ect==4:
        return ''
    else:
        return transtype(times//2,ect+1)+str(times%2)

main()