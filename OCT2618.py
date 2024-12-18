def input_data():
    nums=input().split()
    target=int(input())
    for i in range(len(nums)):
        nums[i]=int(nums[i])
    return nums,target

def pair_base(nums,target):
    index=[]
    for i in range(len(nums)-1):
        index=pair_advenced(nums,target,i,index)
    return index

def pair_advenced(nums,targer,i,index):
    for j in range(i+1,len(nums)):
        if (nums[i]+nums[j]==targer):
            index=index+[[i,j]]
    return index

def main():
    nums,targer=input_data()
    data=pair_base(nums,targer)
    result=select(data)
    print(result)

def select(data):
    register=[0,[]]
    for i in range(len(data)):
        if (data[i][0]*data[i][1]>register[0]):
            register[0]=data[i][0]*data[i][1]
            register[1]=[data[i][1],data[i][0]]
    return register[1]


main()