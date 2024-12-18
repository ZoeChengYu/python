def data():
    mdata=[input().split() for i in range(4)]
    for i in range(4):
        for j in range(len(mdata[i])):
            mdata[i][j]=int(mdata[i][j])
    return mdata

def mini(moon):
    for i in range(len(moon)):
        if 0 in moon[i]:
            return False
    return True

def star(moon):
    if mini(moon):
        return moon
    else:
        for i in range(len(moon)):
            for j in range(len(moon[i])):
                if moon[i][j]==0:
                    moon[i][j]=sun(moon,i,j)
        return star(moon)

def sun(moon,i,j):
    euro=[1,2,3,4]
    for k in range(len(moon[i])):
        if moon[i][k] in euro:
            euro.remove(moon[i][k])
    for k in range(len(moon)):
        if moon[k][j] in euro:
            euro.remove(moon[k][j])
    if i%2==0:
        l=i+1
    else:
        l=i-1
    if j%2==0:
        m=j+1
    else:
        m=j-1
    if moon[l][m] in euro:
        euro.remove(moon[l][m])
    if len(euro)==0:
        print('ERROR')
    elif len(euro)==1:
        return euro[0]
    else:
        return 0

def splitlist(moon):
    for i in range(len(moon)):
        for j in range(len(moon[i])):
            print(moon[i][j],end='')
            if i==(len(moon)-1) and j==(len(moon)-1):
                print('',end='')
            elif j ==(len(moon[i])-1):
                print()
            else:
                print(' ',end='')   

def main():
    moon=data()
    world=star(moon)
    splitlist(world)

    

main()