
#if statement
age=int(input("Enter the age: "))
if(age>18):
 print("SUCCEDED!!!")

 #if else statement
age=int(input("Enter the age: "))
if(age>18):
 print("SUCCEDED!!!")
else:
 print("FAILED!!!")

 #nested if statement
age=int(input("Enter the age: "))
if(age>18):
 print("SUCCEDED!!!")
if(age<10):
 print("FAILED!!!")

 #if elif else statememnt
first=int(input("Enter the First Number: "))
second=int(input("Enter the Second Number: "))
third=int(input("Enter the  Third Number: "))
if(first>second):
    if(first>third):
        print(first)
elif(second>third):
    print(second)
else:
    print(third)            
