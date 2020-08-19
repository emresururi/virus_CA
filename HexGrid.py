import pygame as pg

from VirusCell import *


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
        self.ny_m1 = self.ny - 1
        self.origin = origin
        self.c_i = self.c_j = 0
        self.c_x = self.c_y = 0
        self.maze_map = np.empty((ny, nx), dtype=object)
        self.neighbours = np.empty((ny, nx), dtype=object)
        self.flag_tl = 0
        if self.origin == "tl":
            self.flag_tl = 1
        elif self.origin == "bl":
            self.c_i = self.ny - 1
            self.c_j = 0
            self.c_x , self.c_y = self.ij2xy((self.c_i,self.c_j))
        else:
            # center
            if not center_origin:
                # Center the origin
                self.c_i = round(self.ny / 2 + 0.1)
                self.c_j = round(self.nx / 2 + 0.1) - 1
                # (we're adding 0.1 to always round #.5 to up)
                self.c_x, self.c_y = self.ij2xy((self.c_i, self.c_j))
            else:
                # origin is designated
                self.c_i = center_origin[0]
                self.c_j = center_origin[1]
                self.c_x, self.c_y = self.ij2xy((self.c_i, self.c_j))

        # Initialize cells:
        for i in range(self.ny):
            for j in range(self.nx):
                self.maze_map[i, j] = VirusCell((i + j) % 2)
                # Neighbours
                self.neighbours[i, j] = self.calc_neighbours(i, j)

    def __xy2ij(self, x, y):
        # returns the row-col [i,j] equivalent of (x,y)
        j = self.flag_tl * y + (1 - self.flag_tl) * (x + self.c_x)
        i = self.flag_tl * x + (1 - self.flag_tl) * (-y + self.ny_m1 + int(np.floor(j/2)) - self.c_y)
        return [i, j]

    def __ij2xy(self, i, j):
        # returns the corresponding (x,y) equivalent of row-col [i,j]
        x = self.flag_tl * i + (1 - self.flag_tl)  * (j - self.c_x)
        y = self.flag_tl * j + (1 - self.flag_tl) * (int(self.ny_m1 - i + np.floor(j/2)) - self.c_y)
        return [x, y]

    def __ij2qr(self,i,j):
        # to efficiently store the cells, we need a internal mapping
        q = i - int(np.floor(j/2))
        r = j
        return [q,r]

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
        # pg.init()
        pg.display.init()
        clock = pg.time.Clock()
        clock.tick(30)

        res_x = res_y = 480
        disp = pg.display.set_mode((res_x, res_y))
        pg.display.set_caption("HexGrid")
        color_border = pg.Color('purple')
        colors = ("purple", "yellow", "blue", "red", "green", "brown", "orange")
        border_thickness = 8

        # To -optionally- add spaces between the hexagons
        rx = res_x / (self.nx + 1 + np.ceil((self.nx + 1) / 2))
        ry = res_y / (2 * (self.ny + 1))
        print(rx, ry)
        r = np.min((rx, ry))
        print(r)
        # r = int(res_x / max_nx_ny / 2)
        r_sqrt_3_half = r * np.sqrt(3) / 2
        hex_distance = 2
        r0 = r - hex_distance

        # Position of the [0,0] row-col hex center
        x_translation = 0.75 * ((self.nx + 1) % 2) + 1 * (self.nx % 2)
        x_cent = int(x_translation * r + (res_x - (self.nx + np.ceil(self.nx / 2)) * r) / 2)
        y_cent = int(1.5 * r_sqrt_3_half + (res_y - self.ny * 2 * r_sqrt_3_half) / 2)
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
                pg.draw.polygon(disp, pg.Color(colors[self.maze_map[i, j].state]),
                                hex_points + [x_cent, y_cent] + (i + (np.floor(j / 2))) * vec_a + j * vec_b)
        pg.display.flip()
        while pg.event.wait().type != pg.QUIT:
            pass
