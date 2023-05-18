#Problem 10#
primenumbers=[]
def primefinder(x):
  flag=False
  if x>1:
    for i in range(2,x):
      if (x%i==0):
        flag=True
        break

  if (flag==False):
    primenumbers.append(x)

for i in range(1,10):
  primefinder(i)

total=-1
for i in range(0,len(primenumbers)):
  total+= primenumbers[i]
print("The sum of all primes under 2 million: " + str(total))