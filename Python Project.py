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

HypA = False
HypB = False
HypC = False

if AA == 90:
    HypA = True
if AB == 90:
    HypB = True
if AC == 90:
    HypC = True


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
    if twosides() == 1:
        if HypA == True:
            sc = math.sqrt(math.pow(sa, 2) - math.pow(sb, 2))
        elif HypB == True:
            sc = math.sqrt(math.pow(sb, 2) - math.pow(sa, 2))
        elif HypA == True:
            sc = math.sqrt(math.pow(sa, 2) + math.pow(sb, 2))
        print("Side c is " + str(sc))
    if twosides() == 2:
        if HypA == True:
            sb = math.sqrt(math.pow(sa, 2) - math.pow(sc, 2))
        elif HypB == True:
            sb = math.sqrt(math.pow(sa, 2) + math.pow(sc, 2))
        elif HypC == True:
            sb = math.sqrt(math.pow(sc, 2) - math.pow(sa, 2))
        print("Side b is " + str(sb))
    if twosides() == 3:
        if HypA == True:
            sa = math.sqrt(math.pow(sb, 2) + math.pow(sc, 2))
        elif HypB == True:
            sa = math.sqrt(math.pow(sb, 2) - math.pow(sc, 2))
        elif HypC == True:
            sa = math.sqrt(math.pow(sc, 2) - math.pow(sb, 2))
        print("Side a is " + str(sa))