import math

p=float(input("enter Interest rate per Annum = "))
a=float(input("enter Initial amount = "))
n=int(input("enter years = "))
10

final_amount=a*(math.pow((1+p/100),n))

print("the amount {} at interest rate {} after {} years is now {}".format(a,p,n,final_amount))