__author__ = 'ThKiller'
import math

dict = { 1 : 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7:0, 8:0, 9:0};

def satstatement1(ass):
  if ((ass[0]=="1" and  (ass[1]=="1" or ass[2]=="1") )  or (ass[3]=="1" and  (ass[4]=="1" or ass[5]=="1" or  ass[6]=="1")) or  (ass[7]=="1" and  ass[8]=="1")):
      return 1
  else: return 0

375

def countCounters(ass):
  for i in (0,1,2,3,4,5,6,7,8):
      print("IIIIIIIIIIII",i,ass[i])
      if ass[i]=="1":
        x=int(ass,2)
        print("x",x)
        print("i",i)
        y=math.pow(2,(8-i))
        z=x-int(y)
        print("y",y)
        print("z",z)
        ass1=bin(z)[2:].zfill(9)
        print "vertex",i+1, "org", ass, "counter", ass1, "res", satstatement1(ass1)
        if satstatement1(ass1)==0:
           dict[i+1]=dict[i+1]+1
           print dict

modelount=0
for x in range(0, int(math.pow(2,9))):
    ass= bin(x)[2:].zfill(9)
   #  print ass
    if satstatement1(ass)==1:
        modelount=modelount+1
        countCounters(ass)

    #print ass

print dict
print dict,modelount

