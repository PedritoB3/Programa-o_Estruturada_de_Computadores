from turtle import *

sides = 150
ang = 360/sides

speed(11)
shape("turtle")
pensize(6)
color("Red")

for count in range(36):
    forward(200)
    right(sides)
penup()

backward(100)

pendown()
color("Blue")
for count in range(18):
    forward(150)
    right(sides)
penup()

left(75)
forward(200)

pendown()
color("Green")
for count in range(32):
    forward(150)
    right(sides)
    forward(50)
done()
