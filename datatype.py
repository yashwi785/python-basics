#data type
x=10
y=3.14
z="Hello"
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>   
print(type(z))  # <class 'str'>

#QUESTION: WAP THAT TAKES YOUR AGE AS INPUT AND PRINTS: THE VALUE ENTERED AND THE DATA TYPE
age = int(input("enter your age: "))
print("the value entered is:", age)
print("the data type age holds: ", type(age))

#SUM AND AVG OF TWO NUMBERS
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum = num1 + num2   
print("sum of two number:", sum)
avg = sum / 2
print("average of two number:", avg)

#QUESTION: WAP THAT TAKES TWO NUMBERS AND PRINTS: SUMK, DIFFERENCE,PRODUCT,WHETHER THE FIRST NUMBER IS GREATER THAN THE SECOND NUMBER OR NOT
a= float(input("Enter first number: "))
b= float(input("Enter second number: "))    
print("sum of two number:", a+b)
print("difference of two number:", a-b)
print("product of two number:", a*b)
print("is the first number greater than the second?", a > b)    


#ASSIGNMENT1: take  input in celsius and print its equivalent in farenhite and kelvin
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print("Temperature in Fahrenheit:", fahrenheit)
print("Temperature in Kelvin:", kelvin)

#ASSIGNMENT2: WAP that takes total bill amolunt and number of friends as input and calculate how much each will pay
bill= float(input("Enter total bill amount: "))
friends= int(input("Enter number of friends: "))
each_will_pay = bill / friends
print("Each friend will pay:", each_will_pay)