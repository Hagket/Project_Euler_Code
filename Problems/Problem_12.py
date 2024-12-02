# Problem 12#
#This solution is too slow. The divisors function needs to be optimized to find divisors quicker#
import sys

def divisors(num):
    divisors = []
    print(num)
    for i in range(1, num + 1):
        if (num % i == 0): divisors.append(i)
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

print("Program is finished.")
