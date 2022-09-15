# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Create variables and empty agents list

import random

random.seed(1)

agents = []

agents.append([random.randint(0,99), random.randint(0,99)])
agents.append([random.randint(0,99), random.randint(0,99)])


# Include coordinates at end of agents list

#agents.append([y0,x0])

print(agents)

# Random walk one step

## Randomly change y0 by 1

if random.randint(0,1) == 0:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

## Randomly change x0 by 1

if random.randint(0,1) == 0:
    print("a")
    agents[0][1] += 1
else:
    print("b")
    agents[0][1] -= 1



#if agents[0][0] < 50:
#    agents[0][0] += 1
#else:
#    agents[0][0] -= 1
#
#if agents[0][1] < 50:
#    agents[0][1] += 1
#else:
#    agents[0][1] -= 1


## Randomly change y1 by 1
    
if random.randint(0,1) == 0:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
  
#if agents[1][0] < 50:
#    agents[1][0] += 1
#else:
#    agents[1][0] -= 1

## Randomly change x1 by 1

if random.randint(0,1) == 0:
    agents[1][1] += 1
else:
    agents[1][1] -= 1



print(agents)



# Distance between points in 100x100 grid

dist = ((agents[0][0] - agents[1][0])**2 + (agents[0][1] - agents[1][1])**2)**0.5
print(dist)