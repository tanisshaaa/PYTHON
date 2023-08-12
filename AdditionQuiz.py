import random
a=random.randint(0,9)
b=random.randint(0,9)
print("What is the sum of",a,"and",b,"?")
answer=eval(input("Enter your answer:"))
if((a+b)==answer):
    print("Correct!!!")

else:
    print("Wrong!!!")    