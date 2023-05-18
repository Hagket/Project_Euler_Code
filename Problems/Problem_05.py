#Problem 5#
numbers= []
def divider(num):
  if num%1==0:
    if num%2==0:
      if num%3==0:
        if num%4==0:
          if num%5==0:
            if num%6==0:
              if num%7==0:
                if num%8==0:
                  if num%9==0:
                    if num%10==0:
                      if num%11==0:
                        if num%12==0:
                          if num%13==0:
                            if num%14==0:
                              if num%15==0:
                                if num%16==0:
                                  if num%17==0:
                                    if num%18==0:
                                      if num%19==0:
                                        if num%20==0:
                                          numbers.append(num)


for i in range(1,2):
  mult=1
  while mult<=1000000000:
    num=i*mult
    mult+=1
    divider(num)
print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20: " + str(numbers[0]))
