def singn(n):
    for i in range(n):
        for j in range(n-i):
            print((n-j)*2-1,end='')
        for k in range(i):
            print('$',end='')
        print()

#singn(int(input()))
singn(5)