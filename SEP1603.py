name=input()
student_num=int(input())
CH_SC=int(input())#國文
Computer_A_SC=int(input())#計算機概論
Computer_Sci_SC=int(input())#計算機程式設計
ST=[name,student_num,CH_SC,Computer_A_SC,Computer_Sci_SC]#學生基本資料
Total=ST[2]+ST[3]+ST[4]
Average=int(Total/3)
print('Name:%s\nId:%d\nTotal:%d\nAverage:%d' %(ST[0],ST[1],Total,Average))