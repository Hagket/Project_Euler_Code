#Problem 3#
factors=[]
primefactors=[]
nonprimefactors=[]

def primefactorfinder(x):
  flag=False
  if x>1:
    for i in range(2,x):
      if (x%i==0):
        flag=True
        break

  if flag:
    nonprimefactors.append(x)
  else:
    primefactors.append(x)

def factorfinder(x):
  for i in range(1,x+1):
    if x%i==0:
      factors.append(i)
      primefactorfinder(i)

factorfinder(600851475143)
print("Factors of the given number: " + str(factors))
print("Non-prime factors of the given number: " + str(nonprimefactors))
print("Prime factors of the given number: " + str(primefactors))