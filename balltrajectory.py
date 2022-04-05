import math

v=float(input("enter initial velocity = "))
theta=int(input("enter angle with the horizontal = "))
y=float(input("Enter height = "))
x=float(input("enter value of distance = "))
g=9.8

theta=round(theta*math.pi/180,2)

fx=round(x*math.tan(theta)-(1/(2*pow(v,2)))*((g*pow(x,2))/(math.cos(theta)**2))+y,2)

print("angle = {} degrees \n math.tan({})= {} \n velocity = {} km/hr \n g= {} m/s**2 \n height = {} m \n distance = {} m \n trajectory = {} m".format(theta,theta,math.tan(theta),v,g,y,x,fx))

#print("trajectory=%.1f m" %fx)