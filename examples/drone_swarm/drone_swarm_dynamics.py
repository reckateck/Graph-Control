import numpy as np

class SwarmDynamics:
    def __init__(self, agents, initial_state):
        self.agents = agents
        self.State = initial_state
        self.num_states = 4
        self.num_inputs = 2
        self.Input = np.zeros((self.agents, self.num_inputs))        
        self.X_dot = np.zeros((self.agents, self.num_states))
        
        # define physics parameters
        self.m = 1 # kg
        self.v_nom = 1 # m/s
        self.mu = 0.3 # friction coeff [unitless]
        self.g = 9.81 # m/s^2
        
    def update(self, State, Input):
        """update dynamics forward one time step into the future"""
        # update dynamic variables
        self.State = State
        self.Input = Input
        
        # predict future state (numerical integration)
        self.rk4()
        
    def rk4(self):
        """Use Runge-Kutta 4 to numerically integrate state forward one timestep"""
        
    def states_dot(self):
        """Calcluate current timestep's state derivative"""
        # reshape global state vector into matrix (# of agents x # of local states) for vectorized computation
        X = np.reshape(self.State, (self.agents, self.num_states))
        U = np.reshape(self.Input, (self.agents, self.num_inputs))
        
        # calculate damping coeff. b
        v_mag = np.sqrt(X[:,2]**2 + X[:,3]**2)
        b = (self.mu*self.m*self.g*v_mag)/self.v_nom
        
        # calculate state derivative matrix
        self.X_dot[:,0] = X[:,2]
        self.X_dot[:,1] = X[:,3]
        self.X_dot[:,2] = (U[:,1] - b*X[:,2])*self.m
        self.X_dot[:,3] = (U[:,1] - b*X[:,3])*self.m