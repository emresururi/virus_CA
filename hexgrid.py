import numpy as np


class hexgrid:
    def __init__(self, nx, ny, origin="tl", center_origin=()):
        """Initialize the hex grid.
        The grid contains nx columns and ny rows
        and origin can be assigned to one of:
            * "center"
            * "tl" - Top left
            * "br" - Bottom right
        cells.
        % optional 'center_origin' parameter specifies
             the (row-col) position of the center. If it is omitted,
             origin is defined as the center for odd number of rows/cols
             and {left/up} cell for even numbers.

        """
        self.nx, self.ny = nx, ny
        self.origin = origin
        self.c_i = self.c_j = 0
        self.maze_map = np.empty((nx, ny), dtype=object)
        self.flag_tl = 0
        if self.origin == "tl":
            self.flag_tl = 1
        elif self.origin == "br":
            self.c_i = self.ny - 1
            self.c_j = 0
        else:
            # center
            if not center_origin:
                self.c_i = round(self.nx / 2 + 0.1) - 1
                self.c_j = round(self.ny / 2 + 0.1) - 1
                # (we're adding 0.1 to always round #.5 to up)
            else:
                # origin is designated
                self.c_i = center_origin[0]
                self.c_j = center_origin[1]

    def __xy2ij(self, x, y):
        # returns the row-col [i,j] equivalent of (x,y)
        i = self.flag_tl * x + (1 - self.flag_tl) * (self.c_i - y)
        j = self.flag_tl * y + (1 - self.flag_tl) * (self.c_j + x)
        return [i, j]

    def __ij2xy(self, i, j):
        # returns the corresponding (x,y) equivalent of row-col [i,j]
        x = self.flag_tl * i + (1 - self.flag_tl) * (j - self.c_j)
        y = self.flag_tl * j + (1 - self.flag_tl) * (self.c_i - i)
        return [x, y]
    def xy2ij(self,x,y):
        return self.__xy2ij(x,y)
    def ij2xy(self,x,y):
        return self.__ij2xy(x,y)
    def get_xy(self, x, y):
        [i, j] = self.__xy2ij(x, y)
        return self.maze_map[i, j]

    def set_cell_xy(self, x, y, obj):
        # Fills the cell at location x,y with object obj
        self.maze_map[x, y] = obj

    def neighbours(self, x, y):
        nlist = [[x - 1, y - 1], [x - 1, y], [x, y - 1], [x, y + 1], [x + 1, y], [x + 1, y + 1]]
        """
        nlist.append([x - 1, y - 1])
        nlist.append([x - 1, y])
        nlist.append([x, y - 1])
        nlist.append([x, y + 1])
        nlist.append([x + 1, y])
        nlist.append([x + 1, y + 1])
        """
        nlist = np.array(nlist)
        return nlist
