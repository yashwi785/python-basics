#questions
#1 WAP using for and range() to print all even numbers between 1 to 20

for i in range(2,21,2):
    print(i)

#2 square of 1 to 10 numbers:
for k in range(1,11):
    print(k*k)

#3. multiplication table of entered number
num=int(input("Enter a number:"))   
for a in range(1,11):
    print(num*a)

#4. WAP to print numbers 1 to 50 but print "Yashwi Rathi" for multiples of  5
for b in range(1,51):
    if(b%5==0):
        print("Yashwi Rathi")
    else:
        print(b)

#5. WAP to print the numbers 1 to 10 and skip 7 using continue statement
for c in range(1,11):
    if(c==7):
        continue
    print(c)