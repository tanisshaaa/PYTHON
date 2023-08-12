finalAccountValue=eval(input("Enter final account value:")) 
AnnualInterestRate=eval(input("Enter annual interest rate in percent:")) 
numberOfYears=eval(input("Enter number of years:")) 
numberOfMonths=12*numberOfYears
initialDepositAmount = (finalAccountValue)/(1 + (AnnualInterestRate**numberOfMonths))
print("Initial deposit value is",initialDepositAmount)