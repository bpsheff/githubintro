# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:30:39 2022

@author: benja
"""

import random
import operator
import matplotlib.pyplot
import agentframework
import csv


with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    rowlist = []
    rowlist.append(value)
    environment.append(rowlist)
    # for row in reader:
    #     environment.append(rowlist)
    #     for value in row:
    #         rowlist.append(value)
    #         print(value)

#Check data properly read in
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

a = agentframework.Agent()
print(a.y, a.x)
#Test
a.move()
print(a.y, a.x)

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

#Scatter plot
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)