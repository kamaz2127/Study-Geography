import pygame
import os
from random import randint
import time

width = 700
height = 500
H_W = (700, 500)

window = pygame.display.set_mode(H_W)
pygame.display.set_caption("Study Georaphy")

FPS = 60
clock = pygame.time.Clock()

pygame.font.init()
font2 = pygame.font.SysFont("verdana", 32)

path1 = os.path.join(os.path.abspath(__file__ + '/..'), "Images")
bg = os.path.join(path1, 'map2.png')
background = pygame.transform.scale(pygame.image.load(bg), H_W)

class Country():
    def __init__(self, image, name, c_x, c_y, c_width, c_height): 
        self.image = pygame.transform.scale(pygame.image.load(image), (c_width, c_height))
        self.rect = self.image.get_rect()
        self.name_c = name
        self.rect.x = c_x
        self.rect.y = c_y
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def name_counrty(self):
        return(self.name_c)

rashka = os.path.join(path1, 'russia_a.png')
Russia = Country(rashka, 'Russia', 400, 6, 300, 400)

ukr = os.path.join(path1, 'urkaine_a.png')
Ukraine = Country(ukr,'Ukraine', 447, 107, 300, 400)

bel = os.path.join(path1, 'belarus.png')
Belarus = Country(bel, 'Belarus' ,407, 47, 300, 400)

ast = os.path.join(path1, 'astonia.png')
Estonia = Country(ast, 'Estonia', 369, -11, 300, 400)

lat = os.path.join(path1, 'latvia.png')
Latvia = Country(lat,'Latvia', 368, 10, 300, 400)

lit = os.path.join(path1, 'litva.png')
Lithuania = Country(lit, 'Lithuania', 362, 30, 300, 400)

fin = os.path.join(path1, 'finlandia.png')
Finland = Country(fin, 'Finland', 372, -82, 300, 400)

shv = os.path.join(path1, 'shecia.png')
Sweden = Country(shv, 'Sweden', 292, -50, 300, 400)

pol = os.path.join(path1, 'Polska.png')
Poland = Country(pol, 'Poland', 317, 70, 300, 400)

alb = os.path.join(path1, 'Albania.png')
Albania = Country(alb, 'Albania', 335, 203, 300, 400)

aust = os.path.join(path1, 'Avstria.png')
Austria = Country(aust, 'Austria', 255, 122, 300, 400)

belg = os.path.join(path1, 'Belgia.png')
Belgium = Country(belg, 'Belgium', 159, 81, 300, 400)

bulg = os.path.join(path1, 'Bolgaria.png')
Bulgaria = Country(bulg, 'Bulgaria', 392, 183, 300, 400)

bos_cher = os.path.join(path1, 'Bos_Chernog.png')
Bosnia_and_Montenegro = Country(bos_cher,'Bosnia_and_Montenegro', 305, 168, 300, 400)

bri = os.path.join(path1, 'Britania.png')
Great_Britian = Country(bri,'Great_Britian', 72, 33 , 300, 400)

che = os.path.join(path1, 'Chehia.png')
Czech = Country(che, 'Czech', 280, 95 , 300, 400)

cher = os.path.join(path1, 'Chernog.png')
Montenegro = Country(cher, 'Montenegro', 325, 182 , 300, 400)

dan = os.path.join(path1, 'Dania.png')
Denmark = Country(dan,'Denmark', 224, 20, 300, 400)

fran = os.path.join(path1, 'Francia.png')
France = Country(fran, 'France', 140, 139, 300, 400)

ger = os.path.join(path1, 'Germania.png')
Germany = Country(ger, 'Germany', 225, 80, 300, 400)

gre = os.path.join(path1, 'Grecia.png')
Greece = Country(gre, 'Greece', 382, 240, 300, 400)

hor = os.path.join(path1, 'Horvatia.png')
Croatia = Country(hor, 'Croatia', 290, 157, 300, 400)

irl = os.path.join(path1, 'Irlandia.png')
Ireland = Country(irl, 'Ireland', 1, 0, 300, 400)

isl = os.path.join(path1, 'Islandia.png')
Iceland = Country(isl, 'Iceland', 0, 0, 300, 400)

isp = os.path.join(path1, 'Ispania.png')
Spain = Country(isp,'Spain', 69, 224, 300, 400)

ital = os.path.join(path1, 'Italia.png')
Italy = Country(ital, 'Italy', 249, 194, 300, 400)

luk = os.path.join(path1, 'Luksemburg.png')
Luxembourg = Country(luk,'Luxembourg', 180, 95, 300, 400)

mol = os.path.join(path1, 'Moldav.png')
Moldova = Country(mol,'Moldova', 420, 129, 300, 400)

nid = os.path.join(path1, 'Niderland.png')
Netherlands = Country(nid,'Netherlands', 172, 64, 300, 400)

nor = os.path.join(path1, 'Norvey.png')
Norway = Country(nor,'Norway', 291, -77, 300, 400)

port = os.path.join(path1, 'Portugaly.png')
Portugal = Country(port, 'Portugal', 21, 199, 300, 400)

rom = os.path.join(path1, 'Rumunia.png')
Romania = Country(rom,'Romania', 386, 143, 300, 400)

ser = os.path.join(path1, 'Serbia.png')
Serbia = Country(ser,'Serbia', 341, 166, 300, 400)

s_m = os.path.join(path1, 'Sev_maked.png')
North_Macedonia = Country(s_m,'North_Macedonia', 352, 197, 300, 400)

sheq = os.path.join(path1, 'Shveqcaria.png')
Switzerland = Country(sheq,'Switzerland', 201, 131, 300, 400)

slo = os.path.join(path1, 'Slovakia.png')
Slovakia = Country(slo,'Slovakia', 325, 108, 300, 400)

slov = os.path.join(path1, 'Slovenia.png')
Slovenia = Country(slov,'Slovenia', 275, 140, 300, 400)

ven = os.path.join(path1, 'Vengria.png')
Hungary = Country(ven,'Hungary', 323, 127, 300, 400)


l_country = [Russia, Ukraine,
    Belarus,
    Estonia,
    Latvia,
    Lithuania,
    Finland,
    Sweden,
    Poland,
    Albania,
    Austria,
    Belgium,
    Bulgaria,
    Great_Britian,
    Czech,
    Denmark,
    Bosnia_and_Montenegro,
    Montenegro,
    France,
    Germany,
    Greece,
    Croatia,
    Ireland,
    Iceland,
    Spain,
    Italy,
    Luxembourg,
    Moldova,
    Netherlands,
    Norway,
    Portugal,
    Romania,
    Serbia,
    North_Macedonia,
    Switzerland,
    Slovakia,
    Slovenia,
    Hungary] 


def start_game():
    window.blit(background,(0,0))
    c_country = len(l_country) 
    for tresh in l_country:
        c_country = c_country - 1
        l_country[c_country].update()

# aaaa1 = randint(0, c_count - 1)
# bbbb2 = l_country[aaaa1].sTr()
# for tresh in l_country:
# text_lost = font2.render('Где находиться' + str(bbbb2), 1, (255,0,0))
#  window.blit(text_lost,(10,50)) 
        

game = True
while game:
    start_game()
    
    
    for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                for count in l_country:
                    if count.rect.collidepoint(x,y):
                        print(count.name_counrty())
                        break
                                                                                 
                        


    clock.tick(FPS)
    pygame.display.update()