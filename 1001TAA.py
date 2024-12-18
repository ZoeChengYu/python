def match(s1:str,s2:str)->str:
    a,b=0,0
    for i in range(4):
        if s1[i] == s2[i]:
            a+=1
        elif s1[i] in s2:
            b+=1
    print('%dA%dB' %(a,b))

match('2345','2346')