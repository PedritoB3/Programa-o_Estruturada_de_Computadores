from turtle import *

speed(11)
shape("turtle")
pensize(6)
color("Green")

for count in range(36):
    forward(100)
    right(100)
    right(10)
    forward(60)
penup()

backward(200)

pendown()
color("Purple")
for count in range(18):
    forward(100)
    right(200)
    forward(150)
    forward(10)
    left(50)
penup()

left(100)
forward(200)

pendown()
color("Red")
for count in range(36):
    forward(100)
    left(50)
    backward(25)
    forward(10)

done()
