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
font1 = pygame.font.SysFont("verdana", 24)
font2 = pygame.font.SysFont("verdana", 34)

path1 = os.path.join(os.path.abspath(__file__ + '/..'), "Images")
bg = os.path.join(path1, 'map2.png')
background = pygame.transform.scale(pygame.image.load(bg), H_W) #бэк с картой

#Класс для спрайтов-стран:
class Country():    
    def __init__(self, image, name, c_x, c_y, c_width, c_height): #картинка, имя страны, координата x/y, ширина и высота
        self.image = pygame.transform.scale(pygame.image.load(image), (c_width, c_height))
        self.rect = self.image.get_rect()
        self.name_c = name
        self.rect.x = c_x
        self.rect.y = c_y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))  
    def name_counrty(self):  #метод возвращающий название страны, подозреваю что он лишний но как то так
        return(self.name_c)

#класс для кнопочек и панелей
class Panel:
    def __init__(self, p_x, p_y, w, h, image):
        self.rect = pygame.Rect(p_x, p_y, w, h)
        self.rect.x = p_x
        self.rect.y = p_y
        self.image = pygame.transform.scale(pygame.image.load(image), (w, h))
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

pan_po = os.path.join(path1, "panel_point.png")  #кнопка выход из настроек
panel_points = Panel(-34, 365, 230, 230, pan_po)

b_men = os.path.join(path1, "кнопка_в_меню.png")  #кнопка выход из настроек
button_menu = Panel(250, 300, 170, 60, b_men)

b_ag = os.path.join(path1, "Еще_раз.png")  #кнопка выход из настроек
button_again = Panel(230, 370, 220, 60, b_ag)

seti_lea = os.path.join(path1, "настройки_назад.png")  #кнопка выход из настроек
setting_leave = Panel(10, 10, 50, 50, seti_lea)

but_conf_u = os.path.join(path1, "конфликт_кнопка_Украина.png")  #кнопка Украина в настройках
button_conflict_UK = Panel(100, 370, 150, 60, but_conf_u)

but_conf_r = os.path.join(path1, "конфликт_кнопка_Россия.png")   #кнопка роися в настройках
button_conflict_RU = Panel(450, 370, 150, 60, but_conf_r)

setti = os.path.join(path1, "настройки.png")                       #кнопка настроек
settings = Panel(630, 0, 60, 60, setti)

play_b = os.path.join(path1, "Start.png")                         #кнопка начала игры
button_play = Panel(190, 350, 320, 80, play_b)

lea_b = os.path.join(path1, "leave_but.png")                    #кнопка выхода в меню из карты
leave_button = Panel(0, 0, 100, 50, lea_b)

flagok = os.path.join(path1, "настройки.png")                   #флажок првоерки касания
flag = Panel(100, 100, 2, 2, flagok)

panel_text = os.path.join(path1, "Панель_вопроса.png")          #панель вопроса
text_box = Panel(20, -220, 700, 500, panel_text)

#Создаю спрайты-страны:

rashka = os.path.join(path1, 'russia_a.png')
Russia = Country(rashka, 'Россия', 400, 6, 300, 400)

ukr = os.path.join(path1, 'urkaine_a.png')
Ukraine = Country(ukr,'Украина', 447, 107, 300, 400)

bel = os.path.join(path1, 'belarus.png')
Belarus = Country(bel, 'Беларусь' ,407, 47, 300, 400)

ast = os.path.join(path1, 'astonia.png')
Estonia = Country(ast, 'Эстония', 369, -11, 300, 400)

lat = os.path.join(path1, 'latvia.png')
Latvia = Country(lat,'Латвия', 368, 10, 300, 400)

lit = os.path.join(path1, 'litva.png')
Lithuania = Country(lit, 'Литва', 362, 30, 300, 400)

fin = os.path.join(path1, 'finlandia.png')
Finland = Country(fin, 'Финляндия', 372, -82, 300, 400)

shv = os.path.join(path1, 'shecia.png')
Sweden = Country(shv, 'Швеция', 292, -50, 300, 400)

pol = os.path.join(path1, 'Polska.png')
Poland = Country(pol, 'Польша', 317, 70, 300, 400)

alb = os.path.join(path1, 'Albania.png')
Albania = Country(alb, 'Албания', 335, 203, 300, 400)

aust = os.path.join(path1, 'Avstria.png')
Austria = Country(aust, 'Австрия', 255, 122, 300, 400)

belg = os.path.join(path1, 'Belgia.png')
Belgium = Country(belg, 'Бельгия', 159, 81, 300, 400)

bulg = os.path.join(path1, 'Bolgaria.png')
Bulgaria = Country(bulg, 'Болгария', 392, 183, 300, 400)

bos_cher = os.path.join(path1, 'Bos_Chernog.png')
Bosnia_and_Montenegro = Country(bos_cher,'Босния и Герцеговина', 305, 168, 300, 400)

bri = os.path.join(path1, 'Britania.png')
Great_Britian = Country(bri,'Великобритания', 72, 33 , 300, 400)

che = os.path.join(path1, 'Chehia.png')
Czech = Country(che, 'Чехия', 280, 95 , 300, 400)

cher = os.path.join(path1, 'Chernog.png')
Montenegro = Country(cher, 'Черногория', 325, 182 , 300, 400)

dan = os.path.join(path1, 'Dania.png')
Denmark = Country(dan,'Дания', 224, 20, 300, 400)

fran = os.path.join(path1, 'Francia.png')
France = Country(fran, 'Франция', 140, 139, 300, 400)

ger = os.path.join(path1, 'Germania.png')
Germany = Country(ger, 'Германия', 225, 80, 300, 400)

gre = os.path.join(path1, 'Grecia.png')
Greece = Country(gre, 'Греция', 382, 240, 300, 400)

hor = os.path.join(path1, 'Horvatia.png')
Croatia = Country(hor, 'Хорватия', 290, 157, 300, 400)

irl = os.path.join(path1, 'Irlandia.png')
Ireland = Country(irl, 'Ирландия', 1, 0, 300, 400)

isl = os.path.join(path1, 'Islandia.png')
Iceland = Country(isl, 'Исландия', 0, 0, 300, 400)

isp = os.path.join(path1, 'Ispania.png')
Spain = Country(isp,'Испания', 69, 224, 300, 400)

ital = os.path.join(path1, 'Italia.png')
Italy = Country(ital, 'Италия', 249, 194, 300, 400)

luk = os.path.join(path1, 'Luksemburg.png')
Luxembourg = Country(luk,'Люксембург', 180, 95, 300, 400)

mol = os.path.join(path1, 'Moldav.png')
Moldova = Country(mol,'Молдавия', 420, 129, 300, 400)

nid = os.path.join(path1, 'Niderland.png')
Netherlands = Country(nid,'Нидерланды', 172, 64, 300, 400)

nor = os.path.join(path1, 'Norvey.png')
Norway = Country(nor,'Норвегия', 291, -77, 300, 400)

port = os.path.join(path1, 'Portugaly.png')
Portugal = Country(port, 'Португалия', 21, 199, 300, 400)

rom = os.path.join(path1, 'Rumunia.png')
Romania = Country(rom,'Румыния', 386, 143, 300, 400)

ser = os.path.join(path1, 'Serbia.png')
Serbia = Country(ser,'Сербия', 341, 166, 300, 400)

s_m = os.path.join(path1, 'Sev_maked.png')
North_Macedonia = Country(s_m,'Северная Македония', 352, 197, 300, 400)

sheq = os.path.join(path1, 'Shveqcaria.png')
Switzerland = Country(sheq,'Швейцария', 201, 131, 300, 400)

slo = os.path.join(path1, 'Slovakia.png')
Slovakia = Country(slo,'Словакия', 325, 108, 300, 400)

slov = os.path.join(path1, 'Slovenia.png')
Slovenia = Country(slov,'Словения', 275, 140, 300, 400)

ven = os.path.join(path1, 'Vengria.png')
Hungary = Country(ven,'Венгрия', 323, 128, 300, 400)

#список с спрайтами:

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

bg2 = os.path.join(path1, 'menu.png') #бэк меню
background2 = pygame.transform.scale(pygame.image.load(bg2), H_W)

bg3 = os.path.join(path1, 'конфликты.png')  #бэк настроек
background3 = pygame.transform.scale(pygame.image.load(bg3), H_W)

bg4 = os.path.join(path1, 'game_over.png')  #бэк настроек
background4 = pygame.transform.scale(pygame.image.load(bg4), H_W)

scenes = [background2]  #список для переключения сцен

def start_game():
    window.blit(background,(0,0))
    for tresh in l_country:
        tresh.update()
    text_box.update()

points = 0
# random_name = randint(0, len(l_country)-1)

GREEN = (0,255,0)
RED = (255, 0, 0)

#игровой цикл
finish = False

game = True
while game: 
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.MOUSEBUTTONDOWN:  
            x,y = pygame.mouse.get_pos()          
            if button_play.rect.collidepoint(x,y) and background2 in scenes:   #событие кнопка начала игры
                scenes.clear() 
                scenes.append(background) 
                random_name = randint(0, len(l_country)-1)
            move_glag_x = flag.rect.x = x 
            move_glag_y = flag.rect.y = y 
            if button_again.rect.collidepoint(x,y) and background4 in scenes:    #событие вход в настройки
                scenes.clear()
                scenes.append(background)
                points = 0
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
            if button_menu.rect.collidepoint(x,y) and background4 in scenes:    #событие вход в настройки
                scenes.clear()
                scenes.append(background2)
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
                points = 0
            if settings.rect.collidepoint(x,y) and background2 in scenes:    #событие вход в настройки
                scenes.clear()
                scenes.append(background3)
            if setting_leave.rect.collidepoint(x,y) and background3 in scenes:  #событие выход из настроек(настройки чисто что бы развлечь, не знаю что туда впихнуть)
                scenes.clear()
                scenes.append(background2)
            if button_conflict_RU.rect.collidepoint(x,y) and background3 in scenes:  #событие нажали на кнопку россия в настройках
                game = False
                print('Система: обнаружен Орк')
            if button_conflict_UK.rect.collidepoint(x,y) and background3 in scenes:  #событе нажали на кнопку Украина в настройках
                print('Чел нафактил люто')
            if leave_button.rect.collidepoint(x,y) and background in scenes:    #событие выхода из карты
                scenes.clear() 
                scenes.append(background2)
                ev_flag = 0
                l_country = [Russia, Ukraine,  #вот эту длинную фиговину надо запихнуть в функцию, но потом... когда нибудь)
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
    if not finish == True:
        for s in scenes:
            window.blit(s,(0,0))
        if background in scenes:
            
            start_game()
            flag.update()
            leave_button.update()
            panel_points.update()
            #работает хорошо
            for t in l_country:  
                offset = flag.rect.x - t.rect.x, flag.rect.y - t.rect.y 
                p = t.mask.overlap_area(flag.mask,offset)
                if p > 0:
                    name_touch = t.name_counrty()
                    if l_country[random_name].name_counrty() == name_touch:
                        l_country.remove(t)
                        print('Верно')
                        points += 1
                        if len(l_country) != 0:
                            random_name = randint(0, len(l_country)-1)
                        else:
                            scenes.clear()
                            scenes.append(background4)
                    else:
                        text_KUTD = font1.render('Вы выбрали ' +  str(name_touch), 1, (RED))
                        window.blit(text_KUTD,(220,460))
                        l_country.remove(t)
                        random_name = randint(0, len(l_country)-1)

            if len(l_country) > 0:
                ran_n = l_country[random_name].name_counrty()
                text_question = font1.render('Где находится ' +  str(ran_n) + '?', 1, (0, 0, 0))
                window.blit(text_question,(210,5)) 
                text_point = font1.render('Верно ' +  str(points) + '/38' , 1, (255, 255, 255))
                window.blit(text_point,(10,460))
                # text_KUTD = font1.render('Вы выбрали ' +  str(name_touch), 1, (GREEN))
                # window.blit(text_KUTD,(220,460))             
        if background2 in scenes:
            button_play.update()
            settings.update()
        if background3 in scenes:
            button_conflict_RU.update()
            button_conflict_UK.update()
            setting_leave.update()
        if background4 in scenes:
            button_again.update()
            button_menu.update()
            text_right = font2.render(str(points), 1, (0, 255, 0))
            window.blit(text_right,(170,220))
            text_wronge = font2.render(str(38-points), 1, (255, 0, 0))
            window.blit(text_wronge,(480,220))
                                                                                                                
    clock.tick(FPS)
    pygame.display.update()