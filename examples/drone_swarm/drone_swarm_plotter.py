import numpy as np
import matplotlib.pyplot as plt

class SwarmPlotter:
    def __init__(self, State):
        self.state = State
        self.num_agents = len(self.state[:,0]) // 4
        
        # Turn on interactive mode for real-time plotting
        plt.ion() 
        
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.ax.set_title("Real-Time Swarm Convergence")
        self.ax.set_xlabel("X Position")
        self.ax.set_ylabel("Y Position")
        self.ax.grid(True)
        
        # Initialize the scatter object. Extract initial positions
        x_pos = self.state[:,0]
        y_pos = self.state[:,1]
        
        self.scatter = self.ax.scatter(x_pos, y_pos, color='blue', edgecolors='k', zorder=3)
        
        # Set fixed or generous limits so the window doesn't bounce around
        max_x = x_pos.max() + 5
        max_y = y_pos.max() + 5
        min_x = x_pos.min() - 5
        min_y = y_pos.min() - 5
        self.ax.set_xlim(min_x, max_x)
        self.ax.set_ylim(min_y, max_y)

    def update_frame(self, state):
        """Updates the plot data and redraws the canvas."""
        self.state = state
        positions = self.state[:,0:2]
        
        # Update the dot positions
        self.scatter.set_offsets(positions)
        
        # 3. Force matplotlib to flush the graphics to the screen
        self.fig.canvas.draw_idle()
        self.fig.canvas.flush_events()