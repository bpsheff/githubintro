# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## Create variables and empty agents list

import random
import operator
import matplotlib.pyplot

num_agents = 20

random.seed(1)

agents = []

for i in range(num_agents):
    agents.append([random.randint(0,99), random.randint(0,99)])
agents.append([random.randint(0,99), random.randint(0,99)])

agents.append([16, 5])
agents.append([14, 40])
agents.append([16, 5])
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
print("max(agents)", max(agents))
print("max(agents, key=operator.itemgetter(0))", max(agents, key=operator.itemgetter(0)))
print("max(agents, key=operator.itemgetter(1))", max(agents, key=operator.itemgetter(1)))
print("min(agents)", min(agents))
print("min(agents, key=operator.itemgetter(0))", min(agents, key=operator.itemgetter(0)))
print("min(agents, key=operator.itemgetter(1))", min(agents, key=operator.itemgetter(1)))


# Distance between points in 100x100 grid

#dist = ((agents[0][0] - agents[1][0])**2 + (agents[0][1] - agents[1][1])**2)**0.5
#print(dist)


## Graph Plotting

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(len(agents)):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0], color='GREY')
#matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
#matplotlib.pyplot.scatter(agents[2][1],agents[2][0])
#matplotlib.pyplot.scatter(agents[3][1],agents[3][0])

bottom = min(agents, key=operator.itemgetter(0))
print(bottom)
matplotlib.pyplot.scatter(bottom[1], bottom[0], color='BLACK')

top = max(agents, key=operator.itemgetter(0))
print(top)
matplotlib.pyplot.scatter(top[1], top[0], color='RED')

right = max(agents, key=operator.itemgetter(1))
print(right)
matplotlib.pyplot.scatter(right[1], right[0], color='GREEN')

left = min(agents, key=operator.itemgetter(1))
print(left)
matplotlib.pyplot.scatter(left[1], left[0], color='YELLOW')

##Change colour of furthest east agent

###Use largest x-coordinate to indicate the agent furthest east

#if x = max(agents, key=operator.itemgetter(1)):
#    matplotlib.pyplot.scatter(x-coordinate, y-coordinate, color='red')
#    matplotlib.pyplot.show()