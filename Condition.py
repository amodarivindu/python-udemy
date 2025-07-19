
x = int(input("Enter your marks for scince: "))

if x < 35:
    print("you are failed")
elif x >= 35 and x < 50: 
    print("you are pass but grade is C")
elif x >= 50 and x < 60:
    print("you are pass but grade is B") 
elif x >= 60 and x < 70:
    print("you are pass but grade is A")
else:
    print("you are pass and premoted to next class")


height = int(input("Enter your height in cm: "))

job = "security" if height >= 170 else "not security" # ternary operator
print("You are eligible for the job:", job)