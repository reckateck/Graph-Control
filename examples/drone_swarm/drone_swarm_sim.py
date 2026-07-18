import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt
import time

### Global Simulation Parameters ###
SIM_LENGTH = 60 # seconds
SIM_FREQUENCY = 60 # hertz


### Generate a Random Geometric Graph ###
# n = 100 nodes, radius = 0.25
rad = 0.25
G = nx.random_geometric_graph(n=100, radius=rad, dim=2)

# 2. Extract node positions
# NetworkX automatically stores the (x, y) coordinates in a node attribute called 'pos'
pos = nx.get_node_attributes(G, "pos")

# 3. Visualize the graph using its physical coordinates
plt.figure(figsize=(6, 6))
nx.draw_networkx_nodes(G, pos, node_size=30, node_color="crimson")
nx.draw_networkx_edges(G, pos, alpha=0.4, edge_color="gray")

plt.title(f"Random Geometric Graph (r = {rad})")
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.axis("off")
plt.show()

### main simulation loop ###
start_time = time.perf_counter()
current_time = 0.0

# instantiate classes and initialize states

while current_time < SIM_LENGTH:
    
    # first step: find input via controller
    
    # Step 2: update dynamics
    
    # step 3: check if its time to plot and update plots
    
    # step 4: add time step
    time.sleep(1.0/SIM_FREQUENCY) # change if using multiple threads
    current_time = time.perf_counter() - start_time
    
### Display Simulation Metrics ###