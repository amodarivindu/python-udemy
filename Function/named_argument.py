

def get_grade(x, subject="Unknown"):  
    print("The subject is", subject)
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

get_grade( x=54, subject="sinhala") #if we use name argument all after arguments  should be name arguments, 
#we can use like this   get_grade(54, subject="sinhala") but we can use like this get_grade(54, subject="sinhala")
get_grade( 75)