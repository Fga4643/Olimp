a=open("input.txt")
b=list(a)
a.close()
c=[]
for i in b:
    d=i.split("\n")[0]
    c.append(list(map(int,d.split())))
b=[]
while True:
    c.sort()
    f=True
    d=[]
    b=[]
    for i in range(1,len(c)):
        if c[i-1][0]<=c[i][0] and c[i-1][1]>=c[i][0]:
            f=False
            d.append([[c[i-1][0],c[i-1][1]],[c[i][0],c[i][1]]])
            b.append([min(c[i-1][0],c[i][1]),max(c[i][1],c[i-1][1])])
            break
        elif c[i-1][0]<=c[i][1] and c[i-1][1]>=c[i][1]:
            f=False
            d.append([[c[i-1][0],c[i-1][1]],[c[i][0],c[i][1]]])
            b.append([min(c[i-1][0],c[i][1]),max(c[i][1],c[i-1][1])])   
            break
    if f:
        break
    else:
        for i in range(len(d)):
            try:
                c.remove(d[i][0])
                c.remove(d[i][1])
            except:
                pass
        c+=b
for i in c:
    print(*i)
            