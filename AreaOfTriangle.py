x1,x2,y1,y2,z1,z2=eval(input("Enter the points:""\n"))
side1=x1+y1
side2=x2+y2
side3=z1+z2
s=float((side1+side2+side3)/2)

area=((s(s-side1)*(s-side2)*(s-side3))**0.5)