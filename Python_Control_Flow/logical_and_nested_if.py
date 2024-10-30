is_student = True
is_employed = True

if (is_student and is_employed):
    print("You are a working student")
elif (is_student and not is_employed):
    print("You are a student")
elif (not is_student and is_employed):
    print("You are employed but not a student")


Age = int(input("Enter your age: "))

if Age >= 18:
       
      license = input("Please do you have a driving license? (yes / no")

if license.lower() == "yes":
    print("You are allowed to drive")
else:
    print("You need a driver's license to drive")  
# else:        
#     print("You are not old enough to drive")     
