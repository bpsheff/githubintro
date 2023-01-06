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
I. Reading in maps of population density and rat populations
'''
print("I. Reading in the maps of population density and rat populations")
print("PARISH DATA")

# Creating empty lists to store initial population, and rats caught, in each area:
pop1 = []
rats_caught = []

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
# Creating a function to read in each dataset
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

pop1 = read_data('C:/Users/benja/test/githubintro/Black Death/death.parishes.txt')
rats_caught = read_data('C:/Users/benja/test/githubintro/Black Death/death.rats.txt')
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
#         pop1.append(rowlist)
# Check parish environment matches original dataset
#print(pop1)
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
matplotlib.pyplot.imshow(pop1)
matplotlib.pyplot.show()
''' 
(Implicit in read_data function)
# print("RATS DATA")
# # Creating empty environment:
# rats_caught = []

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
#         rats_caught.append(rowlist)
# Check rats environment matches original dataset
#print(rats_caught)
# Display map        
'''
matplotlib.pyplot.imshow(rats_caught)
matplotlib.pyplot.show()


'''
II. Initialising the environment: Creating a map of week 1 deaths
'''
print("II. Initialising the environment: Creating a map of deaths")

# Creating empty environment:
deaths = []
# Writing as CSV file
with open('deaths.csv', 'w', newline = '') as deaths:
    writer = csv.writer(deaths)

# Checking number of rows and columns in each dataset is equal to 400 (as specified in instructions)
print("Rows in parish list = " + str(len(pop1))) # 400
print("Rows in  rat catch area list = " + str(len(rats_caught))) # 400
print("Columns in parish list = " + str(len(pop1[0]))) # 400
print("Columns in rat catch area list = " + str(len(rats_caught[0]))) # 400
# Setting number of rows and columns in new (composite) environment dataset equal to parish (chosen arbitrarily)
nrows = len(pop1) 
# Checking number of rows is as expected
print(nrows)
# Checking number of columns is as expected
ncols = len(pop1)
print(ncols)

# Embedding the deaths formula inside a new function using the list of lists method:
def death_calc(pop, rats):
    # Creating variable for denominator in deaths formula:
    denom = rats ** 0.8
    # Assuming 50% death rate when no rats caught:
    if denom == 0:
        deaths = pop / 2
    # Calculating per area deaths using population (when positive) and rats caught:
    else:
        deaths = pop ** 1.3 / denom
    return deaths    
    
# For each row:
for row in range(nrows):
    # Create an empty list:
    rowlist = []
    # For each value in the row:     # 'column' not 'value'?
    for col in range(ncols):
        # Append value to rowlist:
        rowlist.append(death_calc(pop1[row][col], rats_caught[row][col]))
    deaths.append(rowlist)

# Checking death map data looks as expected
type(deaths)
#print(deaths)

'''
# Testing

# Using a larger float value to check multiplication works:
for row in range(nrows):   # TypeError: 'int' object is not iterable - convert to floats?
    for col in range(ncols):
        rowlist.append(5.04 * parish[row][col] * catch_area[row][col])
deaths.append(rowlist)
print(deaths)   # values all seem to be larger by a factor of ~5, as expected



# Using len(rats) instead of len(parish)

nrows = len(catch_area) 
ncols = len(catch_area)

for row in nrows:

for col in ncols:

rowlist.append(death.parishes.txt[row][col] + death.rats.txt[row][col])

deaths.append(rowlist)


# Setting row and column lengths manually

nrows = 400 
ncols = 400

for row in nrows:

for col in ncols:

rowlist.append(death.parishes.txt[row][col] + death.rats.txt[row][col])

environment.append(rowlist)
'''
# Displaying map of deaths
matplotlib.pyplot.imshow(deaths)
matplotlib.pyplot.show()


'''
III. Creating maps for subsequent weeks
'''
print('III. Creating maps for subsequent weeks')

# Now we have the number of deaths in each area, we can subtract these from initial parish population to find the updated population at the beginning of week 2.

# Creating dataset for population at beginning of week 2:
pop2 = []

# Setting number of rows and columns in new (composite) environment dataset equal to parish (chosen arbitrarily as before):
nrows = len(pop2) 
print(nrows)
ncols = len(pop2)
print(ncols)

# Setting up a count of areas still populated after initial wave of deaths (continued within if-else conditional):
count = 0

def survivors(pop_prev, rats):
    # Calculating population after week 1 deaths:
    pop = pop_prev - deaths
'''
    # # Setting up conditional to distinguish/pick out
    # if pop > 0:
    #     rowlist.append(int(pop))
    #     count = count + 1
    # # Ensuring remaining parish populations cannot be negative:
    # else:
    #     rowlist.append(0)
'''
    
# For each row:
for row in range(nrows):
    # Create empty list:
    rowlist = []
    # For each value in row:     # 'column' not 'value'?
    for col in range(ncols):
        # Setting up conditional to distinguish/pick out
        if pop2 > 0:
            rowlist.append(int(survivors(pop1[row][col], deaths[row][col])))
            count = count + 1
        # Ensuring remaining parish populations cannot be negative:
        else:
            rowlist.append(0)
    # 
    pop2.append(rowlist)
# 
print(count)

# 
#print(pop2)

'''
        # # Calculating population after week 1 deaths:
        # pop2 = pop1[row][col] - deaths[row][col]
'''

'''
# For each row:
for row in range(nrows):
    # Create empty list:
    rowlist = []
    # For each value in row:     # 'column' not 'value'?
    for col in range(ncols):
        # Calculating population after week 1 deaths:
        pop2 = pop1[row][col] - deaths[row][col]
        # Setting up conditional to distinguish/pick out
        if pop2 > 0:
            rowlist.append(int(pop2))
            count = count + 1
        # Ensuring remaining parish populations cannot be negative:
        else:
            rowlist.append(0)
    # 
    pop2.append(rowlist)

'''

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
# Displaying map of parish population at the beginning of week 2
matplotlib.pyplot.imshow(pop2)
matplotlib.pyplot.show()

# From here we can create a map of deaths for week 2, using the same formula as before, assuming number of rats in each area doesn't change
# Creating the environment for week 2
deaths2 = []

# For each row:
for row in range(nrows):
    # Create an empty list:
    rowlist = []
    # For each value in the row:     # 'column' not 'value'?
    for col in range(ncols):
        # Append value to rowlist:
        rowlist.append(death_calc(pop2[row][col], rats_caught[row][col]))
        #rowlist.append(1.04 * pop2[row][col] * rats_caught[row][col])
    # 
    deaths2.append(rowlist)
# 
#print(deaths2)

# Displaying map of deaths
matplotlib.pyplot.imshow(deaths2)
matplotlib.pyplot.show()

'''
Week 3
'''
# Repeating for week 3
print('Repeating for week 3')
# Creating dataset for population at the beginning of week 3
pop3 = []

# Setting number of rows and columns in new (composite) deaths dataset equal to parish (chosen arbitrarily)
nrows = len(pop1) 
print(nrows)
ncols = len(pop1)
print(ncols)

# Setting up a count of areas still populated after initial wave of deaths (continued within if-else conditional):
count = 0

# For each row:
for row in range(nrows):
    # Create empty list:
    rowlist = []
    # For each value in row:     # 'column' not 'value'?
    for col in range(ncols):
        # Setting up conditional to distinguish/pick out
        if pop3 > 0:
            rowlist.append(int(survivors(pop2[row][col], deaths[row][col])))
            count = count + 1
        # Ensuring remaining parish populations cannot be negative:
        else:
            rowlist.append(0)
    # 
    pop3.append(rowlist)
# 
print(count)

'''
# For each row:
for row in range(nrows):
    # Create an empty list:
    rowlist = []
    # For each value in the row:     # 'column' not 'value'?
    for col in range(ncols):
        # Append value to rowlist:
        rowlist.append(pop2[row][col] - deaths2[row][col])
    # 
    pop3.append(rowlist)
'''
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
deaths3 = []

# For each row:
for row in range(nrows):
    # Create an empty list:
    rowlist = []
    # For each value in the row:     # 'column' not 'value'?
    for col in range(ncols):
        # Append value to rowlist:
        rowlist.append(death_calc(pop3[row][col], rats_caught[row][col]))
        #rowlist.append(1.04 * pop3[row][col] * rats_caught[row][col])
    # 
    deaths3.append(rowlist)
# 
#print(deaths3)

# Displaying map of deaths
matplotlib.pyplot.imshow(deaths3)
matplotlib.pyplot.show()

'''
Week 4
'''
# Repeating for week 4
print('Repeating for week 4')
# Creating dataset for population at the beginning of week 4
pop4 = []

# Setting number of rows and columns in new (composite) environment dataset equal to parish (chosen arbitrarily)
nrows = len(pop1) 
print(nrows)
ncols = len(pop1)
print(ncols)

# Setting up a count of areas still populated after initial wave of deaths (continued within if-else conditional):
count = 0

# For each row:
for row in range(nrows):
    # Create empty list:
    rowlist = []
    # For each value in row:     # 'column' not 'value'?
    for col in range(ncols):
        # Setting up conditional to distinguish/pick out
        if pop4 > 0:
            rowlist.append(int(survivors(pop3[row][col], deaths[row][col])))
            count = count + 1
        # Ensuring remaining parish populations cannot be negative:
        else:
            rowlist.append(0)
    # 
    pop4.append(rowlist)
# 
print(count)

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