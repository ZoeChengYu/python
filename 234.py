class Solution(object):
    def intToRoman(self, num):
        num1=Solution().spice(num)
        num=Solution().truetype(num1)
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

    def spice(self,num)->list:
        if num<10:
            return [num]
        else:
            for i in range(len(str(num))):
                x=num//10
                y=num%10
                return Solution().spice(x)+[y]

    def truetype(self,num):
        if len(num)==4:
            return num
        else:
            return Solution().truetype([0]+num)
        
Solution().intToRoman(444)