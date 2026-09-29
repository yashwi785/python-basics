#string
name = "Alice"
last_name = "Smith"
print(name)  # Alice
print(type(name))  # <class 'str'>

#concatenation
print(name + " " + last_name)

#length of string
print(len(name))  # 5
print(len(last_name))  # 5

#indexing starts from 0
print(name[0])  # A
print(last_name[0])  # S

#QUESTION:WAP that takes user name as input and prints: first character, last character, total length of string
name = input("enter your name:")
print(name[0])  # first character
print(name[-1])  # last character
print(len(name))  #  total length of string 
print("first character:", name[0])
print("last character:", name[-1])
print("total length:", len(name))   
print(name.upper())  # convert to uppercase
print(name.lower())  # convert to lowercase
print(name.capitalize())  # capitalize first letter     
print(name.title())  # title case   
print(name.strip())  # remove leading and trailing whitespace       
print(name.replace("a", "@"))  # replace 'a' with '@' in the string 
print(name.split())  # split the string into a list of words    
print(name.count("a"))  # count occurrences of 'a' in the string    

#formatted string
age = 25  
name=input("Enter your name: ")  
print(f"Hello, {name}! You are {age} years old.")

#escape characters
print("Hello\nWorld")  # prints Hello and World on separate lines
print("Hello\tWorld")  # prints Hello and World separated by a tab
print("He said, \"Hello!\"")  # prints He said, "Hello!"

#emojis converter
msg = input("Enter your message: ")
msg = msg.replace(":)", "😊")
msg = msg.replace(":(", "😢")
print(msg)