import math
a=input()
b=input()
c=input()
a=int(a)
b=int(b)
c=int(c)
x1=((-b)+math.sqrt(b**2-4*a*c))/(2*a)
x2=((-b)-math.sqrt(b**2-4*a*c))/(2*a)
if x1==x2 :#當兩者答案相同時，視為同根，只列印一個答案
    print('%.1f' %x1)
else :
    print('%.1f' %x1)
    print('%.1f' %x2)