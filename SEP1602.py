import math
a=int(input())
b=int(input())
c=int(input())
S=(b**2-4*a*c)
if S<0 :#虛根時
    R=(-b)/(2*a)
    I=math.sqrt(-S)/(2*abs(a))
    print('%.1f+%.1fi\n%.1f-%.1fi' %(R,I,R,I))
elif S==0 :#重根時
    R=(-b)/(2*a)
    print('%.1f' %R)
else :#有兩解時
    x1=((-b)+math.sqrt(S))/(2*a)
    x2=((-b)-math.sqrt(S))/(2*a)
    print('%.1f\n%.1f' %(x1,x2))