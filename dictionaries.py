#dictionaries
#unordered,mutable
#key:value pair 
#indexing doesn't work

student = {
    "name": "John",
    "age": 25,
    "courses": ["Math", "Science", "History"] ,
    "name": "John Doe"  # duplicate key, the last value will overwrite the previous one
}

print(student["name"])  # accessing value by key
print(student["age"])   # accessing value by key
print(student["courses"])  # accessing value by key

print(type(student))  # type is dict
print(student["name"]) # this will print the value of the key "name" which is "John Doe"
print(student)
student['age'] = 26  # updating value of existing key
print(student)
student["favcourse"]="maths"
print(student)
student.pop("age")  #reomoves the key
print(student)
print(student.keys())
print(student.items())


