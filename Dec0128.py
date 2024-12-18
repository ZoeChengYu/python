def inputer():
    base=int(input())
    ball=int(input())
    seto=[]
    for u in range(2):
        seto.append(bouns(base))
    ssd=input().split()
    return seto,ssd

def bouns(base):
    iso=input().split()
    vol=[['0' for i in range(base)] for j in range(base)]
    for i in range(base):
        for j in range(base):
            vol[i][j]=iso[i*base+j]
    return vol

def laplus(data,lists):
    ghost=[[(0*i) for i in range(len(data[j]))]for j in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in lists:
                ghost[i][j]=1
    line=linecount(ghost)
    mix=[[(int(data[i][j])*ghost[i][j])for j in range(len(data[i]))]for i in range(len(data))]
    return line

def linecount(ghost):
    line=0
    positive=1
    nagetive=1
    for i in range(len(ghost)):
        row=1
        column=1
        for j in range(len(ghost[i])):
            row*=ghost[i][j]
            column*=ghost[j][i]
        line+=(row+column)
        positive*=ghost[i][i]
        nagetive*=ghost[i][-i-1]
    line+=(positive+nagetive)
    return line

def main():
    line=[0,0]
    data,lists=inputer()
    for i in range(2):
        line[i]=laplus(data[i],lists)
    if line[0]>line[1]:
        print('A Win')
    elif line[1]>line[0]:
        print('B Win')
    else:
        print('Tie')

main()