'''
# IMPORTING MODULES
'''
print('IMPORTING MODULES')
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

def read_data(filename):
    result = []
    with open(filename, newline='') as f_p:  # 'r' command implied
        reader = csv.reader(f_p, quoting=csv.QUOTE_NONNUMERIC)    # Maps in CSV format, so read in using csv.reader command
        for row in reader:
            rowlist = []
            for value in row:
                rowlist.append(value)
                #print(value)
            result.append(rowlist)
    return result

parish = read_data('death.parishes.txt')
catch_area = read_data('death.rats.txt')
''' 
(Implicit in read_data function)
# # Read parish population density CSV into environment
# with open('death.parishes.txt', newline='') as f_p:  # 'r' command implied
#     reader = csv.reader(f_p, quoting=csv.QUOTE_NONNUMERIC)    # Maps in CSV format, so read in using csv.reader command
#     for row in reader:
#         rowlist = []
#         for value in row:
#             rowlist.append(value)
#             #print(value)
#         parish.append(rowlist)
# Check parish environment matches original dataset
#print(parish)
'''
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
''' 
(Implicit in read_data function)
# print("RATS DATA")
# # Creating empty environment:
# catch_area = []

# # Read rats CSV into environment
# with open('death.rats.txt', newline='') as f_r:  # 'r' command implied
#     # Maps in CSV format, so read in using csv.reader command:
#     reader = csv.reader(f_r, quoting=csv.QUOTE_NONNUMERIC)    
#     # For each row:
#     for row in reader:
#         # Create an empty list:
#         rowlist = []
#         # For each value in the row:
#         for value in row:
#             # Append the value to the rowlist:
#             rowlist.append(value)
#             #print(value)
#         catch_area.append(rowlist)
# Check rats environment matches original dataset
#print(catch_area)
# Display map        
'''
matplotlib.pyplot.imshow(catch_area)
matplotlib.pyplot.show()


'''
II. Initialising the environment: Creating a map of week 1 deaths
'''
print("II. Initialising the environment: Creating a map of deaths")

# Creating empty environment:
death_map = []

'''
List of lists method
'''
# Checking number of rows and columns in each dataset is equal to 400 (as specified in instructions)
print("Rows in parish list = " + str(len(parish))) # 400
print("Rows in  rat catch area list = " + str(len(catch_area))) # 400
print("Columns in parish list = " + str(len(parish[0]))) # 400
print("Columns in rat catch area list = " + str(len(catch_area[0]))) # 400
# Setting number of rows and columns in new (composite) environment dataset equal to parish (chosen arbitrarily)
nrows = len(parish) 
print(nrows)
ncols = len(parish)
print(ncols)

def death_calc(pop, rats):
    d = rats ** 0.8
    if d == 0:
        # 50% death
        death = pop / 2
    else:
        death = pop ** 1.3 / d
    return death
    
    
    
# For each row:
for row in range(nrows):
    # Create an empty list:
    rowlist = []
    # For each value in the row:     # 'column' not 'value'?
    for col in range(ncols):
        # Append value to rowlist:
        
        # d = catch_area[row][col] ** 0.8
        # if d == 0:
        #     # 50% death
        #     death = parish[row][col] / 2
        # else:
        #     death = parish[row][col] ** 1.3 / d
        # rowlist.append(death)
        
        rowlist.append(death_calc(parish[row][col], catch_area[row][col]))
    # 
    death_map.append(rowlist)
# 
#print(death_map)

'''
# Testing

# Using a larger float value to check multiplication works:
for row in range(nrows):   # TypeError: 'int' object is not iterable - convert to floats?
    for col in range(ncols):
        rowlist.append(5.04 * parish[row][col] * catch_area[row][col])
death_map.append(rowlist)
print(death_map)   # values all seem to be larger by a factor of ~5, as expected



# Using len(rats) instead of len(parish)

nrows = len(catch_area) 
ncols = len(catch_area)

for row in nrows:

for col in ncols:

rowlist.append(death.parishes.txt[row][col] + death.rats.txt[row][col])

death_map.append(rowlist)


# Setting row and column lengths manually

nrows = 400 
ncols = 400

for row in nrows:

for col in ncols:

rowlist.append(death.parishes.txt[row][col] + death.rats.txt[row][col])

environment.append(rowlist)
'''

# Converting to CSV format
type(death_map)

# Displaying map of deaths
matplotlib.pyplot.imshow(death_map)   # need to save as csv file first?
matplotlib.pyplot.show()

'''
NumPy method
'''
'''
# Writing to empty file
with open('deaths.csv', 'w', newline='') as f:  
# Hadamard (element-wise) multiplication of parish and rats data using the numpy module
    numpy.multiply(parish, catch_area)
    print(numpy.multiply(parish, catch_area))
    1.04 * numpy.array(environment)
    print(1.04 * numpy.array(environment))
    # Testing
    5.01 * numpy.array(environment)
    print(5.01 * numpy.array(environment))
'''    
    
'''    
# Creating scalar variable for deaths calculations
    scalar = 1.04
# Multiplying by 1.04 as in deaths formula
    numpy.multiply(scalar, environment)
# Printing result
    print(numpy.multiply(scalar, environment))
# Testing calculation method
    scalar2 = 2.0
    numpy.multiply(scalar2, environment)
    print(numpy.multiply(scalar2, environment))
    scalar3 = 3
    numpy.multiply(scalar3, environment)
    print(numpy.multiply(scalar3, environment))
'''

'''
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
'''

'''
    numpy.multiply(1.04 * environment)  # TypeError: can't multiply sequence by non-int of type 'float'

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
III. Creating maps for subsequent weeks
'''
print('Creating maps for subsequent weeks')

# Now we have the number of deaths in each area, we can subtract these from initial parish population to find the updated population at the beginning of week 2

# Creating dataset for population at the beginning of week 2
pop2 = []

# Setting number of rows and columns in new (composite) environment dataset equal to parish (chosen arbitrarily)
nrows = len(parish) 
print(nrows)
ncols = len(parish)
print(ncols)
count = 0
# For each row:
for row in range(nrows):
    # Create an empty list:
    rowlist = []
    # For each value in the row:     # 'column' not 'value'?
    for col in range(ncols):
        # Append value to rowlist:
        pop = parish[row][col] - death_map[row][col]
        if pop > 0:
            rowlist.append(int(pop))
            count = count + 1
        else:
            rowlist.append(0)
    # 
    pop2.append(rowlist)
# 
print(count)
#print(pop2)


'''
# Testing

# Using a larger float value to check multiplication works:
for row in range(nrows):   # TypeError: 'int' object is not iterable - convert to floats?
    for col in range(ncols):
        rowlist.append(5.04 * parish[row][col] * catch_area[row][col])
environment.append(rowlist)
print(environment)   # values all seem to be larger by a factor of ~5, as expected



# Using len(rats) instead of len(parish)

nrows = len(catch_area) 
ncols = len(catch_area)

for row in nrows:

for col in ncols:

rowlist.append(death.parishes.txt[row][col] + death.rats.txt[row][col])

environment.append(rowlist)


# Setting row and column lengths manually

nrows = 400 
ncols = 400

for row in nrows:

for col in ncols:

rowlist.append(death.parishes.txt[row][col] + death.rats.txt[row][col])

environment.append(rowlist)
'''

type(pop2)

# Displaying map of parish population at the beginning of week 2
matplotlib.pyplot.imshow(pop2)
matplotlib.pyplot.show()

# From here we can create a map of deaths for week 2, using the same formula as before, assuming number of rats in each area doesn't change
# Creating the environment for week 2
death_map2 = []

# For each row:
for row in range(nrows):
    # Create an empty list:
    rowlist = []
    # For each value in the row:     # 'column' not 'value'?
    for col in range(ncols):
        # Append value to rowlist:
        rowlist.append(death_calc(pop2[row][col], catch_area[row][col]))
        #rowlist.append(1.04 * pop2[row][col] * catch_area[row][col])
    # 
    death_map2.append(rowlist)
# 
#print(death_map2)

# Displaying map of deaths
matplotlib.pyplot.imshow(death_map2)
matplotlib.pyplot.show()

'''
Week 3
'''
# Repeating for week 3
print('Repeating for week 3')
# Creating dataset for population at the beginning of week 3
pop3 = []

# Setting number of rows and columns in new (composite) death_map dataset equal to parish (chosen arbitrarily)
nrows = len(parish) 
print(nrows)
ncols = len(parish)
print(ncols)

# For each row:
for row in range(nrows):
    # Create an empty list:
    rowlist = []
    # For each value in the row:     # 'column' not 'value'?
    for col in range(ncols):
        # Append value to rowlist:
        rowlist.append(pop2[row][col] - death_map2[row][col])
    # 
    pop3.append(rowlist)
# 
#print(pop3)

'''
# Testing

# Using a larger float value to check multiplication works:
for row in range(nrows):   # TypeError: 'int' object is not iterable - convert to floats?
    for col in range(ncols):
        rowlist.append(5.04 * parish[row][col] * catch_area[row][col])
environment.append(rowlist)
print(environment)   # values all seem to be larger by a factor of ~5, as expected



# Using len(rats) instead of len(parish)

nrows = len(catch_area) 
ncols = len(catch_area)

for row in nrows:

for col in ncols:

rowlist.append(death.parishes.txt[row][col] + death.rats.txt[row][col])

environment.append(rowlist)


# Setting row and column lengths manually

nrows = 400 
ncols = 400

for row in nrows:

for col in ncols:

rowlist.append(death.parishes.txt[row][col] + death.rats.txt[row][col])

environment.append(rowlist)
'''

type(pop3)

# Displaying map of parish population at the beginning of week 3
matplotlib.pyplot.imshow(pop3)
matplotlib.pyplot.show()

# From here we can create a map of deaths for week 3, using the same formula as before, assuming number of rats in each area doesn't change
# Creating the environment for week 3
death_map3 = []

# For each row:
for row in range(nrows):
    # Create an empty list:
    rowlist = []
    # For each value in the row:     # 'column' not 'value'?
    for col in range(ncols):
        # Append value to rowlist:
        rowlist.append(death_calc(pop3[row][col], catch_area[row][col]))
        #rowlist.append(1.04 * pop3[row][col] * catch_area[row][col])
    # 
    death_map3.append(rowlist)
# 
#print(death_map3)

# Displaying map of deaths
matplotlib.pyplot.imshow(death_map3)
matplotlib.pyplot.show()

'''
Week 4
'''
# Repeating for week 4
print('Repeating for week 4')
# Creating dataset for population at the beginning of week 4
pop4 = []

# Setting number of rows and columns in new (composite) environment dataset equal to parish (chosen arbitrarily)
nrows = len(parish) 
print(nrows)
ncols = len(parish)
print(ncols)

# For each row:
for row in range(nrows):
    # Create an empty list:
    rowlist = []
    # For each value in the row:     # 'column' not 'value'?
    for col in range(ncols):
        # Append value to rowlist:
        rowlist.append(pop3[row][col] - death_map3[row][col])
    # 
    pop4.append(rowlist)
# 
#print(pop4)

'''
# Testing

# Using a larger float value to check multiplication works:
for row in range(nrows):   # TypeError: 'int' object is not iterable - convert to floats?
    for col in range(ncols):
        rowlist.append(5.04 * parish[row][col] * catch_area[row][col])
environment.append(rowlist)
print(environment)   # values all seem to be larger by a factor of ~5, as expected



# Using len(rats) instead of len(parish)

nrows = len(catch_area) 
ncols = len(catch_area)

for row in nrows:

for col in ncols:

rowlist.append(death.parishes.txt[row][col] + death.rats.txt[row][col])

environment.append(rowlist)


# Setting row and column lengths manually

nrows = 400 
ncols = 400

for row in nrows:

for col in ncols:

rowlist.append(death.parishes.txt[row][col] + death.rats.txt[row][col])

environment.append(rowlist)
'''
"""
type(pop4)

# Displaying map of parish population at the beginning of week 4
matplotlib.pyplot.imshow(pop4)
matplotlib.pyplot.show()

# From here we can create a map of deaths for week 4, using the same formula as before, assuming number of rats in each area doesn't change
# Creating the environment for week 4
environment4 = []

# For each row:
for row in range(nrows):
    # Create an empty list:
    rowlist = []
    # For each value in the row:     # 'column' not 'value'?
    for col in range(ncols):
        # Append value to rowlist:
        pop3
        rowlist.append(1.04 * pop4[row][col] * catch_area[row][col])
    # 
    environment4.append(rowlist)
# 
print(environment4)

# Displaying map of deaths
matplotlib.pyplot.imshow(environment4)
matplotlib.pyplot.show()
"""