def instart():
    xp=input().split()
    sleep=[int(i) for i in input().split()]

    n=int(xp[0])
    start=int(xp[1])
    end=int(xp[2])

    rood=dict()
    for _ in range(n):
        top,tail=input().split()
        top=int(top)
        tail=int(tail)
        if top not in rood:
            rood[top]=[]
        if tail not in rood:
            rood[tail]=[]
        rood[top].append(tail)
        rood[tail].append(top)

    ans=9999
    ans_path=[]
    rest_position=0
    
    for slept in sleep:
        count,pach=findpach(rood,start,end,slept)
        if (count!=-1) and len(pach)<ans:
            ans_path=[int(i) for i in pach]
            rest_position=slept
            ans=len(pach)
    return rest_position,ans_path
    
def findpach(rood,start,end,middle):
    queue=[[start]]
    visit=[]
    findmidflag=False

    while queue:
        path=queue.pop()
        node=path[-1]
        if node not in visit:
            for neighbol in rood[node]:
                if neighbol in visit:
                    continue
                if neighbol == middle:
                    queue.clear()
                    cur_pach=path+[neighbol]
                    queue.append(cur_pach)
                    findmidflag=True
                    break
                cur_pach=path+[neighbol]
                queue.append(cur_pach)

                if findmidflag==True:
                    if neighbol==end:
                        return len(cur_pach)-1,cur_pach
            visit.append(node)
    return -1,None

def main():
    rest,lap=instart()
    if rest==0:
        print('NO')
    else:
        print(rest)
        for i in lap:
            print(i,end=' ')

main()