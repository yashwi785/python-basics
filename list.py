#list
#list is a collection which is ordered and changeable. Allows duplicate members.
#list ar mutable, meaning you can change, add, and remove items in a list after it has been created.

foods =['pizza', 'waffle', 'hotdog', 'pasta', 'pudding']
print(foods)
print(len(foods))
print(foods[0])
print(foods[-1]) # negative indexing
print(foods[1:4]) # slicing
foods[1]="taco" # accessing specific element
print(foods[1])
print("Max value:", max(foods)) # max value
print("Min value:", min(foods)) # min value

foods.append("ice cream") # adding element at the end
print(foods)
foods.insert(2, "burger") # adding element at specific index
print(foods)
foods.remove("hotdog") # removing element
print(foods)
foods.pop() # removing last element
print(foods)
foods.sort() # sorting the list
print(foods)
foods.reverse() # reversing the list
print(foods)
foods.clear() # clearing the list
print(foods)

#question: take 3 favourite foods from user and store them in a list then print list, length of list.

food1= input("Enter your first favourite food: ")
food2= input("Enter your second favourite food: ")
food3= input("Enter your third favourite food: ")

favourite_foods = [food1, food2, food3]
print("Your favourite foods are:", favourite_foods)
print("Length of the list:", len(favourite_foods))  
