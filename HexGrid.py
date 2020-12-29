import pygame as pg

from VirusCell import *


class HexGrid:
    def __init__(self, nx: object, ny: object, origin: object = "tl", center_origin: object = ()) -> object:
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
        pg.display.init()
        res_x = res_y = 480
        self.disp = pg.display.set_mode((res_x, res_y))
        self.nx, self.ny = nx, ny
        self.ny_m1 = self.ny - 1
        self.origin = origin
        self.c_i = self.c_j = 0
        self.c_x = self.c_y = 0
        self.maze_map = np.empty((ny, nx), dtype=object)
        self.neighbours = np.empty((ny, nx), dtype=object)
        self.neighbours_all = np.empty((ny, nx), dtype=object)
        self.neighbours_TF = np.empty((ny, nx), dtype=object)
        self.walls = np.empty((ny,nx), dtype=object)
        self.flag_tl = 0
        if self.origin == "tl":
            self.flag_tl = 1
        elif self.origin == "bl":
            self.c_i = self.ny - 1
            self.c_j = 0
            self.c_x, self.c_y = self.ij2xy((self.c_i, self.c_j))
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
        self.x_min = -self.c_x
        self.x_max = self.nx + self.x_min - 1
        self.y_min = -self.c_y
        self.y_max = self.ny + self.y_min - 1
        self.range_x = range(self.x_min, self.x_max + 1)
        self.range_y = range(self.y_min, self.y_max + 1)
        # Initialize cells:
        for q in range(self.ny):
            for r in range(self.nx):
                # q, r = self.ij2qr((i, j))
                x, y = self.qr2xy((q, r))
                # # q, r = self.xy2qr((x, y))
                self.maze_map[q, r] = VirusCell((x + y + 1) % 2)
                # Neighbours
                self.neighbours[q, r] = self.calc_neighbours(x, y)
                k = self.calc_neighbours2(x,y)
                self.neighbours_all[q,r] = k[0][:]
                self.neighbours_TF[q,r] = k[1][:]
                #self.neighbours[q,r] = list(k[0][k[1]])

                self.walls[q,r] = [False,False,False,False,False,False]


    def __xy2ij(self, x, y):
        # returns the row-col [i,j] equivalent of (x,y)
        j = self.flag_tl * y + (1 - self.flag_tl) * (x + self.c_x)
        int_np_floor_j_over_2 = int(np.floor(j / 2))
        i = self.flag_tl * x + (1 - self.flag_tl) * (
                -y + self.ny_m1 + int_np_floor_j_over_2 - self.c_y)
        return [i, j]

    def __ij2xy(self, i, j):
        # returns the corresponding (x,y) equivalent of row-col [i,j]
        int_np_floor_j_over_2 = int(np.floor(j / 2))
        x = self.flag_tl * i + (1 - self.flag_tl) * (j - self.c_x)
        y = self.flag_tl * j + (1 - self.flag_tl) * (self.ny_m1 - i + int_np_floor_j_over_2 - self.c_y)
        return [x, y]

    def __ij2qr(self, i, j):
        # to efficiently store the cells, we need a internal mapping
        q = i - int(np.floor(j / 2))
        r = j
        return [q, r]

    def __qr2ij(self, q, r):
        j = r
        i = q + int(np.floor(j / 2))
        return [i, j]

    def xy2ij(self, xy):
        return self.__xy2ij(xy[0], xy[1])

    def ij2xy(self, ij):
        return self.__ij2xy(ij[0], ij[1])

    def ij2qr(self, ij):
        return self.__ij2qr(ij[0], ij[1])

    def qr2ij(self, qr):
        return self.__qr2ij(qr[0], qr[1])

    def xy2qr(self, xy):
        return self.ij2qr(self.xy2ij(xy))

    def qr2xy(self, qr):
        return self.ij2xy(self.qr2ij(qr))

    def get_xy(self, x, y):
        [q, r] = self.xy2qr((x, y))
        return self.maze_map[q, r]

    def set_cell_xy(self, x, y, obj):
        # Fills the cell at location x,y with object obj
        [q, r] = self.xy2qr((x, y))
        self.maze_map[q, r] = obj

    def set_wall_xy(self,x,y,direction):
        # Sets a wall between the given cell and the direction
        # The direction map is:
        # 0: NW | 1:N | 2: NE | 3: SE | 4:S | 5:SW
        #      1
        #   0     2
        #   5     3
        #      4

        self.get_wall_xy(x,y)[direction] = True
        n =self.get_neighbours_all_xy(x,y)[direction]
        contra_direction = [3,4,5,0,1,2]
        self.get_wall_xy(n[0],n[1])[contra_direction[direction]] = True

    def erase_wall_xy(self,x,y,direction):
        # Sets a wall between the given cell and the direction
        # The direction map is:
        # 0: NW | 1:N | 2: NE | 3: SE | 4:S | 5:SW
        self.get_wall_xy(x,y)[direction] = 0

    def get_wall_xy(self,x,y):
        [q, r] = self.xy2qr((x, y))
        return self.walls[q, r]

    def get_neighboursTF_xy(self,x,y):
        [q, r] = self.xy2qr((x, y))
        return self.neighbours_TF[q, r]

    def get_neighbours_all_xy(self,x,y):
        [q, r] = self.xy2qr((x, y))
        return self.neighbours_all[q, r]

    def calc_neighbours(self, x, y):
        i, j = self.xy2ij((x, y))
        nlist = [[i - 1, j - 1], [i - 1, j], [i, j + 1], [i + 1, j + 1], [i + 1, j], [i, j - 1]]
        """
        nlist.append([x - 1, y - 1])
        nlist.append([x - 1, y])
        nlist.append([x, y - 1])
        nlist.append([x, y + 1])
        nlist.append([x + 1, y])
        nlist.append([x + 1, y + 1])
        """
        nlist = np.array(nlist)
        nlist = np.array(list(map(self.ij2qr, nlist)))
        filt = np.logical_and(np.logical_and(nlist[:, 0] >= 0, nlist[:, 1] >= 0),
                              np.logical_and(nlist[:, 0] < self.ny, nlist[:, 1] < self.nx))
        nlist = nlist[filt]
        nlist = list(map(self.qr2xy, nlist))
        return nlist

    def calc_neighbours2(self, x, y):
        i, j = self.xy2ij((x, y))
        nlist = [[i - 1, j - 1], [i - 1, j], [i, j + 1], [i + 1, j + 1], [i + 1, j], [i, j - 1]]
        """
        nlist.append([x - 1, y - 1])
        nlist.append([x - 1, y])
        nlist.append([x, y - 1])
        nlist.append([x, y + 1])
        nlist.append([x + 1, y])
        nlist.append([x + 1, y + 1])
        """
        nlist = np.array(nlist)
        nlist = np.array(list(map(self.ij2qr, nlist)))
        filt = np.logical_and(np.logical_and(nlist[:, 0] >= 0, nlist[:, 1] >= 0),
                              np.logical_and(nlist[:, 0] < self.ny, nlist[:, 1] < self.nx))
        #nlist = nlist[filt]
        nlist = np.array(list(map(self.qr2xy, nlist)))
        return (nlist,filt)

    def get_neighbours(self, x, y):
        [q, r] = self.xy2qr((x, y))
        possible_directions = self.neighbours_TF[q,r]
        existing_walls = self.walls[q,r]
        possible_neighbors_filter = np.logical_and(possible_directions,np.logical_not(existing_walls))
        return list(self.neighbours_all[q, r][possible_neighbors_filter])

    def get_unwalled_neighbours(self,x,y):
        return np.array(self.get_neighbours_all_xy(x,y))[np.logical_not(np.array(self.get_wall_xy(x,y)))]
    # TODO: Draw (export to SVG) or visualization method
    def visualize(self):
        # Visualizes the grid using PyGame
        # pg.init()
        #pg.display.init()
        clock = pg.time.Clock()
        clock.tick(10)

        res_x = res_y = 480
        #disp = pg.display.set_mode((res_x, res_y))
        pg.display.set_caption("HexGrid")
        color_border = pg.Color('black')
        colors = ("purple", "white", "blue", "red", "green", "darkred", "orange", "chocolate", "darkslategray", "salmon")
        border_thickness = 8

        # To -optionally- add spaces between the hexagons
        rx = res_x / (self.nx + 1 + np.ceil((self.nx + 1) / 2))
        ry = res_y / (2 * (self.ny + 1))
        # # print(rx, ry)
        r = np.min((rx, ry))
        # # print(r)
        r_sqrt_3_half = r * np.sqrt(3) / 2
        hex_distance = 2
        r0 = r - hex_distance

        # Position of the [0,0] row-col hex center
        x_translation = 0.75 * ((self.nx + 1) % 2) + 1 * (self.nx % 2)
        x_cent = int(x_translation * r + (res_x - (self.nx + np.ceil(self.nx / 2)) * r) / 2)
        y_cent = int(1.5 * r_sqrt_3_half + (res_y - self.ny * 2 * r_sqrt_3_half) / 2)
        # # print(y_cent)

        vec_a = (np.array([0, 1]) * np.sqrt(3) * r).astype(int)
        vec_b = (np.array([3, -np.sqrt(3)]) * r / 2).astype(int)
        pg.draw.rect(self.disp, color_border, [0, 0, res_x, res_y], border_thickness + 5)

        # Define the hexagon corners
        hex_points = []
        theta = np.pi / 3
        for i in range(6):
            hex_points.append([np.cos(theta * i) * r0, np.sin(theta * i) * r0])
        hex_points = np.array(hex_points).astype(int)
        hps = [hex_points[1,0],hex_points[1,1],hex_points[0,0],hex_points[2,0],hex_points[3,0],hex_points[4,1]]

        for q in range(self.ny):
            for r in range(self.nx):
                i, j = self.__qr2ij(q, r)
                pg.draw.polygon(self.disp, pg.Color(colors[self.maze_map[q, r].state]),
                                hex_points + [x_cent, y_cent] + (i * vec_a + j * vec_b))

                k1 = np.add([x_cent+hps[0],y_cent+hps[1]],[i * vec_a + j * vec_b])
                k2 = np.add([x_cent +hps[2], y_cent], [i * vec_a + j * vec_b])
                l1 = np.add([x_cent+hps[3],y_cent+hps[1]],[i * vec_a + j * vec_b])
                l2 = np.add([x_cent +hps[4], y_cent], [i * vec_a + j * vec_b])
                m1 = np.add([x_cent+hps[0],y_cent+hps[1]],[i * vec_a + j * vec_b])
                m2 = np.add([x_cent +hps[3], y_cent+hps[1]], [i * vec_a + j * vec_b])
                n1 = np.add([x_cent+hps[3],y_cent+hps[5]],[i * vec_a + j * vec_b])
                n2 = np.add([x_cent +hps[0], y_cent+hps[5]], [i * vec_a + j * vec_b])
                o1 = np.add([x_cent +hps[2], y_cent ], [i * vec_a + j * vec_b])
                o2 = np.add([x_cent +hps[0], y_cent + +hps[5]], [i * vec_a + j * vec_b])
                p1 = np.add([x_cent +hps[4], y_cent ], [i * vec_a + j * vec_b])
                p2 = np.add([x_cent +hps[3], y_cent +hps[5]], [i * vec_a + j * vec_b])

                wall_color = "blue"


                xy = self.ij2xy((i,j))
                walls = self.get_wall_xy(xy[0],xy[1])
                #print(self.ij2xy((i,j)),walls)
                if(walls[3]):
                    # SE (3)
                    pg.draw.line(self.disp,pg.Color(wall_color),(k1[0,0],k1[0,1]),(k2[0,0],k2[0,1]),5)
                if (walls[5]):
                    # SW (5)
                    pg.draw.line(self.disp, pg.Color(wall_color), (l1[0, 0], l1[0, 1]), (l2[0, 0], l2[0, 1]), 5)
                if (walls[4]):
                    # S (4)
                    pg.draw.line(self.disp, pg.Color(wall_color), (m1[0, 0], m1[0, 1]), (m2[0, 0], m2[0, 1]), 5)
                if (walls[1]):
                    # N (1)
                    pg.draw.line(self.disp, pg.Color(wall_color), (n1[0, 0], n1[0, 1]), (n2[0, 0], n2[0, 1]), 5)
                if (walls[2]):
                    # NE (2)
                    pg.draw.line(self.disp, pg.Color(wall_color), (o1[0, 0], o1[0, 1]), (o2[0, 0], o2[0, 1]), 5)
                if (walls[0]):
                    # NW (0)
                    pg.draw.line(self.disp, pg.Color(wall_color), (p1[0, 0], p1[0, 1]), (p2[0, 0], p2[0, 1]), 5)

                pg.display.flip()

        #pg.draw.line(self.disp,pg.Color("blue"),(20,30),(50,70))
        #while pg.event.wait().type != pg.QUIT:
        #    pass
