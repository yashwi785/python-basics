#conditional statements
#if statement
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")

#if else statement
result =int(input("Enter your marks: "))
if result>=40:
    print("You have passed the exam.")
else:
    print("You have failed the exam.")  

#if elif else statement
mark=int(input("Enter your marks: "))  
if(mark>=90):
    print("You have scored A grade.")   
elif(50<mark<90):
    print("you have scored B grade ")
else:
    print("you hae failed!")

#nested if statement
agegrp=int(input("Enter your age: "))
if agegrp>=18:
    print("You are eligible to vote.")
    if agegrp>=60:
        print("You are a senior citizen.")
    else:
        print("You are an adult.")

#  QUESTION: TAKE NUMBER AS INPUT AND PRINT: POSTIVE, NEGATIVE, EQUALS TO ZERO

a =int(input("Enter a number: "))
if a>0:
    print("The number is positive.")
elif a<0:
    print("The number is negative.")
else:
    print("The number is zero.")