from HexGrid import *

nx = 20
ny = 20

# Origin (in terms of i,j)
oi = 3
oj = 2
ox = 7
oy = 2
oa = 9
ob = 8


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
grid_bl.get_xy(0, 0).state = 5
grid_bl.get_xy1(12, 0).state = 5
grid_bl.get_xy1(12, 8).state = 5


print("After the update, the state of the <1,1> cell is now: {:}".format(grid_bl.get_xy(1, 1).state))

# Set its neighbours' states:
for xy in grid_bl.get_neighbours(0, 0):
    # print(xy)
    grid_bl.get_xy(xy[0], xy[1]).state = 2

for xy in grid_bl.get_neighbours(12, 0):
    # print(xy)
    grid_bl.get_xy(xy[0], xy[1]).state = 3

for xy in grid_bl.get_neighbours(12, 8):
    # print(xy)
    grid_bl.get_xy(xy[0], xy[1]).state = 4


# Print the states:
for x in grid_bl.range_x:
    for y in grid_bl.range_y:
        print("{:d},{:d}: {:d}".format(x, y, grid_bl.get_xy(x, y).state), end=" | ")
    print("")

grid_bl.visualize()



