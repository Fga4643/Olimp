a=open("input.txt")
b=int(list(a)[0])
a.close()
tyui=0
for i1 in ["","+","-"]:
    for y2 in ["","+","-"]:
        for i3 in ["","+","-"]:
            for i4 in ["","+","-"]:
                for i5 in ["","+","-"]:
                    for i6 in ["","+","-"]:
                        for i7 in ["","+","-"]:
                            for i8 in ["","+","-"]:
                                d=[i1,y2,i3,i4,i5,i6,i7,i8]
                                dop=list()
                                dei=list()
                                rt=1
                                for i2 in range(2,10):
                                    if d[i2-2]=="":
                                        rt=rt*10+i2
                                    elif d[i2-2]=="+":
                                        dei.append("+")
                                        dop.append(rt)
                                        rt=i2
                                    elif d[i2-2]=="-":
                                        dei.append("-")
                                        dop.append(rt)
                                        rt=i2
                                dop.append(rt)
                                rt=0
                                rt+=dop[0]
                                for y4 in range(len(dei)):
                                    if dei[y4]=="+":
                                        rt=rt+dop[y4+1]
                                    else:
                                        rt=rt-dop[y4+1]
                                if rt==b:
                                    tyui+=1
print(tyui)