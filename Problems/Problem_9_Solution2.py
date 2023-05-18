#Alternate Solution for 9 by ryt_1484#
def pythagorean(nmax):
    for a in range(1,nmax):
        for b in range(a+1,1000-a):
            c=nmax-a-b
            p=a**2+b**2
            if p==c**2:
                print("a="+str(a)+", b="+str(b)+", c="+str(c))
                return a*b*c
            elif p>c**2:
                break

print(pythagorean(1000))