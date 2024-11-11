# Age Validator
age = int(input("Enter your age: "))
if age < 0:
    print("Age cannot be negative!")
elif age > 120:
    print("That age is unlikely!")
else:
    print("Your age is:", age)



try:
    age = int(input("Enter your age: "))
    
    if age < 0:
        print("Age cannot be negative!")
    elif age > 120:
        print("That age is unlikely!")
    else:
        print("Your age is:", age)
        
except ValueError:
    print("Invalid input! Please enter a numeric value.")
