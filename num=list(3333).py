class Solution(object):
    def intToRoman(self, num):
        num_f=list(str(num))
        num=[0,0,0,0]
        for i in range(len(num_f)):
            num[-i-1]=int(num_f[-i-1])
        data=''
        data+=('M'*num[0])
        if num[1]==9:
            data+='CM'
        elif num[1]==4:
            data+='CD'
        else:
            data+='D'*(num[1]//5)
            data+='C'*(num[1]%5)
        if num[2]==9:
            data+='XC'
        elif num[2]==4:
            data+='XL'
        else:
            data+='L'*(num[2]//5)
            data+='X'*(num[2]%5)
        if num[3]==9:
            data+='IX'
        elif num[3]==4:
            data+='IV'
        else:
            data+='V'*(num[3]//5)
            data+='I'*(num[3]%5)
        return data
    
print(Solution().intToRoman(389))