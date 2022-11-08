# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:27:22 2022

@author: benja
"""

import random

class Agent:
    
    def __init__(self):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
    
    def move(self):
    # def move(self, agents):
        # Adjust x-coordinates    
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
            # agents.self.x = (agents.self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            # agents.self.x = (agents.self.x - 1) % 100        
        # Adjust y-coordinates
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
            # agents.self.y = (agents.self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
            # agents.self.y = (agents.self.y - 1) % 100

        


 

            
# a = agentframework.Agent()