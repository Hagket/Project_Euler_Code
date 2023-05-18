#Problem 9#
import math
triples=[]
onektriple=[]
def squarer(b,x):
  while b<=1000:
    if (x==0):
      return 1
    else:
      return b*squarer(b,x-1)
      b+=1

def pythagtrip(a,b):
  c2=squarer(a,2) + squarer(b,2)
  c=math.sqrt(c2)
  if (c-int(c)==0):
    triples.append(a)
    triples.append(b)
    triples.append(c)
    sum=int(a+b+c)
    #print("Sum: " + str(sum))
    if sum==1000:
      onektriple.append(a)
      onektriple.append(b)
      onektriple.append(c)



for i in range(1,500):
  mult=1
  while mult<500:
    pythagtrip(i,mult)
    mult+=1
print(onektriple[0])
print(onektriple[1])
print(onektriple[2])

finalsolution=int(onektriple[0]*onektriple[1]*onektriple[2])
print("The product of the only pythagorean triplet for which a + b + c = 1000 is: " + str(finalsolution))