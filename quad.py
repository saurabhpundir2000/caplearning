import cmath
a=int(input("enter coeff of x^2= "))
b=int(input("enter coeff of x= "))
c=int(input("enter const= "))

d=(b**2)-(4*a*c)

s1=(-b+ cmath.sqrt(d))/(2*a)
s2=(-b- cmath.sqrt(d))/(2*a)
print("the solutions are {} and {}".format(s1,s2))
