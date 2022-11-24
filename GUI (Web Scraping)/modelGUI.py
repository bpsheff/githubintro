# Import all modules needed
import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import agentframeworkGUI
import csv
import tkinter

#Random seed set equal to zero
random.seed(0)

import requests
import bs4

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html', verify=False)
content = r.text    # string created from text file
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)


#Creating the environment in which agents move around
environment = []    # making empty list
with open('C:/Users/benja/test/githubintro/in.txt', newline='') as f:           # Renamed for efficiency
    dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowlist = []    # making empty list
        for value in row:
            # print(value)
            rowlist.append(value)
        environment.append(rowlist)

# # Check data are properly read in                    # Uncomment to run check
# matplotlib.pyplot.imshow(environment)
# matplotlib.pyplot.show()

def run():
    animation = matplotlib.animation.FuncAnimation(
        fig, update, frames=gen_function, repeat=False)
    canvas.draw()       # creates animation

# Function returning distance between agents
def distance_between(a, b):                                                     
    return (((a.x - b.x)**2) + ((a.y - b.y)**2))**0.5

num_of_agents = 101              # Adjust according to desired number of agents
num_of_iterations = 100
neighbourhood = 20
agents = []

# For animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Create GUI
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)


# Making the agents
for i in range(num_of_agents):
    # agents.append([random.randint(0,99), random.randint(0,99)])
    agents.append(agentframeworkGUI.Agent(i, environment, agents))
    if (i >= len(td_ys)):
        y = None
        x = None
        # y = random.randint(0,99)
        # x = random.randint(0,99)
    else:
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
    agents.append(agentframeworkGUI.Agent(i, environment, agents, y, x))

# Printing the agents
for i in range(len(agents)):
    print(agents[i].x, agents[i].y)

print("Test: Printing agents[1] from agents[0]")
print(agents[0].agents[1])

carry_on = True	

# Move the agents
def update(frame_number):
    
    print ("iteration", frame_number)
    fig.clear()
    global carry_on

    # random.shuffle(agents)
    for i in range(len(agents)):
        agents[i].move()        
    for i in range(len(agents)):                                              
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

    # Stopping condition:
        
    stop = False
    count = 0
    for i in range(num_of_agents):                                              
        if (agents[i].store > 80):        
            count = count + 1
    if count == len(agents):
        print("stopping condition at frame", frame_number)
        carry_on = False
    
    # print("After move:")
    # # Display the agents
    # for i in range (num_of_agents):
    #     print(agents[i].x, agents[i].y)
    
    #Scatter plot
    matplotlib.pyplot.xlim(0, 99)   #setting range of x-axis
    matplotlib.pyplot.ylim(0, 99)   #y-axis range
    matplotlib.pyplot.imshow(environment)   #displaying agents in environment                                 
                # (may have to select Model -> Run model within Model window) 
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    # matplotlib.pyplot.show()
    canvas.draw()
    
def gen_function(b = [0]):
    a = 0
    global carry_on    #for clarity only
    while (a < 10) & (carry_on) :
        yield a		                    
        a = a + 1

# animation = matplotlib.animation.FuncAnimation(
#     # fig, update, interval=1, repeat=False, frames=num_of_iterations)
# animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)


for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
# # Writing out the environment:
# with open('dataout.csv', 'w', newline='') as f2:
#     writer = csv.writer(f2, delimiter=',')
#     for row in environment:
#         writer.writerow(row)                                 


tkinter.mainloop()