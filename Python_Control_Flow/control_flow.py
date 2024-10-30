Name = str (input("What is your name?: "))
print(Name)

Age = int (input("Enter your age: "))
print(Age)

if (Age < 18):
        print("You are a minor.")
elif (18 >= Age <= 64):
        print("You are an adult.")
else:
        print("You are a senior.")    