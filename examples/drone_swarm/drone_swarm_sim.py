import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt
import time
from drone_swarm_plotter import SwarmPlotter
from drone_swarm_dynamics import SwarmDynamics

### Global Simulation Parameters ###
SIM_LENGTH = 15 # seconds
SIM_FREQUENCY = 60 # hertz
PLOT_FREQUENCY = 10 # hertz
AGENTS = 10
RAD = 0.25

# Generate the graph
G = nx.random_geometric_graph(n=AGENTS, radius=RAD, dim=2)

# Extract positions and convert dictionary values to a NumPy array
pos_dict = nx.get_node_attributes(G, "pos")
pos = np.array(list(pos_dict.values())) * 10  # Scale up from unit square

# Define global initial state: shape (N, 4) -> [x, y, vx, vy]
INITIAL_STATE = np.zeros((len(pos), 4))
INITIAL_STATE[:, 0:2] = pos
INITIAL_STATE[:, 2:4] = np.ones_like(pos)

### main simulation loop ###
# instantiate classes and initialize states
plotter = SwarmPlotter(INITIAL_STATE)
dynamics = SwarmDynamics(INITIAL_STATE, SIM_FREQUENCY)

# start timer
current_time = 0.0
next_plot = 0.0
start_time = time.perf_counter()

while current_time < SIM_LENGTH:
    while current_time < next_plot:
        
        # first step: find input via controller
        if current_time - start_time < 1.0:
            #u = np.ones_like(pos)
            u = np.zeros_like(pos)
        else:
            u = np.zeros_like(pos)
        
        # Step 2: update dynamics
        x = dynamics.State
        dynamics.update(x,u)

        # step 3: add time step
        time.sleep(1.0/SIM_FREQUENCY) # change if using multiple threads
        current_time = time.perf_counter() - start_time
        
    # update animation
    plotter.update_frame(dynamics.State)
    
    # update next plot time
    next_plot = current_time + 1/PLOT_FREQUENCY
    
### Display Simulation Metrics ###
print(f"Simulation took {time.perf_counter() - start_time} seconds")