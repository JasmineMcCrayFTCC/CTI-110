# Jasmine McCray
# October 27, 2026
# P4LAB1_McCrayJasmine.py
# This program will use loops and turtles to draw

#Import from library
from ast import While
import turtle

# Create a turtle window and object
window = turtle.Screen()
pen = turtle.Turtle()

# Set turtle options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("turtle")

# Bg color
window.bgcolor("pink")

#Draw the square
for side in range(4):
    pen.forward(100)
    pen.left(90)

#Put triangle on top of square
pen.penup()
pen.goto(2, 110)
pen.pendown()
turtle.begin_fill()
for i in range(3):
    pen.forward(100)
    pen.left(120)
turtle.end_fill()

#Draw the triangle
sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1



# Wait on user to close window
window.mainloop()
