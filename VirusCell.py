import numpy as np


class VirusCell:
    def __init__(self, state):
        self.state = state
        self.neighbors = ()

    def set_neighbors(self, neighbors):
        self.neighbors = np.array(neighbors)
