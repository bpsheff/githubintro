# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Create variables

import random

y0 = random.random()*100 < 100
x0 = random.random()*100 < 100

# Random walk one step

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0,x0)

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0,x0)




# Create variables
y1 = 50
x1 = 50

# Random walk one step

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y0,x0)
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1,x1)


dist = ((y0 - y1)**2 + (x0 - x1)**2)**0.5
print(dist)