#(Find the number of years and days)
minutes=eval(input("Enter the number of minutes: "))
hour=minutes//60
remainingHours=minutes%60
day=hour//24
remainingDay=remainingHours%24
years=day//365
remainingYears=remainingDay%365
print(years,remainingYears)
                  