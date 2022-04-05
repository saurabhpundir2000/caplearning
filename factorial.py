n=int(input("enter a number"))
fact=1
if n<0:
    print("wrong input")
elif n==0:
    print("1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial is= ",fact)
