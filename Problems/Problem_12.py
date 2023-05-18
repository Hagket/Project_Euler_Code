# Problem 12#
import sys


def divisor(num):
    divisors = []

    for i in range(1, num + 1):
        if (num % i == 0):
            divisors.append(i)
    if (len(divisors) >= 500):
        print("Triangular number with over 500 divisors: " + str(num))
        print(divisors)
        sys.exit()


num = 0
i = 1
while (True):
    divisor(num + i)
    num += i
    i += 1

print("Program is finished.")