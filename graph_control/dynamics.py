import numpy as np
import networkx as nx

class Dynamics:
    def __init__(self, G: nx.DiGraph, state_keys: list):
        self.G = G
        self.state_keys = state_keys
        
    def extract_states(self):
        """Extracts node attributes into a NumPy array"""
        