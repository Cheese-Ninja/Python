#Python Project

import math
import turtle

egg = turtle.Turtle()
egg.color("#F4A896", "#358597")

n = int(input("Integer: \n"))
egg.begin_fill()
egg.pensize(5)
for i in range(n):
    egg.forward(50)
    egg.left(180-(180*(n-2)/n))
egg.end_fill()
turtle.done()

print("Hello World")
print("Goodbye World")

print("lmao\n")