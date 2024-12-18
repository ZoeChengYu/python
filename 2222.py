def getNum(nums: list, index: int)->list:
    subset = ''
    for j in range(len(nums)):
    # 如果第 j 位是 1,表示選擇 nums[j]
        if index & (1 << j):
            subset+=(nums[j])
    return subset

def test00(keys,N):
    juge=[]
    for i in range(1, 1<<len(keys)):
        if len(getNum(keys, i))==N:
            juge.append(getNum(keys, i))
    print(juge)

test00('abcdef',2)