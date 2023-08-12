number=eval(input("Enter a number between 0 and 1000: "))
lastDigit=number%10
lastDigitQuotient=number//10
middleDigit=lastDigitQuotient%10
firstDigit=lastDigitQuotient//10
print("The digits are:","\n",firstDigit,"\n",middleDigit,"\n",lastDigit)
