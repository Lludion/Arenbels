
from arenbels.game.dpixel import DPixel
from arenbels.tools import Grid

def grid_to_world(filename):
    """
    Parses a world file (.arb) into a real World object
    """
    with open(filename,"r") as file:
        state = 0
        coresp_dict = {}
        for l in file.readlines():
            if state == 0:
                if l[0] != '#':
                    if l[-2] == '#':#test if maritime region
                        new_reg = ("sea",l[1:-2])
                    else:
                        new_reg = ("reg",l[1:-1])
                    coresp_dict[l[0]] = new_reg
                else:
                    state = 1
            elif state == 1:
                length = int(l)
                state = 2
            elif state == 2:
                height = int(l)
                grid = [[DPixel(x=x,y=y) for y in range(height)] for x in range(length)]
                state = 3
            elif state == 3:
                if l[0] == '#':
                    state = 4
                    c_y = 0#line offset (current y)
            elif state == 4:
                #adding the walkability of pixels
                if c_y < height:
                    for c_x in range(length):
                        c = l[c_x]
                        cp = grid[c_x][c_y]
                        if c == "0":
                            cp.walk = False
                            cp.swim = False
                        elif c == "1":
                            cp.walk = True
                            cp.swim = False
                        elif c == "2":
                            cp.walk = False
                            cp.swim = True
                        elif c == "3":
                            cp.walk = True
                            cp.swim = True
                    c_y += 1
                else:
                    if l[0] == '#':
                        state = 5
                        c_y = 0#line offset (current y)
            elif state == 5:
                #adding the regions to pixels
                if c_y < height:
                    for c_x in range(length):
                        grid[c_x][c_y].region = coresp_dict[l[c_x]]

                    c_y += 1
        return length,height,Grid(grid)