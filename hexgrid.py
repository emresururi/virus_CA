import numpy as np


class hexgrid():
    def __init__(self, nx, ny, origin="tl"):
        """Initialize the hex grid.
        The grid contains nx columns and ny rows
        and origin can be assigned to one of:
            * "center"
            * "tl" - Top left
            * "br" - Bottom right
        cells.
        """
        self.nx, self.ny = nx, ny
        self.origin = origin
        self.delta_x = 0
        self.delta_y = 0
        self.maze_map = np.empty((nx, ny), dtype=object)
        if (self.origin == "tl"):
            self.delta_x = self.delta_y = 0
    def __xy2ij(self,x,y):
        

    def get_xy(self, x, y):
        return self.maze_map[x - self.delta_x, y - self.delta_y]

    def set_cell_xy(self, x, y, obj):
        # Fills the cell at location x,y with object obj
        self.maze_map[x, y] = obj

    def neighbours(self, x, y):
        list = []
        list.append([x - 1, y - 1])
        list.append([x - 1, y])
        list.append([x, y - 1])
        list.append([x, y + 1])
        list.append([x + 1, y])
        list.append([x + 1, y + 1])
        list = np.array(list)
        return list
