ht=int(input("enter height in cm = "))
wt=int(input("enter weight in kg = "))

BMI=int (wt/(ht/100)**2)

print("BMI = ",BMI)

if BMI <= 19:  
    print("underweight")  
elif BMI <= 25:  
    print("healthy")  
elif BMI <= 30:  
    print("overweight")  
else:  
    print("obese")  



