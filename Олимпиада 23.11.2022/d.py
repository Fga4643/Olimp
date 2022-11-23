def prov(bl,ye,blu,spis,proch):
    qer=[]
    if blu in ye:
        qer.append(False)
        return True
    else:
        if blu in proch or spis[blue]==[]:
            qer.append(False)
            return False
        else:
            ter=spis[blu]
            for i in ter:
                proch.append(blu)
                qer.append(prov(bl,ye,int(i),spis,proch))
    if True in qer:
        return True
    elif False in qer:
        return False
a=open("input.txt")
re=[]
bl=[]
ye=[]
b=int(a.readline().split("\n")[0])
spis=[]
for i in range(b):
    c=a.readline().split("\n")[0]
    spis.append([])
    d=list(map(int,c.split()))
    if d[1]==0:
        re.append(d[0]-1)
    elif d[1]==1:
        bl.append(d[0]-1)
    else:
        ye.append(d[0]-1)
b=int(a.readline().split("\n")[0])
ret=[]
qer=[]
for i in range(b):
    ret=list(map(int,a.readline().split("\n")[0].split()))
    qer.append(ret)
    spis[ret[0]-1].append(ret[1]-1)
res=[]
for red in re:
    for i in spis[red]:
        if i in ye:
            res.append([red+1,i+1])
        if i in bl:
            blue=i
            for i1 in spis[blue]:
                if i1 in ye:
                    res.append([red+1,i+1])
                else:
                    if prov(bl,ye,i1,spis,[]):
                        res.append([red+1,i+1])
for i in qer:
    if i in res:
        print(*i)