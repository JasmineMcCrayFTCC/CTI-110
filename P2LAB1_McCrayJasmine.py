#Jasmine McCray
#P2LAB1
#9/28/2026
#This program will calculate the diameter, circumference, and area of a circle. 

#Import math module to use math.pi for constant
import math

#Get radius
radius = float(input("What is the radius of the circle? "))
print()

#Calculate diameter
diameter = 2 * radius

#Display diameter with 1 dec point
print(f"The diameter of the circle is {diameter:.1f}\n")

#Calculate circumference
circumference = 2 * math.pi * radius

#Display circumference with 2 decimal places
print(f"The circumference of the circle is {circumference:.2f}\n")

#Calculate area
area = math.pi * radius ** 2

#Display area with 3 decimal places
print(f"The area of the circle is {area:.3f}")