from VirusCell import *
import pygame as pg


class HexGrid:
    def __init__(self, nx, ny, origin="tl", center_origin=()):
        """Initialize the hex grid.
        The grid contains nx columns and ny rows
        and origin can be assigned to one of:
            * "center"
            * "tl" - Top left
            * "bl" - Bottom left
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
        elif self.origin == "bl":
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
                self.neighbours[i, j] = self.calc_neighbours(i, j)

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
        [i, j] = self.__xy2ij(x, y)
        self.maze_map[i, j] = obj

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

    def get_neighbours(self, x, y):
        [i, j] = self.__xy2ij(x, y)
        return list(map(self.ij2xy, self.neighbours[i, j]))

    # TODO: Draw (export to SVG) or visualization method
    def visualize(self):
        # Visualizes the grid using PyGame
        pg.init()
        clock = pg.time.Clock()
        clock.tick(30)

        res_x = res_y = 480
        disp = pg.display.set_mode((res_x, res_y))
        pg.display.set_caption("HexGrid")
        color_border = pg.Color('purple')
        border_thickness = 8

        # To -optionally- add spaces between the hexagons
        max_nx_ny = self.ny + self.nx/2
        max_ny_nx = self.nx + self.ny/2
        max_nxy = np.max((max_nx_ny,max_ny_nx))
        r = int(res_x / max_nx_ny / 2)
        print(r)
        # r = 48.0
        r_sqrt_3_half = r*np.sqrt(3)/2
        hex_distance = 5
        r0 = r - hex_distance

        # Position of the [0,0] row-col hex center
        x_cent = int(3*r/2)
        y_cent = (self.nx+1)*r_sqrt_3_half
        print(y_cent)


        vec_a = (np.array([0, 1]) * np.sqrt(3) * r).astype(int)
        vec_b = (np.array([3, -np.sqrt(3)]) * r / 2).astype(int)
        pg.draw.rect(disp, color_border, [0, 0, res_x, res_y], border_thickness + 5)

        # Define the hexagon corners
        hex_points = []
        theta = np.pi / 3
        for i in range(6):
            hex_points.append([np.cos(theta * i) * r0, np.sin(theta * i) * r0])
        hex_points = np.array(hex_points).astype(int)

        for i in range(self.ny):
            for j in range(self.nx):
                pg.draw.polygon(disp, color_border, hex_points + [x_cent, y_cent] + i * vec_a + j * vec_b)

        pg.display.flip()
