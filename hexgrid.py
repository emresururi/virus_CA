from VirusCell import *


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
        self.maze_map = np.empty((ny, nx), dtype=object)
        self.neighbours = np.empty((ny, nx), dtype=object)
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

        # Initialize cells:
        for i in range(self.ny):
            for j in range(self.nx):
                self.maze_map[i, j] = VirusCell((i + j) % 2)
                # Neighbours
                self.neighbours[i, j] = 5

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

    def xy2ij(self, xy):
        return self.__xy2ij(xy[0], xy[1])

    def ij2xy(self, ij):
        return self.__ij2xy(ij[0], ij[1])

    def get_xy(self, x, y):
        [i, j] = self.__xy2ij(x, y)
        return self.maze_map[i, j]

    def set_cell_xy(self, x, y, obj):
        # Fills the cell at location x,y with object obj
        self.maze_map[x, y] = obj

    def calc_neighbours(self, i, j):
        nlist = [[i - 1, j - 1], [i - 1, j], [i, j - 1], [i, j + 1], [i + 1, j], [i + 1, j + 1]]
        """
        nlist.append([x - 1, y - 1])
        nlist.append([x - 1, y])
        nlist.append([x, y - 1])
        nlist.append([x, y + 1])
        nlist.append([x + 1, y])
        nlist.append([x + 1, y + 1])
        """
        nlist = np.array(nlist)
        filt = np.logical_and(np.logical_and(nlist[:, 0] >= 0, nlist[:, 1] >= 0),
                              np.logical_and(nlist[:, 0] < self.ny, nlist[:, 1] < self.nx))
        nlist = nlist[filt]
        return nlist
