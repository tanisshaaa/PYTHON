pound=0.45359237
inch=0.0254
weight,height=eval(input("Enter weight and height: "))
kilogram=pound*weight
meters=inch*height
BMI=kilogram/(meters**2)

print("BMI is",BMI)