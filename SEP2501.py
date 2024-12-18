def inputs () :
    Triangle=[int(input()),int(input()),int(input())]#三角形邊長輸入
    Triangle=sorted(Triangle)#重新排列
    a,b,c=Triangle[0],Triangle[1],Triangle[2]
    return a,b,c

def is_Triangle (a,b,c):
    if a+b<=c :#三角形基本條件判斷
        print('Not Triangle')
    else :
        Type_Triangle(a,b,c)


def Type_Triangle (a,b,c):
    if a==c :#正三角
        print('Equilateral Triangle')
    if a==b or b==c :#等腰三角形
        print('Isosceles Triangle')
    if a**2+b**2<c**2 :#鈍角
        print('Obtuse Triangle')
    elif a**2+b**2>c**2 :#銳角
        print('Acute Triangle')
    else :#直角
        print('Right Triangle')

def main ():
    a,b,c=inputs()
    is_Triangle(a,b,c)

main()