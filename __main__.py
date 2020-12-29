from HexGrid import *
import random
from matplotlib import pyplot as plt
import time
nx = 20
ny = 20
number_of_cell = 200
sick_cell = 10
masked_cell = 10
stop_turn = 200



nx_lim_l, nx_lim_r = -int(nx / 2), int(nx / 2)
ny_lim_l, ny_lim_r = -int(ny / 2), int(ny / 2)
nx_list = []
ny_list = []
for i in range(nx + 1):
    n1 = -nx / 2 + i
    nx_list.append(int(n1))
for i in range(ny + 1):
    n = -ny / 2 + i
    ny_list.append(int(n))

# Origin (in terms of i,j)
oi = 3
oj = 2

grid_bl = HexGrid(nx, ny, "center", (oi, oj))
for x in range(-2, 7, 2):
    grid_bl.set_wall_xy(x, 0, 4)
    grid_bl.set_wall_xy(x, 0, 3)
for x in range(-1, 7, 2):
    grid_bl.set_wall_xy(x, -1, 1)
    grid_bl.set_wall_xy(x, -1, 2)


# self.x = random.randint(nx_lim_l, nx_lim_r)
# self.y = random.randint(ny_lim_l, ny_lim_r)


# yatay duvar üreteci


class cell(object):
    def __init__(self):

        self.x = random.randint(nx_lim_l, nx_lim_r)
        self.y = random.randint(ny_lim_l, ny_lim_r)
        self.possibility = [1,2,3,4]
        self.possibility_in = [1]
        self.possibility_mask = [1,2,3,4,5,6,7]
        self.possibility_mask_in = [1,2,3,4,5,]
        self.dirty_floor_posiblity = [1,2,3,4,5,6,7,8,9,0]
        self.dirty_floor_posiblity_in = [1,2,3,4,5]
        self.pdc = random.randint(0,11)
        self.live_or_death = ["L1", "L1", "L1", "L1", "D"]
        self.sick_state = 3
        self.deathly_sick_state = 5
        self.death_state = 0
        self.deathly_sick_posibility = "healthy"
        self.live_death = "Live"
        self.dirty_floor_or_normal = [0, 6]
        self.dirty_floor_in = 9
        self.deathly = False
        self.disease = False
        self.mask_chance = [True,False,True,False]
        self.mask = False
        self.duration_of_illnes = random.randint(30, 50)
        self.state = 4
        self.sick_possibility = 0
    # hareketi tanımlayan fonksiyon
    def move(self):
        self.Life = True
        self.komsular = grid_bl.get_neighbours(self.x, self.y)
        gidecegi_yer = random.choice(self.komsular)
        #for i in self.komsular:
            #if grid_bl.get_xy(i[0], i[1]).state == 3 and self.state == 4:
                #self.sick_possibility = random.choice(self.possibility)
        if self.state >= 2:
            #   Sağlıklı Hücrelerin hareket tanımı
            if self.state == 4:
                if grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 4:
                    self.komsular.remove(gidecegi_yer)
                    new_pos = random.choice(self.komsular)
                    print("yasak konum silindi ve yeni konum seçildi")
                    #print("yeni konum", new_pos)
                    grid_bl.get_xy(new_pos[0], new_pos[1]).state = grid_bl.get_xy(self.x, self.y).state
                    grid_bl.get_xy(new_pos[0], new_pos[1]).state = self.state
                    grid_bl.get_xy(self.x, self.y).state = 0
                    self.x = new_pos[0]
                    self.y = new_pos[1]
                    self.komsular.append(gidecegi_yer)
                elif grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 3 or grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 5:
                    if self.y >= -2:
                        if self.mask == True:
                            self.sick_possibility = random.choice(self.possibility_mask_in)
                        else:
                            self.sick_possibility = random.choice(self.possibility_in)
                    if self.y <= -2:
                        if self.mask == True:
                            self.sick_possibility = random.choice(self.possibility_mask)
                        else:
                            self.sick_possibility = random.choice(self.possibility)
                    self.komsular.remove(gidecegi_yer)
                    new_pos = random.choice(self.komsular)
                    print("yasak konum silindi ve yeni konum seçildi")
                    #print("yeni konum", new_pos)
                    grid_bl.get_xy(new_pos[0], new_pos[1]).state = grid_bl.get_xy(self.x, self.y).state
                    grid_bl.get_xy(new_pos[0], new_pos[1]).state = self.state
                    grid_bl.get_xy(self.x, self.y).state = 0
                    self.x = new_pos[0]
                    self.y = new_pos[1]
                    self.komsular.append(gidecegi_yer)
                elif grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 6 or grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 9:
                    if self.y >= -2:
                        self.dirty_floor_sick = random.choice(self.dirty_floor_posiblity_in)
                    if self.y <= -2:
                        self.dirty_floor_sick = random.choice(self.dirty_floor_posiblity)
                    if self.dirty_floor_sick == 1:
                        print("zeminden bulastı")
                        self.sick_possibility = 1
                        self.dirty_floor_sick = 0
                    grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = grid_bl.get_xy(self.x, self.y).state
                    grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = self.state
                    grid_bl.get_xy(self.x, self.y).state = 0
                    self.x = gidecegi_yer[0]
                    self.y = gidecegi_yer[1]
                else:
                    grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = grid_bl.get_xy(self.x, self.y).state
                    grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = self.state
                    grid_bl.get_xy(self.x, self.y).state = 0
                    self.x = gidecegi_yer[0]
                    self.y = gidecegi_yer[1]
            elif self.state == 3 or self.state == 5:
                if grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 4 or grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 3 or grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 5:
                    self.komsular.remove(gidecegi_yer)
                    new_pos = random.choice(self.komsular)
                    print("yasak konum silindi ve yeni konum seçildi")
                    #print("yeni konum", new_pos)
                    grid_bl.get_xy(new_pos[0], new_pos[1]).state = grid_bl.get_xy(self.x, self.y).state
                    grid_bl.get_xy(new_pos[0], new_pos[1]).state = self.state
                    if self.y >= -2:
                        grid_bl.get_xy(self.x, self.y).state = self.dirty_floor_in
                    if self.y <= -2:
                        grid_bl.get_xy(self.x, self.y).state = random.choice(self.dirty_floor_or_normal)
                    self.x = new_pos[0]
                    self.y = new_pos[1]
                    self.komsular.append(gidecegi_yer)
                else:
                    grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = grid_bl.get_xy(self.x, self.y).state
                    grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = self.state
                    if self.y >= -2:
                        grid_bl.get_xy(self.x, self.y).state = self.dirty_floor_in
                    if self.y <= -2:
                        grid_bl.get_xy(self.x, self.y).state = random.choice(self.dirty_floor_or_normal)
                    self.x = gidecegi_yer[0]
                    self.y = gidecegi_yer[1]





        if self.sick_possibility == 1:
            #print("Hastalandı")
            self.disease = True
            self.state = self.sick_state

        if self.disease == True:
            self.duration_of_illnes -= 1
            self.deathly_sick_posibility = random.randint(0,11)
            #print(self.deathly_sick_posibility)
            #print("hastalatıktaki gün",self.duration_of_illnes)
            self.sick_possibility = 0

            if self.duration_of_illnes <= 0:
                self.sick_possibility = 0
                self.deathly_sick_posibility = 0
                self.state = 4
                print("iyilesti")
                self.disease = False
                return self.duration_of_illnes
        if self.deathly_sick_posibility == 5:
            #print("ölümcül durumda")
            self.deathly = True
            self.sick_possibility = 0
            self.state = self.deathly_sick_state
        if self.deathly == True:
            self.live_death = random.choice(self.live_or_death)
            if self.live_death == "D":
                self.deathly_sick_posibility = 0
                grid_bl.get_xy(self.x, self.y).state = self.death_state
                self.state = 1
                self.Life = False
                print("hücre öldü")

turn_number = []
n_cell = []
cells = []
#n tane hücre oluşturma

for i in range(number_of_cell):
    if i < sick_cell:
        Hex_Cell = cell()
        cells.append(Hex_Cell)
        cells[i].sick_possibility = 1
    elif i >= sick_cell:
        Hex_Cell = cell()
        cells.append(Hex_Cell)
for i in range(number_of_cell):
    if i >= sick_cell:
        if masked_cell != 0:
            masked_cell -= 1
            cells[i].mask = True


f = 0
z = 0
x = 0
y = 0
infected_cell = [sick_cell]
healthy_cell = [number_of_cell-sick_cell]
death_cell = [0]
mask_cell = [masked_cell]
#hücrelerin hareketini güncelliyor ve olen hucreleri siliyor
Running = True
turn = 0
while Running == True:
    turn += 1
    print(turn,". Tur")
    turn_number.append(turn)
    a = len(cells)
    n_cell.append(a)
    #infected_cell.append(infected_number)
    if turn == stop_turn:
        break
    #print("tur",turn)
    #if len(cells) == 8:
        #break
    for i in cells:
        i.move()
        if i.mask == True:
            f += 1
        if i.disease == True:
            x += 1
        elif i.disease == False:
            y += 1

        if i.Life == False:
            cells.remove(i)
            z += 1
    infected_cell.append(x)
    healthy_cell.append(y)
    death_cell.append(z)
    mask_cell.append(f)
    y = 0
    x = 0
    f = 0
    grid_bl.visualize()




    #state i 1 e esıt olan tum hucrelerin stateini sıfırlıyor arka planı net görebilmek için yaptım
    for i in nx_list:
        for j in ny_list:
            if grid_bl.get_xy(i, j).state == 1:
                grid_bl.get_xy(i, j).state -= 1
                #print("şu konumda hasta hücre var", [i, j])

            if grid_bl.get_xy(i, j).state == 6:
                dirty_floor = random.randint(0, 20)
                #print("floor",dirty_floor)
                if dirty_floor == 5:
                    grid_bl.get_xy(i, j).state = 0
                    dirty_floor = 0
            if grid_bl.get_xy(i, j).state == 9:
                dirty_floor = random.randint(0, 50)
                #print("floor",dirty_floor)
                if dirty_floor == 5:
                    grid_bl.get_xy(i, j).state = 0
                    dirty_floor = 0

total = len(cells) - len(healthy_cell) + len(death_cell)

plt.xlabel('Turn')
plt.ylabel('Total Cell')
plt.title('Hexgrid Disease Simulation')
plt.plot(turn_number, n_cell, color="Orange")
plt.plot(turn_number, infected_cell, color="Red")
plt.plot(turn_number, healthy_cell, color="Green")
plt.plot(turn_number, death_cell, color="DarkRed")
plt.plot(turn_number, mask_cell, color="Yellow")
plt.legend(['Living Cell', 'Infected Cell', 'Healthy Cell','Death cell','Mask cell'])
plt.show()
