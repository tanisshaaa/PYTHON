'''Write a program that calculates the energy needed to
heat water from an initial temperature to a final temperature.'''

M=eval(input("Enter the amount of water in kilograms:")) 
initialTemperature=eval(input("Enter the initial temperature:")) 
finalTemperature=eval(input("Enter the final temperature:"))
Q=M*(finalTemperature - initialTemperature) * 4184 
print("The energy needed is",Q)