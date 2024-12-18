def data():
    n=inputs(0)
    m=inputs(0)
    a=inputs(0)
    b=inputs(1)
    c=inputs(0)
    d=inputs(1)
    return n,m,a,b,c,d

def inputs(t):
    if t==0:
        n=int(input())
    else:
        n=float(input())
    return n

def base(n,m,a,b,c,d):
    lilab=[[0,0,0,0]]
    for i in range(m):
        x=((b/c)*(1-d))
        y=int(lilab[i][1]*x)
        if i == 0:
            lilab.append([i+1,lilab[i][1]+a,a,0])
        elif lilab[i][1]+y>=n*(1-d):
            if i<c:
                lilab.append([i+1,int(n*(1-d)),int(n*(1-d)-lilab[i][1]),0])
            else:
                lilab.append([i+1,int(lilab[i][1]-lilab[i-c+1][2]),0,lilab[i-c+1][2]])
                d+=lilab[i-c+1][2]/n
        else:
            if i<c:
                lilab.append([i+1,lilab[i][1]+y,y,0])
            else:
                lilab.append([i+1,lilab[i][1]+y-lilab[i-c+1][2],y,lilab[i-c+1][2]])
                d+=lilab[i-c+1][2]/n
    return lilab[1:]

def outputs(timeline):
    people=0
    for i in range(len(timeline)):
        people+=timeline[i][2]
        timelineoutput(timeline,i)
        print()
    print(people)

def timelineoutput(timeline,i):
    for j in range(4):
        print(timeline[i][j],end=' ')

def main():
    n,m,a,b,c,d=data()
    timeline=base(n,m,a,b,c,d)
    outputs(timeline)

main()