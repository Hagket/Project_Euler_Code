#Problem 12#
#Solution 2 (Easy Solution using sympy library)#
from sympy import divisors 

triNum = 0
i = 1
while (True):
    divisors_list = list(divisors(triNum))
    if (len(divisors_list) >= 500):
      print("Triangular number with over 500 divisors: " + str(triNum))
      print(divisors)
      break
    triNum += i
    i += 1
