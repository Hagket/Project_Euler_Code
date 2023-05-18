#Problem 17#
onesPlace=["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] #36 total
teens=["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"] #70 total
tensPlace=["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
total=0

for i in range(1,1001):
  singleDigits=[int(i) for i in str(i)]
  numString=""
  if (len(singleDigits)==4):
    numString+="onethousand"

  if (len(singleDigits)==3):
    numString+=onesPlace[singleDigits[0]]
    numString+="hundred"
    if (singleDigits[1]!=0 or singleDigits[2]!=0):
      numString+="and"

    if (singleDigits[1]==1):
      numString+=teens[singleDigits[2]]
    else:
      numString+=tensPlace[singleDigits[1]]
      numString+=onesPlace[singleDigits[2]]
  if (len(singleDigits)==2):
    if (singleDigits[0]==1):
      numString+=teens[singleDigits[1]]
    else:
      numString+=tensPlace[singleDigits[0]]
      numString+=onesPlace[singleDigits[1]]

  if (len(singleDigits)==1):
    numString+=onesPlace[singleDigits[0]]

  total+=len(numString)



print("The amount of letters used by the numbers 1-1000 writen out in words is: " + str(total))