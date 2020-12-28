from HexGrid import *
import random
from matplotlib import pyplot as plt
#import time
nx = 10
ny = 10

nx_lim_l, nx_lim_r = -nx/2, nx/2
ny_lim_l, ny_lim_r = -ny/2, ny/2
nx_list = []
ny_list = []
for i in range(nx + 1):
    n1 = -nx/2 + i
    nx_list.append(int(n1))
for i in range(ny + 1):
    n = -ny/2 + i
    ny_list.append(int(n))

# Origin (in terms of i,j)
oi = 3
oj = 2

grid_bl = HexGrid(nx, ny, "center", (oi, oj))


#self.x = random.randint(nx_lim_l, nx_lim_r)
#self.y = random.randint(ny_lim_l, ny_lim_r)



#yatay duvar üreteci


class cell(object):
    def __init__(self):

        self.x = random.randint(nx_lim_l, nx_lim_r)
        self.y = random.randint(ny_lim_l, ny_lim_r)
        self.possibility = [1, 2, 3, 4]
        self.possibility_in = [1, 2]
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
        if grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 6 or grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 6:
            if self.y >= -2:
                self.dirty_floor_sick = random.choice(self.dirty_floor_posiblity_in)
            elif self.y <= -2:
                self.dirty_floor_sick = random.choice(self.dirty_floor_posiblity)
            if self.dirty_floor_sick == 1:
                print("zeminden bulastı")
                self.sick_possibility = 1
                self.dirty_floor_sick = 0
            grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = 0
        if grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 3 or grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 5 and self.state == 4:
            if self.y >= -2:
                self.sick_possibility = random.choice(self.possibility_in)
            elif self.y <= -2:
                self.sick_possibility = random.choice(self.possibility)
            #self.state -= 1
            self.komsular.remove(gidecegi_yer)
            new_pos = random.choice(self.komsular)
            #print("yasak konum silindi ve yeni konum seçildi")
            #print("yeni konum", new_pos)
            grid_bl.get_xy(new_pos[0], new_pos[1]).state = grid_bl.get_xy(self.x, self.y).state
            grid_bl.get_xy(new_pos[0], new_pos[1]).state = self.state
            grid_bl.get_xy(self.x, self.y).state = 0
            self.x = new_pos[0]
            self.y = new_pos[1]
            self.komsular.append(gidecegi_yer)
        #gidecegi yerde bir hücre varsa oraya gitmiyor
        elif grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 2 and grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 3 and grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 4 and grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 5:
            self.komsular.remove(gidecegi_yer)
            new_pos = random.choice(self.komsular)
            print("yasak konum silindi ve yeni konum seçildi")
            #print("yeni konum", new_pos)
            grid_bl.get_xy(new_pos[0], new_pos[1]).state = grid_bl.get_xy(self.x, self.y).state
            grid_bl.get_xy(new_pos[0], new_pos[1]).state = self.state
            if self.state == 4:
                grid_bl.get_xy(self.x, self.y).state = 0
            elif self.state == 3 or self.state == 5:
                grid_bl.get_xy(self.x, self.y).state = random.choice(self.dirty_floor_or_normal)
            self.x = new_pos[0]
            self.y = new_pos[1]
            self.komsular.append(gidecegi_yer)

        # state 2 den buyukse ve baska etken yoksa normal random hareket ediyor
        elif self.state >= 2:
            grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = grid_bl.get_xy(self.x, self.y).state
            grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = self.state
            if self.state == 4:
                grid_bl.get_xy(self.x, self.y).state = 0
            elif self.state == 3 or self.state == 5:
                if self.y <= -2:
                    grid_bl.get_xy(self.x, self.y).state = random.choice(self.dirty_floor_or_normal)
                elif self.y >= -2:
                    grid_bl.get_xy(self.x, self.y).state = self.dirty_floor_in
            self.x = gidecegi_yer[0]
            self.y = gidecegi_yer[1]
        #eger hucrenin state i 2 ye esit olduysa hucreyi olduruyor


        if self.sick_possibility == 1:
            print("Hastalandı")
            self.disease = True
            self.state = self.sick_state

        if self.disease == True:
            self.duration_of_illnes -= 1
            self.deathly_sick_posibility = random.randint(0,11)
            print(self.deathly_sick_posibility)
            print("hastalatıktaki gün",self.duration_of_illnes)
            self.sick_possibility = 0

            if self.duration_of_illnes <= 0:
                self.sick_possibility = 0
                self.deathly_sick_posibility = 0
                self.state = 4
                self.sick_possibility = 0
                print("iyilesti")
                self.disease = False
                return self.duration_of_illnes
        if self.deathly_sick_posibility == 5:
            print("ölümcül durumda")
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
n = 15
sick_cell = 5
#n tane hücre oluşturma

for i in range(n):
    if i < sick_cell:
        Hex_Cell = cell()
        cells.append(Hex_Cell)
        cells[i].sick_possibility = 1
    elif i >= sick_cell:
        Hex_Cell = cell()
        cells.append(Hex_Cell)

#for i in range(sick_cell):
    #cells[i].sick_possibility = 1


#hücrelerin hareketini güncelliyor ve olen hucreleri siliyor
Running = True
turn = 0
while Running == True:
    turn += 1
    turn_number.append(turn)
    a = len(cells)
    n_cell.append(a)
    if turn == 100:
        break
    #print("tur",turn)
    #if len(cells) == 8:
        #break
    for i in cells:
        i.move()
        if i.Life == False:
            cells.remove(i)


    grid_bl.visualize()




    #state i 1 e esıt olan tum hucrelerin stateini sıfırlıyor arka planı net görebilmek için yaptım
    for i in nx_list:
        for j in ny_list:
            if grid_bl.get_xy(i, j).state == 1:
                grid_bl.get_xy(i, j).state -= 1
                #print("şu konumda hasta hücre var", [i, j])

            if grid_bl.get_xy(i, j).state == 6:
                dirty_floor = random.randint(0, 20)
                print("floor",dirty_floor)
                if dirty_floor == 5:
                    grid_bl.get_xy(i, j).state = 0
                    dirty_floor = 0
            if grid_bl.get_xy(i, j).state == 9:
                dirty_floor = random.randint(0, 50)
                print("floor",dirty_floor)
                if dirty_floor == 5:
                    grid_bl.get_xy(i, j).state = 0
                    dirty_floor = 0



plt.xlabel('Turn')
plt.ylabel('Total Cell')
plt.title('Graph')
plt.plot(turn_number, n_cell, color="Red")
