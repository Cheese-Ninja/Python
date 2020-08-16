#Python Project

import math
import turtle
import random

# Asking User for inputs

AA = float(input("What is Angle A?\ If unknown, input 0\n"))
AB = float(input("What is Angle B?\ If unknown, input 0\n"))
AC = float(input("What is Angle C?\ If unknown, input 0\n"))
sa = float(input("What is Side a?\ If unknown, input 0\n"))
sb = float(input("What is Side b?\ If unknown, input 0\n"))
sc = float(input("What is Side c?\ If unknown, input 0\n"))

def twosides():
    if sa != 0 and sb != 0 and sc == 0:
        return 1
    if sa != 0 and sb == 0 and sc != 0:
        return 2
    if sa == 0 and sb != 0 and sc != 0:
        return 3
    else:
        return 0

if twosides() > 0:
    if twosides() == 1:
        sc = math.sqrt(math.pow(sa, 2) + math.pow(sb, 2))
        print(sc)
    if twosides() == 2:
        sb = math.sqrt(math.pow(sa, 2) + math.pow(sc, 2))
        print(sc)
    if twosides() == 3:
        sa = math.sqrt(math.pow(sb, 2) + math.pow(sc, 2))
        print(sc)