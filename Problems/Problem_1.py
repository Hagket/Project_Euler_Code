#Problem 1#
numbers=[]
number=3
while (number<1000):
  if (number%3==0):
    numbers.append(number)
    number+=1
  elif (number%5==0):
    numbers.append(number)
    number+=1
  else:
    number+=1
total=0
for i in range(0,len(numbers)):
  total+= numbers[i]
print("The sum of all multiples of 3 or 5 below 1000: " + str(total))
