# this class represents the dynamics for a swarm of planar double integrator robots. for simulation 
# stability friction is modeled as a damper where friction force is divided by a nominal velocity to 
# create a damping coefficient.  

import numpy as np

class SwarmDynamics:
    def __init__(self, agents, initial_state, frequency):
        self.agents = agents
        self.State = initial_state
        self.num_states = 4
        self.num_inputs = 2
        self.Input = np.zeros((self.agents, self.num_inputs))
        self.dt = 1/frequency
        
        # define physics parameters
        self.m = 1 # kg
        self.v_nom = 1 # m/s
        self.mu = 0.3 # friction coeff [unitless]
        self.g = 9.81 # m/s^2
        
    def update(self, State, Input):
        """update dynamics forward one time step into the future"""
        # update dynamic variables
        self.State = np.reshape(State, (self.agents, self.num_states))
        self.Input = np.reshape(Input, (self.agents, self.num_inputs))
        
        # predict future state (numerical integration)
        self.rk4()
        
        return self.State
        
    def rk4(self):
        """Use Runge-Kutta 4 to numerically integrate state forward one timestep"""
        # calculate derivative slopes
        k1 = self.states_dot(statestep = 0)
        k2 = self.states_dot(statestep=k1*self.dt/2.0)
        k3 = self.states_dot(statestep=k2*self.dt/2.0)
        k4 = self.states_dot(statestep=k3*self.dt)
        
        # update state
        self.State = self.State + self.dt/6.0 * (k1 + 2*k2 + 2*k3 + k4)
        
    def states_dot(self, statestep):
        """Calcluate current timestep's state derivative"""
        # reshape global state vector into matrix (# of agents x # of local states) for vectorized computation
        X = self.State + statestep
        U = self.Input
        
        # calculate damping coefficient vector b
        v_mag = np.sqrt(X[:,2]**2 + X[:,3]**2)
        b = (self.mu*self.m*self.g*v_mag)/self.v_nom
        
        # calculate state derivative matrix
        X_dot = np.zeros((self.agents, self.num_states))
        X_dot[:,0] = X[:,2]
        X_dot[:,1] = X[:,3]
        X_dot[:,2] = (U[:,0] - b*X[:,2])*self.m
        X_dot[:,3] = (U[:,1] - b*X[:,3])*self.m
        
        return X_dot