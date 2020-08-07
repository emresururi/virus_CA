from HexGrid import *

# Create a "bottom-left" origin, 4-cell wide x 3-cell high grid
grid_bl = HexGrid(4, 4, "bl")

# List the neighbours of the cell at <1,1>
# (since this is a 'bl' grid, it is the "up 1, right one" to the origin
# at the bottom-left)
print(grid_bl.get_neighbours(1, 1))

# Get its state:
print(grid_bl.get_xy(1, 1).state)

# Set its state:
grid_bl.get_xy(1, 1).state = 5
print(grid_bl.get_xy(1, 1).state)

# Set its neighbours states:
for xy in grid_bl.get_neighbours(1, 1):
    #print(xy)
    grid_bl.get_xy(xy[0], xy[1]).state = 4

# Print the states:
for i in range(3):
    for j in range(4):
        xy = grid_bl.ij2xy((i, j))
        x = xy[0]
        y = xy[1]
        print("{:d},{:d}: {:d}".format(x, y, grid_bl.get_xy(x, y).state))

grid_bl.visualize()