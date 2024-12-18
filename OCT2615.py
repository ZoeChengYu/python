def str_to_list():
    list_input=list(input())
    data=filter_Tool(list_input)
    return data
    
def filter_Tool(list_input):
    true_data=list(str(i) for i in range(0,10))
    data=[]
    for i in range(len(list_input)):
        data=next_for_in_Tool(list_input,true_data,data,i)
    return data

def next_for_in_Tool(list_input,true_data,data,i):
    for j in range(len(true_data)):
        if list_input[i]==true_data[j]:
            data=data+[int(list_input[i])]
    return data

def determination_tool(data):
    len_num=len(data)
    flag=1
    for i in range(len_num//2+len_num%2):
        if data[i] != data[len_num-1-i]:
            flag *=0
    if flag==1:
        result=list(set(data))
    else:
            data.sort()
            result=find_Duplicate_Values(data)
    return result

def find_Duplicate_Values(data):
    duplicate_datd=[]
    for i in range(len(data)-1):
            if data[i]==data[i+1]:
                duplicate_datd=duplicate_datd+[data[i]]
    
    duplicate_datd=list(set(duplicate_datd))
    duplicate_datd.sort(reverse=True)
    return duplicate_datd

def main():
    data=str_to_list()
    result=determination_tool(data)
    print(result)

main()