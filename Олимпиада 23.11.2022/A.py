a=open("input.txt")
b=list(a)
a.close()
b=list(map(int,b))
b.sort()
cmax=b[-1]*b[-2]*b[-3]
cmin=b[0]*b[1]*b[-1]
print(max(cmax,cmin))
    