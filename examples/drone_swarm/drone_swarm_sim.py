import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt
import time
from drone_swarm_plotter import SwarmPlotter

### Global Simulation Parameters ###
SIM_LENGTH = 60 # seconds
SIM_FREQUENCY = 60 # hertz
PLOT_FREQUENCY = 10 # hertz
AGENTS = 100


### Generate a Random Geometric Graph ###
# n = 100 nodes, radius = 0.25
rad = 0.25
G = nx.random_geometric_graph(n=AGENTS, radius=rad, dim=2)

# 2. Extract node positions
# NetworkX automatically stores the (x, y) coordinates in a node attribute called 'pos'
pos = nx.get_node_attributes(G, "pos")

### main simulation loop ###
start_time = time.perf_counter()
current_time = 0.0
next_plot = 0.0

# instantiate classes and initialize states
plotter = SwarmPlotter(State)

while current_time < SIM_LENGTH:
    while current_time < next_plot:
        
        # first step: find input via controller

        # Step 2: update dynamics

        # step 3: check if its time to plot and update plots


        # step 4: add time step
        time.sleep(1.0/SIM_FREQUENCY) # change if using multiple threads
        current_time = time.perf_counter() - start_time
        
    # update animation
    plotter.update_frame(State)
    
    # update next plot time
    next_plot = current_time + 1/PLOT_FREQUENCY
    
### Display Simulation Metrics ###