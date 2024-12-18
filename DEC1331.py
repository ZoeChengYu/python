def intdata():
    data=input().split()
    for i in data:
        if ord('f')>=ord(i) and ord(i)>=ord('a'):
            data[data.index(i)]=10+(ord(i)-ord('a'))
        # elif ord('F')>=ord(i) and ord(i)>=ord('A'):
        #     data[data.index(i)]=10+(ord(i)-ord('A'))
        else:
            data[data.index(i)]=int(i)
    return data

def math(data):
    big=max(data)
    small=min(data)
    if len(data)%2==0:
        mid=(data[(len(data)+1)//2]+data[(len(data)-1)//2])//2
    else:
        mid=data[len(data)//2]
    return (big+small+mid)

def outline(sum):
    if sum<10:
        print(sum)
    else:
        return outline(sum//10+sum%10)

def main():
    data=intdata()
    sum=math(data)
    outline(sum)

main()