def strsp(data,N):
    wordlist=[]
    for i in range(1,1<<len(data)):
        if len(listdata(data,i))==N:
            wordlist.append(listdata(data,i))
    return wordlist

def listdata(data,index):
    box=''
    for j in range(len(data)):
        if index & (1<<j):
            box+=(data[j])
    return box

print(strsp('0123456789',4))