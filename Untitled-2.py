class Solution(object):
    def intToRoman(self, num):
        M_num=num//1000
        num=num%1000
        D_num=num//500
        num=num%500
        C_num=num//100
        num=num%100
        L_num=num//50
        num=num%50
        X_num=num//10
        num=num%10
        V_num=num//5
        num=num%5
        I_num=num
        data=''
        data+=('M'*M_num)
        if D_num==1 and C_num==4:
            data+='CM'
        elif C_num==4:
            data+='CD'
        else:
            data+='D'*D_num
            data+='C'*C_num
        if L_num==1 and X_num==4:
            data+='XC'
        elif X_num==4:
            data+='XL'
        else:
            data+='L'*L_num
            data+='X'*X_num
        if V_num==1 and I_num==4:
            data+='IX'
        elif I_num==4:
            data+='IV'
        else:
            data+='V'*V_num
            data+='I'*I_num
        return data
    
print(Solution().intToRoman(389))