#Problem 7#
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

for i in range(1,2):
  mult=1
  while mult<=200000:
    num=i*mult
    mult+=1
    primefinder(num)
print("The 10,001th prime number: " + str(primenumbers[10001]))