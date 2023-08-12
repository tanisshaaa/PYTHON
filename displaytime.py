#FROM SEC TO HOURS
seconds=int(input("Enter the seconds:"))
hour=seconds//60 #integer division
minute=seconds%60 #REMAINDER division
print("For the following",seconds,"sec. It will be",hour,"hour",minute,"minutes.")

#FROM SEC TO MIN
seconds=int(input("Enter the seconds:"))
minutes=seconds//60 #integer division
remainingSeconds=seconds%60 #REMAINDER division
print("For the following",seconds,"sec. It will be",minutes,"minutes",remainingSeconds,"seconds.")
