#Problem 6#
squares=[]
ofthesquare=[]
def squarer(b,x):
  while b<=100:
    if (x==0):
      return 1
    else:
      return b*squarer(b,x-1)
      b+=1

for i in range(1,101):
  num=squarer(i,2)
  squares.append(num)

total=0
for i in range(0,len(squares)):
  total+=squares[i]
print("The sum of the squares of the first 100 natural numbers: "+ str(total))

for i in range(1,101):
  ofthesquare.append(i)

total=0
for i in range(0,len(ofthesquare)):
  total+=ofthesquare[i]
print("The square of the sum of the first 100 natural numbers: " + str(25502500))

difference=25502500-338350
print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum: " + str(difference))