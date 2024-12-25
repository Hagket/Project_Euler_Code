#Problem 12#
#CODE NEEDS TO BE OPTIMIZED#
  
import sys
import math

def prime_factors(n):
  primeFactors = []
  divisors = []

  duplicateCount = 0
  while n % 2 == 0:
    duplicateCount += 1
    if duplicateCount == 1: 
      divisors.append(2)
    primeFactors.append(2)
    n = n // 2
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    duplicateCount = 0
    while n % i == 0:
      duplicateCount += 1
      if duplicateCount == 1: 
        divisors.append(i)
      primeFactors.append(i)
      n = n // i
  if n > 2:
      primeFactors.append(n)
      divisors.append(n)

  return primeFactors


def divisors(num): #main function
  divisors = [1,num]
  primeFactors = prime_factors(num)
  for x in set(primeFactors): divisors.append(x)

  #Cartesian Product of size 2
  if (len(primeFactors)>=2):
    for i in range(len(primeFactors)): 
      for j in range(i+1,len(primeFactors)):
        product = (primeFactors[i]*primeFactors[j])
        if (product < num): divisors.append(product)
  #Cartesian Product of size 3
  if (len(primeFactors)>=3):
    for i in range(len(primeFactors)): 
      for j in range(i+1,len(primeFactors)):
        for k in range(j+1,len(primeFactors)):
          product = (primeFactors[i]*primeFactors[j]*primeFactors[k])
          if (product < num): divisors.append(product)
  #Cartesian Product of size 4
  if (len(primeFactors)>=4):
    for i in range(len(primeFactors)): 
      for j in range(i+1,len(primeFactors)):
        for k in range(j+1,len(primeFactors)):
          for l in range(k+1,len(primeFactors)):
            product = (primeFactors[i]*primeFactors[j]*primeFactors[k]*primeFactors[l])
            if (product < num): divisors.append(product)
              
  if (len(set(divisors)) >= 500):
      print("Triangular number with over 500 divisors: " + str(num))
      print(set(divisors))
      print("Expected Answer: 76576500") #REMOVE LATER
      sys.exit()

triNum = 1
i = 1
while (True):
  divisors(triNum)
  triNum += i
  i += 1
