#Python Project

import math
import turtle

egg = turtle.Turtle()

n = int(input("Integer: \n"))
for i in range(n):
    egg.forward(50)
    egg.left(180-(180*(n-2)/n))
turtle.done()

print("Hello World")
print("Goodbye World")

print("lmao\n")