
#marks = int(input("Enter your marks for scince: "))
# Function to determine the grade based on marks
def get_grade(marks, subject):  
    #print("The subject is", subject)
    if marks < 35:
        grade =  "you are failed"
    elif marks >= 35 and marks < 50: 
        grade =  "you are pass but grade is C"
    elif marks >= 50 and marks < 60:
        grade =  "you are pass but grade is B"
    elif marks >= 60 and marks < 70:
        grade =  "you are pass but grade is A"
    else:
        grade =  "you are pass and premoted to next class"
    
    return grade

grade = get_grade(57, "sinhala")

print(grade)  # Output: you are pass but grade is B