# IMPORTING MODULES
# For working with CSV files
import csv
# For plotting maps
import matplotlib

import os


'''
I. Reading in the maps of population density and rat populations
'''


'''
Initialising the environment
'''
print("II. Initialising the environment")

# Creating empty environment:
environment = []

'''
# Initialising the directory
print("Initialising the directory")
dir = os.getcwd()

print(dir)
#print(dir)
parent = os.path.dirname(dir)
print(parent)
parent = os.path.dirname(parent)
parent = os.path.dirname(parent)
basedir = os.path.dirname(parent)
#print(basedir)
datadir = os.path.join(basedir, 'data')
#print(datadir)
inputdatadir = os.path.join(datadir, 'input')
#print(inputdatadir)
outputdatadir = os.path.join(datadir, 'output')
#print(outputdatadir)
# Open file and read.
file = os.path.join(inputdatadir, 'in.txt')

# Open file and read.
popden.parish = os.path.join(inputdatadir, 'death.parishes.txt')
'''

# Read parish population density CSV into environment
with open('C:/Users/benja/test/githubintro/Black Death/death.parishes.txt', newline='') as f:  # 'r' command implied
#with open('C:/Users/benja/test/githubintro/Black Death/death.parishes.txt', newline='') as popden.parish:  # 'r' command implied

# Maps in CSV format, so read in using csv.reader command:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)    
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
            #print(value)
        environment.append(rowlist)

'''
# Codecademy approach (reading each line separately):
# with open("death.parishes.txt") as popden.parish:
    # pdp.data = popden.parish.readlines()
    # print(pdp.data)
    
# # Powerpoint ('most flexible and detailed') approach:
# popden.parish = open("death.parishes.txt")  # what is popden.parish here?
# pdp.data = []
# for line in popden.parish:
#     parsed_line = str.split(line,",")
#     pdp.data_line = []
#     for word in parsed_line:
#         pdp.data_line.append(pdp.data_line)
#     pdp.data.append(pdp.data_line)
# print(pdp.data)
# popden.parish.close()
'''

# Display map        
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

# Read rats CSV into environment
with open('C:/Users/benja/test/githubintro/Black Death/death.rats.txt', newline='') as f2:  # 'r' command implied

# Maps in CSV format, so read in using csv.reader command:
    reader = csv.reader(f2, quoting=csv.QUOTE_NONNUMERIC)    
    # For each row:
    for row in reader:
        # Create an empty list:
        rowlist = []
        # For each value in the row:
        for value in row:
            # Append the value to the rowlist:
            rowlist.append(value)
            #print(value)
        environment.append(rowlist)

# Display map        
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()


'''
II. Creating a map of deaths
'''


    

# Display map        
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()    