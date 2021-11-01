import math

shape=input("What shape do you have ")
if shape == "square" :
  length=int(input("Enter the length of the square "))
  method=input("Do you want to work out the perimeter or the area ")
  if method == "perimeter":
    perimeter=int(length) * 4
    print(perimeter)
  elif method == "area":
     area=length * length
     print(area)
elif shape == "circle":
  radius=int(input("What is the radius of the circle "))
  method=input("Do you want to work out the circumference or the area ")
  if method == "circumference":
    circumference= 2 * math.py * radius
    print(circumference)
  elif method == "area":
    area=(math.py * radius)**2
    print(area)
elif shape == "Triangle":
  side1=int(input("What is the length of side a "))
  side2=int(input("What is the length of side b "))
  height=int(input("What is the height "))
  base=int(input("What is the base "))
  method=input("Would you like to work out the perimeter or area ")
  if method == "perimeter":
    perimeter=side1 +side2 + base
    print("perimeter")
  elif method == "area":
    area=height * base / 2
    print(area)
elif shape == "Rectangle":
  length=int(input("Enter the length "))
  height=int(input("Enter the height "))
  method=input("Would you like to work out the perimeter or area ")
  if method == "perimeter":
    perimeter=length+height * 2 
    print(perimeter)
  elif method == "area" :
    area=length * height
    print(area)
elif shape == "Parallelogram":
  side=int(input("Enter the length of one side "))
  base=int(input("Enter the base "))
  method=input("Would you like to work out the perimeter or area ")
  if method == "perimeter":
    perimeter= 5 * side
    print(perimeter)
  elif method == "area":
    area=side + base * 2
    print(area)
elif shape == "Rhombus":
  side=int(input("Enter the length of one side "))
  diagnol1=int(input("Enter the length of one of the diagnols "))
  diagnol2=int(input("Enter the length of the other diagnol "))
  method=input("Would you like to work out the perimeter or area ")
  if  method == "perimeter":
    perimeter= 4 * side
    print(perimeter)
  elif method == "area":
    area=diagnol1 * diagnol2 /2
    print(area)

