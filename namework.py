name = ("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print("Hello " + name + "you are eligible to continue the application")
else:
    print("Hello" + name + "you are young and cannot apply")