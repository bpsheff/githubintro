import random

class Agent():
    
    def __init__(self, i, environment, agents, y = None, x = None):            
        self.i = i
        self.environment = environment
        self.agents = agents
        self.store = 0
        if x == None:
            self.x = random.randint(0, 99)
        else:
            self.x = x
        if y == None:
            self.y = random.randint(0, 99)
        else:    
            self.y = y
        
    def __str__(self):
        return "i=" + str(self.i) + "store=" + str(self.store) + ", x=" + \
            str(self.x) + ", y=" + str(self.y)
                
    def move(self):
        
        # Adjust x-coordinate
        if random.randint(0, 1) == 0: # random condition
            self.x = self.x + 1     # adds 1 to x-coordinate if condition met
        else:
            self.x = self.x - 1     # subtracts 1 if condition met
        
        #Adjust y-coordinate
        if random.randint(0,1) == 0:
            self.y = self.y + 1
        else:
            self.y = self.y - 1
    
    #Function allowing agents to erode, or 'eat' their environment        
    def eat(self):                                                              
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0

    def share_with_neighbours(self, neighbourhood):
        # Loop through the agents in self.agents
        for i in range(len(self.agents)):
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(self.agents[i])
            # If distance is less than or equal to the neighbourhood:
            if distance <= neighbourhood:
                # Average (half the sum of self.store and agent.store):
                ave = (self.store + self.agents[i].store) / 2
                self.store = ave
                self.agents[i].store = ave
                print("sharing " + str(distance) + " " + str(ave))

    def distance_between(self, b):
        return (((self.x - b.x)**2) + ((self.y - b.y)**2))**0.5
