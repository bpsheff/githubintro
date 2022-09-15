# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Create variables

import random

y0 = random.randint(0,99)
x0 = random.randint(0,99)

print(y0)
print(x0)

# Random walk one step

if y0 < 50:
    y0 += 1
else:
    y0 -= 1

if x0 < 50:
    x0 += 1
else:
    x0 -= 1

print(y0,x0)

if y0 < 50:
    y0 += 1
else:
    y0 -= 1

if x0 < 50:
    x0 += 1
else:
    x0 -= 1

print(y0,x0)




# Create variables
y1 = random.randint(0,99)
x1 = random.randint(0,99)

# Random walk one step

if y1 < 0.5:
    y1 += 1
else:
    y1 -= 1

if x1 < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1,x1)


if y1 < 0.5:
    y1 += 1
else:
    y1 -= 1

if x1 < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1,x1)


# Distance between points in 100x100 grid

dist = ((y0 - y1)**2 + (x0 - x1)**2)**0.5
print(dist)