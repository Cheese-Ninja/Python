#Python Project

import math
import turtle
import random

# Asking User for inputs

AA = float(input("What is Angle A? If unknown, input 0\n"))
AB = float(input("What is Angle B? If unknown, input 0\n"))
AC = float(input("What is Angle C? If unknown, input 0\n"))
sa = float(input("What is Side a? If unknown, input 0\n"))
sb = float(input("What is Side b? If unknown, input 0\n"))
sc = float(input("What is Side c? If unknown, input 0\n"))

HypLen = [False, False, False]
# 0 = A, 1 = B, 2 = C 

if AA == 90:
    HypLen[0] = True
if AB == 90:
    HypLen[1] = True
if AC == 90:
    HypLen[2] = True


def twosides():
    if sa != 0 and sb != 0 and sc == 0:
        return 1
    if sa != 0 and sb == 0 and sc != 0:
        return 2
    if sa == 0 and sb != 0 and sc != 0:
        return 3
    else:
        return 0

# Pythagoras

if twosides() > 0:
    # Figuring out which rearrangement of the formula to use
    if twosides() == 1:
        if HypLen[0] == True:
            sc = math.sqrt(math.pow(sa, 2) - math.pow(sb, 2))
        elif HypLen[1] == True:
            sc = math.sqrt(math.pow(sb, 2) - math.pow(sa, 2))
        elif HypLen[2] == True:
            sc = math.sqrt(math.pow(sa, 2) + math.pow(sb, 2))
    if twosides() == 2:
        if HypLen[0] == True:
            sb = math.sqrt(math.pow(sa, 2) - math.pow(sc, 2))
        elif HypLen[1] == True:
            sb = math.sqrt(math.pow(sa, 2) + math.pow(sc, 2))
        elif HypLen[2] == True:
            sb = math.sqrt(math.pow(sc, 2) - math.pow(sa, 2))
    if twosides() == 3:
        if HypLen[0] == True:
            sa = math.sqrt(math.pow(sb, 2) + math.pow(sc, 2))
        elif HypLen[1] == True:
            sa = math.sqrt(math.pow(sb, 2) - math.pow(sc, 2))
        elif HypLen[2] == True:
            sa = math.sqrt(math.pow(sc, 2) - math.pow(sb, 2))
    print("Side A is " + str(sa) + ", Side B is " + str(sb) + ", Side C is " + str(sc) + ".")
    # SOHCAHTOA Trig
    if HypLen[0] == True:
        AB = math.degrees(math.acos(sc / sa))
        AC = 90 - AB
    elif HypLen[1] == True:
        AC = math.degrees(math.acos(sa / sb))
        AA = 90 - AC
    elif HypLen[2] == True:
        AA = math.degrees(math.acos(sb / sc))
        AB = 90 - AA
    print("Angle A is " + str(AA) + ", Angle B is " + str(AB) + ", Angle C is " + str(AC) + ".")