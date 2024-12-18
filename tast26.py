dss=[['w','s','f'],['w','d','s','x'],['r','w'],['a','s'],['w'],['e']]
lendss=[]
result=[]
for i in range(len(dss)):
    lendss.append(len(dss[i]))
maxdss=max(lendss)
for x in range(1,maxdss+1):
    regist=[]
    for i in range(len(dss)):
        if len(dss[i])==x:
            dss[i].sort()
            regist.append(dss[i])
    regist.sort()
    result.append(regist)
for i in range(maxdss):
    for j in range(len(result[i])):
        for k in range(len(result[i][j])):
            if result[i][j][k]==result[i][j][-1]:
                print(result[i][j][k])
            else:
                print(result[i][j][k],end=' ')