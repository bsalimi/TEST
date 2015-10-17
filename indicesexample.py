__author__ = 'ThKiller'

__author__ = 'ThKiller'
import math



def satstatement1(ass):
 # if ass[0]=="1" or  (ass[1]=="1" and ass[2]=="1") or  (ass[3]=="1" and ass[4]=="1" and ass[5]=="1"):
  if (ass[0]=="1"  or  (ass[1]=="1" and ass[2]=="1")) or (ass[4]=="1" and ass[3]=="1"):
      return 1
  else: return 0

def countCounters(ass):
  for i in (0,1,2,3,4):
      print("IIIIIIIIIIII",i,ass[i])
      if ass[i]=="1":
        x=int(ass,2)
        #print("x",x)xaaaa
        #print("i",i)
        y=math.pow(2,(5-i))
        z=x-int(y)
        #print("y",y)
        #print("z",z)
        ass1=bin(z)[2:].zfill(6)
        #print "vertex",i, "org", ass, "counter", ass1, "res", satstatement1(ass1)
        if satstatement1(ass1)==0:
           print ass
           dict[i]=dict[i]+1
           print dict

modelount=0
for x in range(0, 64):
    ass= bin(x)[2:].zfill(6)
    if satstatement1(ass)==1:
        modelount=modelount+1
        countCounters(ass)

    #print ass

print dict
print dict,modelount

