#Problem 14#
max=0
longestNum=0

for i in range (13,1000000):
  num=i
  collatz=[i]
  while (num!=1):
    if (num%2==0):
      num/=2
      collatz.append(num)
    else:
      num=3*num+1
      collatz.append(num)
  if (len(collatz)>max):
    max=len(collatz)
    longestNum=i

print("The starting number, under 1 million, that produces the longest Collatz sequence is: " + str(longestNum))