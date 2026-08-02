import numpy as np
from scipy.linalg import solve_continuous_are

class SwarmController:
    def __init__(self, Param, Initial_state):
        self.A = Param["A"]
        self.B = Param["B"]
        self.L = Param["L"]
        
        self.state = Initial_state
        self.input = np.zeros((Param["num_inputs"]*Param["num_states"], 1))
        
        self.Q = Param["Q"]
        self.R = Param["R"]
        
        self.K = self.calculate_gains()
        
    def update(self, state):
        # calculate control input using consensus
        u = -np.kron(self.L, self.K) @ self.state
        
        # feedback linearization (adding friction back to the input)
        
        return self.input
    
    def calculate_gains(self):
        # check controllability
        self.kalman_controllability()
        
        # solve the algebraic riccotti equation for P
        P = solve_continuous_are(self.A, self.B, self.Q, self.R)
        
        # extract optimal gains matrix
        R_inv = np.linalg.inv(self.R)
        self.K = R_inv @ self.B.T @ P
        
        
        
    def kalman_controllability(self):
        # initialize controllability matrix
        n = self.A.shape[1]
        m = self.B.shape[1]
        C_AB = np.zeros((n,m*n))
        
        # populate matrix
        for i in range(0,n):
            start_col = i*m
            end_col   = i*m + m
            C_AB[:, start_col:end_col] = np.linalg.matrix_power(self.A, i) @ self.B
            
        # check rank of controllability matrix
        rank = np.linalg.matrix_rank(C_AB)
        if rank == n: 
            pass
        else:
            raise ValueError(f"system is partially controllable. rank: {rank}")
          