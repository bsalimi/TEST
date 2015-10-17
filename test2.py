__author__ = 'ThKiller'
__author__ = 'ThKiller'
import math

result=dict()
size=10

def checkforthree(ass):
    trues=0
    for i in range(0,size):
        if ass[i]=='1':
            trues=trues+1
    if trues>=3:
        return 1
    else: return 0



def satstatement1(ass):
  #if ass[0]=="1" or  (ass[1]=="1" and ass[2]=="1"):
  #if ass[0]=="1" and ((ass[1]=="1" or ass[2]=="1")):
  # if (ass[0]=="1" and ass[1]=="1" and ass[2]=="1")):
  if (ass[0]=="1" and ( ass[1]=="1" or ass[2]=="1")) or  (ass[3]=="1" and ass[4]=="1") :
  if (ass[1]=='1' or(ass[0]=='1'))

      return 1
  else: return 0

def countCounters(ass):
    for i in range(0,size):
      if ass[i]=="1":
        x=int(ass,2)
        y=math.pow(2,size-i-1)
        z=x-int(y)
        ass1=bin(z)[2:].zfill(size)
        if satstatement1(ass1)==0:
           if i in result.keys():
                result[i]=result[i]+1
                if i==3:
                    print('t'+str(i)+":"+ass,""+ass1)
                print x,y,z,i
           else: result.update({i:1})

modelount=0
for x in range(0, int(math.pow(2,size))):
    ass= bin(x)[2:].zfill(size)
    print(ass)
    if satstatement1(ass)==1:
        modelount=modelount+1
        countCounters(ass)

    #print ass

for i in result.keys():
        print('t'+str(i)+":"+str(result[i]))


for i in range(0,5):
    print(i)