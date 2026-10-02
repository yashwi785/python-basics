#question:WAP to print numbers from 1 to 10 using while loop
i=1
while i<=10:
    print(i)
    i+=1
# question2: WAP to print 10 to 1 
j=10
while j>=1:
    print(j)
    j-=1
#WAP TO PRINT ALL EVEN NUMBERS BETWEEN 1 TO 50
num = 1
while num<=50:
    if(num%2==0):
        print(num)
    num+=1
#WAP THAT PRINTS THE SUM OF FIRST N NATURAL NUMBER
n=int(input("Enter a number:"))
sum=0
while n>=1:
    sum= sum+n
    n-=1
print("sum:", sum)
print("n:",n)

#WAP to print pattern
i=1
while i<=5:
    print("*"*i)
    i+=1

#WAP t print multiplication table of a number

z= int(input("enter a number"))
a=1
while a<=10:
    print(z*a)
    a+=1 
#WAP to print your name initialising with number
b=1
while b<=5:
    print(b,"Yashwi Rathi")
    b+=1