
print("This program converts feet and inches to centimeters.")
print("Enter number of feet:", end=' ')
feet = int(input())
confeet = feet* 30.48
print("Enter number of inches:",end=' ')
inch = int(input())
coninch = inch * 2.54


print(feet, "ft", inch, "in =" , confeet + coninch , "cm")