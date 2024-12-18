def star_mark(n):#印星號的程式
    for i in range(n):
        print('*',end='')

def number_up_mark(n):#上數程式
    for i in range(1,n+1,2):
        print(i,end='')

def Error_messenge():#錯誤輸出
    print('Error')

def number_down_mark(n):#下數程式
    for i in range(n-2,0,-2):
        print(i,end='')

def up_count(n):#上半部控制
    for i in range(n):
        star_mark(n-i-1)
        number_up_mark(2*i+1)
        number_down_mark(2*i+1)
        print()

def down_count(n):#下半部控制
    for i in range(n,0,-1):
        star_mark(n-i+1)
        number_up_mark(2*i-1)
        number_down_mark(2*i-1)
        print()

def print_out_control(N):#總控制
    up_count(N)
    down_count(N-1)
        
def input_control():#輸入端
    input_number=int(input())
    return input_number

def main():#判斷區
    data=input_control()
    if data<=0:
        Error_messenge()
    else:
        print_out_control(data)

main()