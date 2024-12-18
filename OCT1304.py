def data_base():
    data=str(input())
    data_list=data.split()
    for time in range(len(data_list)):
        data_list[time]=int(data_list[time])
    return data_list

def find_prime_number(list_data):
    Ans=[]
    flag_A=0
    for num in range(len(list_data)):
        flag_B=1
        for test in range(2,int(list_data[num]**0.5+1),1):
            if((list_data[num]% test==0) or (list_data[num]== 1)):
                flag_A += 0
                flag_B *= 0
            else:
                flag_A += 1
                flag_B *= 1
                
                    
        if flag_B==1 and list_data[num] != 1:
            Ans=Ans+[list_data[num]]
        Ans.sort()
    if Ans==[]:
        return 'No prime number'
    else:
        return Ans
    
            
 
def main():
    data=data_base()
    print(find_prime_number(data))
    
main()