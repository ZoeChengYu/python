ans_list=[]

def generate(s:str,M:str):
    if (len(s)==int(M)):
        ans_list.append(s)
        return ans_list
    else:
        for i in range(10):
            if not str(i) in s:
                generate(s+str(i),M)

generate('','4')
print(ans_list)