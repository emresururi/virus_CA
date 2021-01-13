################################################################################################################
# Hücresel otomata tabanlı olasılığa bağlı virus yayılma modeli,                                               #
# maskeli hücreler ve bağışıklık kazanmış hücre durumları modelde mevcut                                       #
# İstenilen sayıda hücre, hasta hücre ve maskeli hücre ile başlatılması mümkün                                 #
# Simulasyon istenilen tur sayısı sonuna ulaştığında simulasyonla ilgili datalar grafik şeklinde gösterilmekte #
################################################################################################################


from HexGrid import *
import random
from matplotlib import pyplot as plt
from scipy.stats import norm
import time
nx = 30
ny = 30
number_of_cell = 350    #başlangıçtaki hasta hücre sayısı
sick_cell = 1          #başlangıçtaki hasta hücre sayısı (toplam hücrelerin içinden)
masked_cell = 35         #maske kullanan hücrelerin sayısı
stop_turn = 200         #Simulasyon uzunluğu



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

# Duvar üreteçleri



for x in range(-2, 3, 2):
    grid_bl.set_wall_xy(x, -12, 4)
    grid_bl.set_wall_xy(x, -12, 3)
for x in range(-1, 3, 2):
    grid_bl.set_wall_xy(x, -13, 1)
    grid_bl.set_wall_xy(x, -13, 2)

for x in range(6, 12, 2):
    grid_bl.set_wall_xy(x, -12, 4)
    grid_bl.set_wall_xy(x, -12, 3)
for x in range(5, 12, 2):
    grid_bl.set_wall_xy(x, -13, 1)
    grid_bl.set_wall_xy(x, -13, 2)

for x in range(16, 22, 2):
    grid_bl.set_wall_xy(x, -12, 4)
    grid_bl.set_wall_xy(x, -12, 3)
for x in range(15, 22, 2):
    grid_bl.set_wall_xy(x, -13, 1)
    grid_bl.set_wall_xy(x, -13, 2)

for x in range(26, 27, 2):
    grid_bl.set_wall_xy(x, -12, 4)
    grid_bl.set_wall_xy(x, -12, 3)
for x in range(25, 27, 2):
    grid_bl.set_wall_xy(x, -13, 1)
    grid_bl.set_wall_xy(x, -13, 2)




class cell(object):
    def __init__(self):

        self.x = random.randint(nx_lim_l, nx_lim_r)
        self.y = random.randint(ny_lim_l, ny_lim_r)
        self.possibility = [1,2,]
        self.possibility_in = [1,2,1,1]
        self.possibility_mask = [1,2,3,4,5,6,7]
        self.possibility_mask_in = [1,2,3,4,5,]
        self.dirty_floor_posiblity = [1,2,3,4,5,6,7,8,9]
        self.dirty_floor_posiblity_in = [1,2,3,4,5]
        self.pdc = random.randint(0,11)
        self.live_or_death = ["L1", "L2", "L3","L4","L5","L6","L7","L8","L9","L10","L11","L12","L13","L14","L15","L16","L17","L18","L19",]
        self.sick_state = 3
        self.deathly_sick_state = 5
        self.death_state = 0
        self.deathly_sick_posibility = "healthy"
        self.live_death = "Live"
        self.dirty_floor_or_normal = [0,6]
        self.dirty_floor_in = [0,9,9]
        self.deathly = False
        self.disease = False
        self.mask_chance = [True,False,True,False]
        self.mask = False
        self.duration_of_illnes = random.randint(15, 20)
        self.state = 4
        self.sick_possibility = 0
        self.immunity = False
        self.immunity_calc = random.randint(190,200)
    # hareketi tanımlayan fonksiyon
    def move(self):
        self.Life = True
        self.komsular = grid_bl.get_neighbours(self.x, self.y)
        gidecegi_yer = random.choice(self.komsular)

        if self.state >= 2:
            #   Sağlıklı Hücrelerin hareket tanımı
            if self.state == 4:
                if grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state == 4:
                    #self.komsular.remove(gidecegi_yer)
                    self.komsular = [x for x in self.komsular if not (x==gidecegi_yer).all()]
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
                    if self.immunity == False:
                        if self.y >= -12:
                            if self.mask == True:
                                self.sick_possibility = random.choice(self.possibility_mask_in)
                            else:
                                self.sick_possibility = random.choice(self.possibility_in)
                        if self.y <= -12:
                            if self.mask == True:
                                self.sick_possibility = random.choice(self.possibility_mask)
                            else:
                                self.sick_possibility = random.choice(self.possibility)
                    #self.komsular.remove(gidecegi_yer)
                    self.komsular = [x for x in self.komsular if not (x == gidecegi_yer).all()]
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
                    if self.immunity == False:
                        if self.y >= -12:
                            self.dirty_floor_sick = random.choice(self.dirty_floor_posiblity_in)
                        if self.y <= -12:
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
                    # self.komsular.remove(gidecegi_yer)
                    self.komsular = [x for x in self.komsular if not (x == gidecegi_yer).all()]
                    new_pos = random.choice(self.komsular)
                    print("yasak konum silindi ve yeni konum seçildi")
                    #print("yeni konum", new_pos)
                    grid_bl.get_xy(new_pos[0], new_pos[1]).state = grid_bl.get_xy(self.x, self.y).state
                    grid_bl.get_xy(new_pos[0], new_pos[1]).state = self.state
                    if self.y >= -12:
                        grid_bl.get_xy(self.x, self.y).state = random.choice(self.dirty_floor_in)
                    if self.y <= -12:
                        grid_bl.get_xy(self.x, self.y).state = random.choice(self.dirty_floor_or_normal)
                    self.x = new_pos[0]
                    self.y = new_pos[1]
                    self.komsular.append(gidecegi_yer)
                else:
                    grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = grid_bl.get_xy(self.x, self.y).state
                    grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = self.state
                    if self.y >= -12:
                        grid_bl.get_xy(self.x, self.y).state = random.choice(self.dirty_floor_in)
                    if self.y <= -12:
                        grid_bl.get_xy(self.x, self.y).state = random.choice(self.dirty_floor_or_normal)
                    self.x = gidecegi_yer[0]
                    self.y = gidecegi_yer[1]





        if self.sick_possibility == 1:
            #print("Hastalandı")
            self.disease = True
            self.state = self.sick_state

        if self.disease == True:
            self.duration_of_illnes -= 1
            self.deathly_sick_posibility = random.randint(0,300)
            #print(self.deathly_sick_posibility)
            #print("hastalatıktaki gün",self.duration_of_illnes)
            self.sick_possibility = 0

            if self.duration_of_illnes <= 0:
                self.sick_possibility = 0
                self.deathly_sick_posibility = 0
                self.state = 4
                print("iyilesti")
                self.disease = False
                self.immunity = True
                return self.duration_of_illnes

        if self.immunity == True:
            self.immunity_calc -= 1
            if self.immunity_calc <= 0:
                self.immunity = False

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
immu = 0
infected_cell = [sick_cell]
healthy_cell = [number_of_cell-sick_cell]
death_cell = [0]
mask_cell = [0]
immunity_cell = [0]
r_g = [0]
s_g = [number_of_cell]
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
        if i.immunity == True:
            immu += 1
    s = y - immu
    s_g.append(s)
    r = immu + z
    r_g.append(r)
    immunity_cell.append(immu)
    infected_cell.append(x)
    healthy_cell.append(y)
    death_cell.append(z)
    mask_cell.append(f)
    y = 0
    x = 0
    f = 0
    immu = 0
    s = 0
    r = 0
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
                dirty_floor = random.randint(0, 40)
                #print("floor",dirty_floor)
                if dirty_floor == 5:
                    grid_bl.get_xy(i, j).state = 0
                    dirty_floor = 0

total = len(cells) - len(healthy_cell) + len(death_cell)
infy =np.mean(infected_cell)

print(infy)

plt.xlabel('Tur')
plt.ylabel('Hucre Sayısı')
plt.title('Virus simulasyonu')
#plt.plot(turn_number, n_cell, color="Orange")
#plt.plot(turn_number,immunity_cell, color= "blue")
#plt.plot(turn_number, infected_cell, color="Red")
#plt.plot(turn_number, healthy_cell, color="Green")
#plt.plot(turn_number, death_cell, color="DarkRed")
#plt.plot(turn_number, mask_cell, color="Yellow")
plt.plot(turn_number, s_g, color="yellow")
plt.plot(turn_number, infected_cell, color="Red")
plt.plot(turn_number,r_g, color= "green")
plt.plot(turn_number,death_cell, color= "Brown")

plt.legend(['S','I', 'R','D'])
plt.show()
