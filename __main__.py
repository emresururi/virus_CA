from HexGrid import *
import random

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

class cell(object):
    def __init__(self):

        self.x = random.randint(nx_lim_l, nx_lim_r)
        self.y = random.randint(ny_lim_l, ny_lim_r)
        self.state = 9
        self.death_state = 0
        self.state_change = 1
        self.pos = [self.x, self.y]
    # hareketi tanımlayan fonksiyon
    def move(self):
        self.Life = True
        self.komsular = grid_bl.get_neighbours(self.x, self.y)
        gidecegi_yer = random.choice(self.komsular)
        #komsu hucrelerinden birinin statei 2 den buyukse yani yakınlarında başka hucre varsa kendi stateini 1 azaltıyor
        for i in self.komsular:
            if grid_bl.get_xy(i[0], i[1]).state >= 2:
                print("temas")
                self.state -= 1
            if grid_bl.get_xy(self.x, self.y).state == 2:
                grid_bl.get_xy(self.x, self.y).state = self.death_state
                self.Life = False
                print("hücre öldü")

        #gidecegi yerde bir hücre varsa oraya gitmiyor
        if grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state >= 2 and self.state >= 2:
            #self.state -= 1
            self.komsular.remove(gidecegi_yer)
            new_pos = random.choice(self.komsular)
            print("yasak konum silindi ve yeni konum seçildi")
            print("yeni konum", new_pos)
            grid_bl.get_xy(new_pos[0], new_pos[1]).state = grid_bl.get_xy(self.x, self.y).state
            grid_bl.get_xy(new_pos[0], new_pos[1]).state = self.state
            grid_bl.get_xy(self.x, self.y).state = 0
            self.x = new_pos[0]
            self.y = new_pos[1]
            self.komsular.append(gidecegi_yer)

        # state 2 den buyukse ve baska etken yoksa normal random hareket ediyor
        elif self.state >= 2:
            grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = grid_bl.get_xy(self.x, self.y).state
            grid_bl.get_xy(gidecegi_yer[0], gidecegi_yer[1]).state = self.state
            grid_bl.get_xy(self.x, self.y).state = 0
            self.x = gidecegi_yer[0]
            self.y = gidecegi_yer[1]
        #eger hucrenin state i 2 ye esit olduysa hucreyi olduruyor
        if grid_bl.get_xy(self.x, self.y).state == 2:
            grid_bl.get_xy(self.x, self.y).state = self.death_state
            self.Life = False
            print("hücre öldü")











#n tane hücre oluşturma
cells = []
n = 5
for i in range(n):
    Cell = cell()
    cells.append(Cell)

#hücrelerin hareketini güncelliyor ve olen hucreleri siliyor
Running = True
turn = 0
while Running:
    turn += 1
    print("tur",turn)
    if len(cells) == 1:
        print("Simulasyon", turn, ".turda tamamlandı")
        break
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
                print("şu konumda hasta hücre var",[i, j])
                break



