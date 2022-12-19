# IMPORTING MODULES
# For working with CSV files:
import csv
# For plotting maps:
import matplotlib
# For operating system commands:
import os
# For reading/writing multiple files:
import fileinput
# For mathematical operations:
import numpy # as np    


'''
I. Reading in the maps of population density and rat populations
'''
print("I. Reading in the maps of population density and rat populations")
print("PARISH DATA")

# Creating empty environment:
parish = []

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
with open('C:/Users/benja/test/githubintro/Black Death/death.parishes.txt', newline='') as f_p:  # 'r' command implied
    reader = csv.reader(f_p, quoting=csv.QUOTE_NONNUMERIC)    # Maps in CSV format, so read in using csv.reader command:
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
            #print(value)
        parish.append(rowlist)
# Check parish environment matches original dataset
print(parish)
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
matplotlib.pyplot.imshow(parish)
matplotlib.pyplot.show()

print("RATS DATA")
# Creating empty environment:
catch_area = []

# Read rats CSV into environment
with open('C:/Users/benja/test/githubintro/Black Death/death.rats.txt', newline='') as f_r:  # 'r' command implied
    # Maps in CSV format, so read in using csv.reader command:
    reader = csv.reader(f_r, quoting=csv.QUOTE_NONNUMERIC)    
    # For each row:
    for row in reader:
        # Create an empty list:
        rowlist = []
        # For each value in the row:
        for value in row:
            # Append the value to the rowlist:
            rowlist.append(value)
            #print(value)
        catch_area.append(rowlist)
# Check rats environment matches original dataset
print(catch_area)
# Display map        
matplotlib.pyplot.imshow(catch_area)
matplotlib.pyplot.show()


'''
II. Initialising the environment: Creating a map of deaths
'''
print("II. Initialising the environment: Creating a map of deaths")

# Creating empty environment:
environment = []

# Writing to empty file
with open('deaths.csv', 'w', newline='') as f:  
# Hadamard (element-wise) multiplication of parish and rats data using the numpy module
    numpy.multiply(parish, catch_area)
    print(numpy.multiply(parish, catch_area))
    # Within the environment:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)   
    # For each row:
    for row in reader:
        # Create an empty list:
        rowlist = []
        # For each value in the row:
        for value in row:
            d = 1.04*p*r     # need to 
            value = d
            # Append the value to the rowlist:
            rowlist.append(value)
            #print(value)
        environment.append(rowlist)
# Multiply new array by 1.04 to find the deaths
    numpy.multiply(1.04 * environment)  # TypeError: can't multiply sequence by non-int of type 'float'

'''
# Test using equivalent method
    print(parish * catch_area)  # TypeError: can't multiply sequence by non-int of type 'list'



    writer = csv.writer(f, delimiter=' ')           # include delimiter command only if want to create space-delimited instead of csv
    for row in data:         
        writer.writerow(row)


deaths.txt[0,0] = 1.04*death.parishes.txt[0,0]*death.rats.txt[0,0]
deaths.txt[i,i] = 1.04*death.parishes.txt[i,i]*death.rats.txt[i,i]
# file1[i,i] = 1.04*file2[i,i]*file3[i,i]


with open('death.parishes.txt', 'w') as f_p, open('death.rats.txt', 'w') as f_r:
    # Within the environment:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)   
    # For each row:
    for row in reader:
        # Create an empty list:
        rowlist = []
        # For each value in the row:
        for value in row:
            d = 1.04*p*r     # need to 
            value = d
            # Append the value to the rowlist:
            rowlist.append(value)
            #print(value)
        environment.append(rowlist)
       
        
for value in row:
            # replace value with d - write function?
        
'''         

'''
III. Displaying the map of deaths
'''
# Converting to CSV format


# Displaying map of deaths
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()    