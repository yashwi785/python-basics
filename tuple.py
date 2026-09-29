#tuple
#imutable

mytuple = (1, 2, 3, 4, 5)
print(mytuple)

#mytuple[2]= 10 # trying to change an element of the tuple will raise an error  

print(mytuple[0]) # accessing specific element  

#empty tuple
empty_tuple = ()
print(type(empty_tuple)) # type is tuple
single_tuple = (1) # single element tuple
print(type(single_tuple)) # type is int

# , makes single_tuple a tuple without , it is an integer.

single_tuple = (1,) # single element tuple with comma
print(type(single_tuple)) # type is tuple

print( "length:", len(mytuple)) # length of tuple  
print("max", max(mytuple)) # max value in tuple    
print("min", min(mytuple)) # min value in tuple    
 
print("last element:",mytuple[-1]) # negative indexing      
print("sliced elements:",mytuple[1:4]) # slicing   
print("count of specific element",mytuple.count(2)) # count of specific element in tuple    
print("element at given index:",mytuple.index(3)) # index of specific element in tuple    
