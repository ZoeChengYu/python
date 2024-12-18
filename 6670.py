def mySum(m, n):
    i=m
    sumValue = 0
    while (i <= n):
        sumValue = sumValue + i
        i=i+1
    print(sumValue)
    return sumValue

def main():
    minValue = int(input("Input a min number:"))
    maxValue = int(input("Input a max number:"))
    main_sum = mySum(minValue, maxValue)
    print('sum (%d %d)= %d' %(minValue, maxValue, main_sum))
main()