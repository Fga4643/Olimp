def poisk(carta,nach,maximalka,hod,vzal,hods,proch):
    hod+=1
    if hod<maximalka:
        vers=[]
        vers.append([nach[0]+1,nach[1]])
        vers.append([nach[0]-1,nach[1]])
        vers.append([nach[0],nach[1]+1])
        vers.append([nach[0],nach[1]-1])
        vers.append([nach[0]+1,nach[1]+1])
        vers.append([nach[0]-1,nach[1]-1])
        vers.append([nach[0]+1,nach[1]-1])
        vers.append([nach[0]-1,nach[1]+1])
        for i in vers:
            if not i in proch:
                try:
                    print(hod,i)
                    if carta[i[0]][i[1]]==".":
                        proch.append(i)
                        hods.append(poisk(carta,nach,maximalka,hod,vzal,hods,proch))
                    elif carta[i[0]][i[1]]=="R":
                        proch.append(i)
                        vzal=True
                        hods.append(poisk(carta,nach,maximalka,hod,vzal,hods,proch))
                    elif carta[i[0]][i[1]]=="E":
                        if vzal:
                            hods+=hod
                            print(hods)
                            return hods
                except:
                    pass
a=open("input.txt")
x,y=map(int,a.readline().split("\n")[0].split())
carta=[]
maximalka=x*y
for i in range(y):
    carta.append(list(a.readline().split("\n")[0]))
a.close()
for i1 in range(x):
    for i2 in range(y):
        if carta[i1][i2]=="L":
            hod=0
            vzal=False
            hods=[]
            nach=[i1,i2]
            proch=[]
            print(list(poisk(carta,nach,maximalka,hod,vzal,hods,proch)))
print(fer)
