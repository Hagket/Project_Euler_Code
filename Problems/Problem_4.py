#Problem 4#
palindromes=[]
def palindromechecker(num):
  origin=num
  reverse=0
  while (num>0):
    remainder=num%10
    reverse=(reverse*10)+remainder
    num=num//10
  if (origin==reverse):
    palindromes.append(origin)

for i in range(100,999):
  mult=100
  while mult<=999:
    num=i*mult
    mult+=1
    palindromechecker(num)
palindromes.sort()
print(palindromes)
print("The largest palindrome made from the product of two 3-digit numbers: " + str(palindromes[len(palindromes)-1]))