import pygame
import os

pygame.init()
pygame.mixer.init()  

script_dir = os.path.dirname(os.path.abspath(__file__))

#loading images for the tracks cover
screen = pygame.display.set_mode((500, 360))
img = pygame.image.load(os.path.join(script_dir, 'cat_4.png'))
img1 = pygame.image.load(os.path.join(script_dir,'1.jpg'))
img2 = pygame.image.load(os.path.join(script_dir,'6.jpg'))
img3 = pygame.image.load(os.path.join(script_dir,'4.jpg'))
img4 = pygame.image.load(os.path.join(script_dir,'5.jpg'))
img5 = pygame.image.load(os.path.join(script_dir,'2.jpg'))
img6 = pygame.image.load(os.path.join(script_dir,'7.jpg'))
img7 = pygame.image.load(os.path.join(script_dir,'3.jpg'))
img8 = pygame.image.load(os.path.join(script_dir,'8.jpg'))
img9 = pygame.image.load(os.path.join(script_dir,'9.jpg'))
image_1 = pygame.transform.scale(img1, (250, 250))
image_2 = pygame.transform.scale(img2, (250, 250))
image_3 = pygame.transform.scale(img3, (250, 250))
image_4 = pygame.transform.scale(img4, (250, 250))
image_5 = pygame.transform.scale(img5, (250, 250))
image_6 = pygame.transform.scale(img6, (250, 250))
image_7 = pygame.transform.scale(img7, (250, 250))
image_8 = pygame.transform.scale(img8, (250, 250))
image_9 = pygame.transform.scale(img9, (250, 250))
images = [
    image_1, image_2, image_3,  image_4, image_5, image_6, 
    image_7, image_8, image_9
]
#for the main menu's background
rect = img.get_rect()
rect.center = (125, 125)

done = False
black = (0, 0, 0)
white = (255, 255, 255)
tracks = [ os.path.join(script_dir, 'swalla.wav'), 
           os.path.join(script_dir, 'senen_kein.wav'), 
           os.path.join(script_dir, 'baika.mp3'),
           os.path.join(script_dir, 'buttons.mp3') ,
            os.path.join(script_dir, 'Casablanca.mp3') ,
            os.path.join(script_dir, 'kanyelele.mp3') , 
            os.path.join(script_dir, 'heart-attack.mp3'), 
            os.path.join(script_dir, 'sidetoside.mp3'), 
            os.path.join(script_dir, '7rings.mp3')
          ]


current = 0

font = pygame.font.SysFont("Times New Roman", 45, 7)
font1 = pygame.font.SysFont('Times New Roman', 25)

text1 = font.render(" MUSIC PLAYER ", True, white)
text4 = font.render('All songs', True, white)

rect1 = text1.get_rect(topleft=(100, 60))
rect3 = text4.get_rect(topleft=(175, 110))

in_player = False
psmode = True 

def draw_main_menu():
    screen.fill((255, 255, 255))
    screen.blit(img, rect)
    screen.blit(text1, rect1)
    pygame.draw.rect(screen, black, rect1, 3)
    screen.blit(text4, rect3)
    pygame.draw.rect(screen, black, rect3, 3)

font2 = pygame.font.SysFont('Times New Roman', 20)

play_text = font2.render(" PLAY ", True, black)
pause_text = font2.render(" PAUSE ", True, black)
stop_text = font2.render(" STOP ", True, black)
back_text = font2.render(" BACK ", True, black)
next_text = font2.render(" NEXT ", True, black)
quit_text = font2.render(" QUIT ", True, black)

play_rect = play_text.get_rect(topleft=(10, 290))
pause_rect = pause_text.get_rect(topleft=(80, 290))
stop_rect = stop_text.get_rect(topleft=(160, 290))
back_rect = back_text.get_rect(topleft=(230, 290))
next_rect = next_text.get_rect(topleft=(55, 320))
quit_rect = quit_text.get_rect(topleft=(135, 320))

t1 = font2.render('1.SWALLA', True, black)
t2 = font2.render('2.SENEN KEIN', True, black)
t3 = font2.render('3.BAIKA', True, black)
t4 = font2.render('4.BUTTONS', True, black)
t5 = font2.render('5.CASABLANCA', True, black)
t6 = font2.render('6.KANYELELE', True, black)
t7 = font2.render('7.HEART ATTACK', True, black)
t8 = font2.render('8.SIDE TO SIDE', True, black)
t9 = font2.render('9.7 RINGS', True, black)

t_rects = [
    t1.get_rect(topleft=(310,40)),
    t2.get_rect(topleft=(310,70)),
    t3.get_rect(topleft=(310,100)),
    t4.get_rect(topleft=(310,130)),
    t5.get_rect(topleft=(310,160)),
    t6.get_rect(topleft=(310,190)),
    t7.get_rect(topleft=(310,220)),
    t8.get_rect(topleft=(310,250)),
    t9.get_rect(topleft=(310,280))
]

texts = [t1,t2,t3,t4,t5,t6,t7,t8,t9]

def draw_player():
    screen.fill(white) 
    pygame.draw.rect(screen, black, pygame.Rect(10, 10, 270, 270))
    pygame.draw.rect(screen, white, pygame.Rect(18, 18, 254, 254), 2)
    screen.blit(images[current], (20, 20))

    title_text = font1.render(" ALL SONGS ", True, black)
    screen.blit(title_text, (310, 10))

    for i in range(len(texts)):
        screen.blit(texts[i], t_rects[i])
        pygame.draw.rect(screen, white, t_rects[i], 1)

    screen.blit(play_text, play_rect)
    pygame.draw.rect(screen, white, play_rect, 2)

    screen.blit(pause_text, pause_rect)
    pygame.draw.rect(screen, white, pause_rect, 2)

    screen.blit(stop_text, stop_rect)
    pygame.draw.rect(screen, white, stop_rect, 2)

    screen.blit(back_text, back_rect)
    pygame.draw.rect(screen, white, back_rect, 2)

    screen.blit(next_text, next_rect)
    pygame.draw.rect(screen, white, next_rect, 2)

    screen.blit(quit_text, quit_rect)
    pygame.draw.rect(screen, white, quit_rect, 2)

def play_mode(event):
    global psmode, in_player, current

    if play_rect.collidepoint(event.pos):
        pygame.mixer.music.load(tracks[current])
        pygame.mixer.music.play()

    elif pause_rect.collidepoint(event.pos):
        if psmode:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        psmode = not psmode

    elif stop_rect.collidepoint(event.pos):
        pygame.mixer.music.stop()
        psmode = True

    elif back_rect.collidepoint(event.pos):
        in_player = False

    elif next_rect.collidepoint(event.pos):
        current = (current + 1) % len(tracks)
        pygame.mixer.music.load(tracks[current])
        pygame.mixer.music.play()
        psmode = True
    
    elif quit_rect.collidepoint(event.pos):
        pygame.quit()

while not done:
    if not in_player:
        draw_main_menu()
    else:
        draw_player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not in_player:
                if rect3.collidepoint(event.pos):
                    in_player = True
            else:
                
                for i, r in enumerate(t_rects):
                    if r.collidepoint(event.pos):
                        current = i
                        pygame.mixer.music.load(tracks[current])
                        psmode = True

                
                play_mode(event)

    pygame.display.update()

pygame.quit()