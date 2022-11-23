def put(carta,nach,kon,rel,hid,kol,relic,res):
                print(hid)
                hod=[]
                hod+=hid
                if hod[0]<=rel[0] and hod[1]==rel[1] and relic==False and hod[0]<len(carta):
                                if carta[hod[0]+1][hod[1]]!="#":
                                                if carta[hod[0]+1][hod[1]]=="R":
                                                                relic=True                                                
                                                kol+=1
                                                hod[0]+=1
                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid                
                if hod[0]==rel[0] and hod[1]<=rel[1] and relic==False and hod[1]<len(carta[1]):
                                if carta[hod[0]][hod[1]+1]!="#":
                                                if carta[hod[0]][hod[1]+1]=="R":
                                                                relic=True                                                
                                                kol+=1
                                                hod[1]+=1
                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid        
                if hod[0]==rel[0] and hod[1]>=rel[1] and relic==False and hod[1]>0:
                                if carta[hod[0]][hod[1]-1]!="#":
                                                if carta[hod[0]][hod[1]-1]=="R":
                                                                relic=True                                                
                                                kol+=1
                                                hod[1]-=1
                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid       
                if hod[0]>=rel[0] and hod[1]==rel[1] and relic==False and hod[0]>0:
                                if carta[hod[0]-1][hod[1]]!="#":
                                                if carta[hod[0]-1][hod[1]]=="R":
                                                                relic=True                                                
                                                kol+=1
                                                hod[0]-=1
                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid       
                if hod[0]<=rel[0] and hod[1]<=rel[1] and relic==False and hod[0]<len(carta) and hod[1]<len(carta[1]):
                                if carta[hod[0]+1][hod[1]+1]!="#":
                                                if carta[hod[0]+1][hod[1]+1]=="R":
                                                                relic=True                                                
                                                kol+=1
                                                hod[1]+=1
                                                hod[0]+=1
                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid          
                if hod[0]>=rel[0] and hod[1]>=rel[1] and relic==False and hod[0]>0 and hod[1]>0:
                                if carta[hod[0]-1][hod[1]-1]!="#":
                                                if carta[hod[0]-1][hod[1]-1]=="R":
                                                                relic=True                                                
                                                kol+=1
                                                hod[1]-=1
                                                hod[0]-=1
                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid       
                if hod[0]<=rel[0] and hod[1]>=rel[1] and relic==False and hod[1]<len(carta[0]) and hod[0]>0:
                                if carta[hod[0]-1][hod[1]+1]!="#":
                                                if carta[hod[0]-1][hod[1]+1]=="R":
                                                                relic=True                                                
                                                kol+=1
                                                hod[1]+=1
                                                hod[0]-=1
                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid          
                if hod[0]>=rel[0] and hod[1]==rel[1] and relic==False and hod[0]<len(carta) and hod[1]>0:
                                if carta[hod[0]+1][hod[1]-1]!="#":
                                                if carta[hod[0]+1][hod[1]-1]=="R":
                                                                relic=True
                                                kol+=1
                                                hod[1]-=1
                                                hod[0]+=1   
                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid         
                                                
                                                
                if hod[0]<=kon[0] and hod[1]==kon[1] and relic==True and hod[0]<len(carta):
                                if carta[hod[0]+1][hod[1]]!="#":
                                                kol+=1
                                                if carta[hod[0]+1][hod[1]]=="E":
                                                                res.append(kol)
                                                else:
                                                                hod[0]+=1
                                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid       
                if hod[0]==kon[0] and hod[1]<=kon[1] and relic==True and hod[1]<len(carta[1]):
                                if carta[hod[0]][hod[1]+1]!="#":
                                                kol+=1
                                                if carta[hod[0]][hod[1]+1]=="E":
                                                                res.append(kol)                                               
                                                else:
                                                                hod[1]+=1
                                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid           
                if hod[0]==kon[0] and hod[1]>=kon[1] and relic==True and hod[1]>0:
                
                                if carta[hod[0]][hod[1]-1]!="#":
                                                kol+=1
                                                if carta[hod[0]][hod[1]-1]=="E":
                                                                res.append( kol)                                             
                                                else:
                                                                hod[1]-=1
                                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid       
                if hod[0]>=kon[0] and hod[1]<=kon[1] and relic==True and hod[0]>0 and hod[1]<len(carta[1]):
                                
                                if carta[hod[0]-1][hod[1]+1]!="#":
                                                kol+=1
                                                if carta[hod[0]-1][hod[1]+1]=="E":
                                                                res.append( kol )                                                 
                                                else:
                                                                hod[0]-=1
                                                                hod[1]+=1
                                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid       
                if hod[0]<=kon[0] and hod[1]<=kon[1] and relic==True and hod[0]<len(carta) and hod[1]<len(carta[1]):
                                if carta[hod[0]+1][hod[1]+1]!="#":
                                                kol+=1
                                                if carta[hod[0]+1][hod[1]+1]=="E":
                                                                res.append( kol   )                                               
                                                else:
                                                                hod[1]+=1
                                                                hod[0]+=1
                                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid          
                if hod[0]>=kon[0] and hod[1]>=kon[1] and relic==True and hod[0]>0 and hod[1]>0:
                                if carta[hod[0]-1][hod[1]-1]!="#":
                                                kol+=1
                                                if carta[hod[0]-1][hod[1]-1]=="E":
                                                                res.append( kol)
                                                else:
                                                                hod[1]-=1
                                                                hod[0]-=1
                                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid       
                if hod[0]<=kon[0] and hod[1]>=kon[1] and relic==True and hod[1]>0 and hod[0]>len(carta):
                                if carta[hod[0]+1][hod[1]-1]!="#":
                                                kol+=1
                                                if carta[hod[0]+1][hod[1]-1]=="E":
                                                                res.append( kol) 
                                                else:
                                                                hod[1]-=1
                                                                hod[0]+=1
                                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)
                hod=[]
                hod+=hid          
                if hod[0]>=kon[0] and hod[1]==kon[1] and relic==True and hod[0]<len(carta) and hod[1]>0:
                                if carta[hod[0]+1][hod[1]-1]!="#":
                                                kol+=1
                                                if carta[hod[0]+1][hod[1]-1]=="E":
                                                                res.append( kol) 
                                                else:
                                                                hod[1]-=1
                                                                hod[0]+=1   
                                                                res+=put(carta,nach,kon,rel,hod,kol,relic,res)    
                return res
                                
                

a=open("input.txt")
x,y=map(int,a.readline().split("\n")[0].split())
carta=[]
maximalka=x*y
for i in range(y):
                carta.append(list(a.readline().split("\n")[0]))
a.close()
for i1 in range(y):
                for i2 in range(x):
                                
                                if carta[i1][i2]=="L":
                                                nach=[i1,i2]
                                elif carta[i1][i2]=="R":
                                                rel=[i1,i2]
                                elif carta[i1][i2]=="E":
                                                kon=[i1,i2]
hid=nach
kol=0
relic=False
res=[]
print(put(carta,nach,kon,rel,hid,kol,relic,res))