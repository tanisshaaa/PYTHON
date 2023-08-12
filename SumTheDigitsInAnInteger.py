#Sum the digits in an integer
number=eval(input("Enter a number between 0 and 1000: "))
lastDigit=number%10
lastDigitQuotient=number//10
middleDigit=lastDigitQuotient%10
firstDigit=lastDigitQuotient//10
print("The sum of the digits is:",lastDigit+middleDigit+firstDigit)