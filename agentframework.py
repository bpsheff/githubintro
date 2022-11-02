# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:27:22 2022

@author: benja
"""




"""
import random

class Agent:
 
    def __init__(self):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
 
    def move(self, agents):
        if random.random() < 0.5:
            agents.self.y = (agents.self.y + 1) % 100
        else:
            agents.self.y = (agents.self.y - 1) % 100
            
        if random.random() < 0.5:
            agents.self.x = (agents.self.x + 1) % 100
        else:
            agents.self.x = (agents.self.x - 1) % 100
            
a = agentframework.Agent()