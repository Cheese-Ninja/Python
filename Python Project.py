#Python Project

import math
import turtle
import random

egg = turtle.Turtle()
egg.color("#F4A896", "#358597")

def semicircle(size):
    for i in range(10):
        egg.forward(size)
        egg.left(18)

# Main triangle


egg.begin_fill()
<<<<<<< HEAD
egg.pensize(5)
for i in range(3):
    egg.forward(200)
    egg.left(120)
egg.end_fill()

egg.pensize(3)

#C

egg.color("#000000", "#000000")
egg.penup()
egg.forward(240)
egg.right(180)
egg.pendown()
semicircle(5)
egg.forward(5)

#A

egg.penup()
egg.left(120)
egg.forward(250)
egg.pendown()
for i in range(2):
    egg.forward(30)
    egg.left(120)
egg.left(60)
egg.forward(15)
egg.right(60)
egg.forward(15)

#B

egg.penup()
egg.right(180)
egg.forward(15)
egg.left(60)
egg.forward(260)
egg.left(120)
egg.pendown()
for i in range(2):
    semicircle(3)
    egg.right(162)
egg.left(235)
egg.forward(40)

turtle.done()
=======
egg.pensize(10)
for i in range(n):
    egg.forward(50)
    egg.left(180-(180*(n-2)/n))
egg.end_fill()
turtle.done()
>>>>>>> 49e395142926cc6a36205bf93774ff118d970f51
