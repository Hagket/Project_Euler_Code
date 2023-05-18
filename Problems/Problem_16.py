#Problem 16#
num=2**1000
singleDigits= [int(num) for num in str(num)]
sumOfDigits=0

for i in range(0,len(singleDigits)):
  sumOfDigits+=singleDigits[i]


print("The sum of the digits of the number 2^1000 is: " + str(sumOfDigits))