#Python Project

import math
import turtle
import random

# Asking User for inputs
AA = float(input("What is Angle A? If unknown, input 0\n"))
while AA < 0 or AA >= 180:
    AA = float(input("What is Angle A? If unknown, input 0\n"))
AB = float(input("What is Angle B? If unknown, input 0\n"))
while AB < 0 or AB >= 180:
    AB = float(input("What is Angle B? If unknown, input 0\n"))
AC = float(input("What is Angle C? If unknown, input 0\n"))
while AC < 0 or AC >= 180:
    AC = float(input("What is Angle C? If unknown, input 0\n"))
sa = float(input("What is Side a? If unknown, input 0\n"))
while sa < 0:
    sa = float(input("What is Side a(in cm)? If unknown, input 0\n"))
sb = float(input("What is Side b (in cm)? If unknown, input 0\n"))
while sb < 0:
    sb = float(input("What is Side b (in cm)? If unknown, input 0\n"))
sc = float(input("What is Side c(in cm)? If unknown, input 0\n"))
while sc < 0:
    sc = float(input("What is Side c(in cm)? If unknown, input 0\n"))

# Checking validity

if sides() == 3 and (sa + sb <= sc or sb + sc <= sa or sc + sa <= sb):
    print("Invalid side lengths: Error too big")

if angles() == 3:
    if AA + AB + AC != 180:
        print("Invalid angles: Error sum 180")

if 20 < angles() < 24 or 10 < angles() < 14:
    if AA + AB + AC > 180:
        print("Invalid angles: Error sum 180")

# Functions

def sides():
    if sa != 0 and sb != 0 and sc != 0:
        return 3
    if sa != 0 and sb != 0 and sc == 0:
        return 21
    if sa != 0 and sb == 0 and sc != 0:
        return 22
    if sa == 0 and sb != 0 and sc != 0:
        return 23
    if sa != 0 and sb == 0 and sc == 0:
        return 11
    if sa == 0 and sb != 0 and sc == 0:
        return 12
    if sa == 0 and sb == 0 and sc != 0:
        return 13
    if sa == 0 and sb == 0 and sc == 0:
        return 0
    else:
        return -1

def angles():
    if AA != 0 and AB != 0 and AC != 0:
        return 3
    if AA != 0 and AB != 0 and AC == 0:
        return 21
    if AA != 0 and AB == 0 and AC != 0:
        return 22
    if AA == 0 and AB != 0 and AC != 0:
        return 23
    if AA != 0 and AB == 0 and AC == 0:
        return 11
    if AA == 0 and AB != 0 and AC == 0:
        return 12
    if AA == 0 and AB == 0 and AC != 0:
        return 13
    if AA == 0 and AB == 0 and AC == 0:
        return 0
    else:
        return -1

# Help

# 3 = All
# 21 = Missing AC
# 22 = Missing AB
# 23 = Missing AA
# 11 = Only has AA
# 12 = Only has AB
# 13 = Only has AC
# 0 = None
# -1 = Error

# Triangle Rules

if 20 < angles() < 24:
    if angles == 21:
        AC = 180 - AA - AB
    elif angles == 21:
        AB = 180 - AA - AC
    elif angles == 21:
        AA = 180 - AC - AB

# Pythagoras

if 20 < sides() < 24:
    # Figuring out which rearrangement of the formula to use
    if sides() == 21:
        if AA == 90:
            sc = math.sqrt(math.pow(sa, 2) - math.pow(sb, 2))
        elif AB == 90:
            sc = math.sqrt(math.pow(sb, 2) - math.pow(sa, 2))
        elif AC == 90:
            sc = math.sqrt(math.pow(sa, 2) + math.pow(sb, 2))
    if sides() == 22:
        if AA == 90:
            sb = math.sqrt(math.pow(sa, 2) - math.pow(sc, 2))
        elif AB == 90:
            sb = math.sqrt(math.pow(sa, 2) + math.pow(sc, 2))
        elif AC == 90:
            sb = math.sqrt(math.pow(sc, 2) - math.pow(sa, 2))
    if sides() == 23:
        if AA == 90:
            sa = math.sqrt(math.pow(sb, 2) + math.pow(sc, 2))
        elif AB == 90:
            sa = math.sqrt(math.pow(sb, 2) - math.pow(sc, 2))
        elif AC == 90:
            sa = math.sqrt(math.pow(sc, 2) - math.pow(sb, 2))
    # SOHCAHTOA Trig
    if AA == 90:
        AB = math.degrees(math.acos(sc / sa))
        AC = 90 - AB
    elif AB == 90:
        AC = math.degrees(math.acos(sa / sb))
        AA = 90 - AC
    elif AC == 90:
        AA = math.degrees(math.acos(sb / sc))
        AB = 90 - AA

# Main SOHCAHTOA

if (10 < sides() < 14 and 20 < angles() < 24) or (20 < sides() < 24 and 10 < angles() < 14): 
    

print("Side A is " + str(sa) + ", Side B is " + str(sb) + ", Side C is " + str(sc) + ".")
print("Angle A is " + str(AA) + ", Angle B is " + str(AB) + ", Angle C is " + str(AC) + ".")