import random

user=input("Enter a choice :")
ch=["rock","paper","scissor"]
comp=random.choice(ch)

print("your choice= ",user ,"\ncomputer choice = ",comp)

if user==comp:
    print ("Draw")
elif user=="paper" and comp=="rock" or user=="rock" and comp=="scissor" or user=="scissor" and comp=="paper"  :
    print("you win")
else:
    print("you Loose")

