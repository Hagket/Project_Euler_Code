#Problem 19#
#This code has not been finished yet b/c problem 19 has not been completed on ProjectEuler account#
monthDays={"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}
monthDaysList=["January","February","March","April","May","June","July","August","September","October","November","December"]
daysOfWeek=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
count=0
daysInYear=365
year=1901
month=0
day=daysOfWeek[1] #January 1st 1901 is a Tuesday
monthDay=monthDays["January"]

for i in range(1,367):
  day=daysOfWeek[i%7]
  if (year%4==0 or year%400==0): #Leap Year
    monthDays["February"]=29
    daysInYear=366
    if (i%(daysInYear+1)==0):
      year+=1
      month+=1
      monthDay=monthDays["January"]
    else:
      if (i%monthDay==1 and day=="Sunday"):
        count+=1
      elif (i%monthDay==0): #End of month
        month+=1
        monthDay+=(monthDays[monthDaysList[month%12]])

  else: #Common Year
    monthDays["February"]=28
    daysInYear=365
    if (i%(daysInYear+1)==0):
      year+=1
      month+=1
      monthDay=monthDays["January"]
    else:
      if (i%(monthDay+1)==1 and day=="Sunday"):
        count+=1
      elif (i%(monthDay+1)==0): #First day of month
        month+=1
        monthDay+=(monthDays[monthDaysList[month%12]])

print(monthDay)
print(monthDaysList[month%12])
print(year)

print("The number of Sundays that fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000) is: " + str(count))
