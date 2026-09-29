#first program
print("hello world:)")

#print hello world 10 times using * symbol:
print(("Hello, World!" + "\n") * 10)

#input from user
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to the program.")       

#variable assignment
age = 20
Name = "Yashwi"
print("My name is " + Name + " and I am " + str(age) + " years old.")

#type conversion
num1 = input("Enter a number: ")
num1 = float(num1)   #this will convert integer to float
print(num1)

#round function
num2 = 3.14159
rounded_num = round(num2, 2)  #rounding to 2 decimal places
print("Rounded number:", rounded_num)

#QUESTION: TAKE DIAMETER AS INPUT AND CALCULATE AREA OF CIRCLE
diameter = float(input("Enter the diameter of the circle: "))
radius = diameter / 2
area = 3.14159 * radius ** 2
print("The area of the circle is:", area)
