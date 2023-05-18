#Problem 2#
fiblist=[]
evenfiblist=[]
fib=0
num=1
case=1
def fibonacci(n):
  if n==1:
    return 1
  if n==2:
    return 1
  else:
    return (fibonacci(n-2))+(fibonacci(n-1))
while (case==1):
  fib=fibonacci(num)
  if (fib<4000000):
    fiblist.append(fib)
    num+=1
  else:
    case=2
print("All Fibonacci numbers: " + str(fiblist))

for i in fiblist:
  if (i%2==0):
    evenfiblist.append(i)
print("All even Fibonacci numbers under 4 million: " + str(evenfiblist))

total=0
for i in range(0,len(evenfiblist)):
  total+=evenfiblist[i]
print("Sum of even Fibonacci numbers under 4 million: " +  str(total))
