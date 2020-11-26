from HexGrid import *
import random
import pygame as pg
from time import sleep
nx = 10
ny = 10

# Origin (in terms of i,j)
oi = 3
oj = 2
running = True


# Create a "centralized" origin at (oi,oj), nx-cell wide x ny-cell high grid
grid_bl = HexGrid(nx, ny, "center",(oi,oj))


# List the neighbours of the cell at <1,1>
# (since this is a 'bl' grid, it is the "up 1, right one" to the origin
# at the bottom-left)
print("Here are the list of neighbours of <0,0>:")
print(grid_bl.get_neighbours(0, 0))

# Get its state:
print("The state of the <0,0> cell is: {:}".format(grid_bl.get_xy(0, 0).state))

# Set its state: 3 ayrı state 3 ayrı hasta
grid_bl.get_xy(0, 0).state = 4
grid_bl.get_xy(3, 2).state = 5




print("After the update, the state of the <1,1> cell is now: {:}".format(grid_bl.get_xy(1, 1).state))

# Set its neighbours' states:
#for xy in grid_bl.get_neighbours(0, 0):
    # print(xy)
    #grid_bl.get_xy(xy[0], xy[1]).state = 2

#for xy in grid_bl.get_neighbours(5, 0):
    # print(xy)
    #grid_bl.get_xy(xy[0], xy[1]).state = 3




# Print the states:
for x in grid_bl.range_x:
    for y in grid_bl.range_y:
        print("{:d},{:d}: {:d}".format(x, y, grid_bl.get_xy(x, y).state), end=" | ")
    print("")

print(grid_bl.get_xy(0, 0).state)
mevcut_x1 = 0
mevcut_y1 = 0
mevcut_x2 = 3
mevcut_y2 = 2



for adimlar in range(100):

    orijinal_koordinatlar_x = mevcut_x1
    orijinal_koordinat_y = mevcut_y1
    komsular = grid_bl.get_neighbours(mevcut_x1, mevcut_y1)
    komsular2 = grid_bl.get_neighbours(mevcut_x2, mevcut_y2)
    #infected_area = grid_bl.get_xy(mevcut_x2, mevcut_y2).state = 2
    gidecegi_yer = random.choice(komsular)
    gidecegi_yer2 = random.choice(komsular2)
    grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = grid_bl.get_xy(mevcut_x1, mevcut_y1).state
    grid_bl.get_xy(gidecegi_yer2[0], gidecegi_yer2[1]).state = grid_bl.get_xy(mevcut_x2, mevcut_y2).state
    grid_bl.get_xy(mevcut_x2, mevcut_y2).state = 0
    grid_bl.get_xy(mevcut_x1, mevcut_y1).state = 0
    mevcut_x1 = gidecegi_yer[0]
    mevcut_y1 = gidecegi_yer[1]
    mevcut_x2 = gidecegi_yer2[0]
    mevcut_y2 = gidecegi_yer2[1]
    if mevcut_x1 == mevcut_x2 and mevcut_y1 == mevcut_y2 + 1:
        print("temas")
        break

    if mevcut_x1 == mevcut_x2 + 1 and mevcut_y1 == mevcut_y2:
        print("temas")
        break

    if mevcut_x1 == mevcut_x2 - 1 and mevcut_y1 == mevcut_y2:
        print("temas")
        break

    if mevcut_x1 == mevcut_x2 - 1 and mevcut_y1 == mevcut_y2 - 1:
        print("temas")
        break

    if mevcut_x1 == mevcut_x2 and mevcut_y1 == mevcut_y2 - 1:
        print("temas")
        break

    if mevcut_x1 == mevcut_x2 + 1 and mevcut_y1 == mevcut_y2 - 1:
        break

    sleep(0.1)
    print(adimlar)
    grid_bl.visualize()










