# Problem 12#
#This solution is too slow. The divisors function needs to be optimized to find divisors quicker#
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
        

def divisors(num): #main function. prime_factors has not been connected yet.
  divisors = []
  print(num)
  for i in range(1, num + 1):
      if (num % i == 0): 
        divisors.append(i)
  if (len(divisors) >= 500):
      print("Triangular number with over 500 divisors: " + str(num))
      print(divisors)
      sys.exit()


triNum = 0
i = 1
while (True):
    divisors(triNum)
    triNum += i
    i += 1
