'''The formula is given as follows:
twc = 35.74 + 0.6215*ta - 35.75*(v**0.16) + 0.4275*ta*(v**0.16)

where is the outside temperature measured in degrees Fahrenheit and v is the
speed measured in miles per hour. is the wind-chill temperature. The formula
cannot be used for wind speeds below 2 mph or for temperatures below or
above 41°F. 

Write a program that prompts the user to enter a temperature between and
41°F and a wind speed greater than or equal to 2 and displays the wind-chill temperature'''

ta=eval(input("Enter the temperature in Fahrenheit between -58 and 41:"))
v=eval(input("Enter the wind speed in miles per hour:"))
twc = 35.74 + 0.6215*ta - 35.75*(v**0.16) + 0.4275*ta*(v**0.16)
print("The wind chill index is",twc)