import pygame, keyboard
from pygame import *
from pygame.locals import *
import music, gameimage, lobby

screen = pygame.display.set_mode((800,600), DOUBLEBUF) #고정 화면
pygame.display.set_caption('CrazySuSoMing') #게임 타이틀
sound = 10 #소리 크기
cursor = gameimage.MOUSE() #마우스


def play(screen,sound, cursor): #메인함수
    pygame.init() #초기화

    #bgm------------------------
    bgm = music.MUSIC('./music/mainstart.mp3')
    bgm.musicplay(sound)
    #배경------------------------
    background = pygame.image.load("./image/img/start.png").convert()
    background = pygame.transform.scale(background, (800,600))
    #Button----------------------
    gamestart_button = gameimage.BUTTON('./image/img/bar.png', (300,500), True, (150, 100))
    gamestart_text = gameimage.BUTTON('./image/img/starttext.png', (300,500), True, (100, 50))
    how_button = gameimage.BUTTON('./image/img/bar.png', (500,500), True, (150, 100))
    how_text = gameimage.BUTTON('./image/img/howtext.png', (500,500), True, (100, 50))
    back_button = gameimage.BUTTON('./image/moo.png', (400, 400), True, (125, 50))
    #넥슨로고---------------------
    nexon_image = gameimage.BUTTON('./image/img/nexon2.png', (740, 70), True, (100, 100))
    #모든_스프라이트_이미지_불러오기
    allSprites = pygame.sprite.OrderedUpdates(gamestart_button, gamestart_text, how_button, how_text, nexon_image, back_button,  cursor)
    howSprites = pygame.sprite.OrderedUpdates(back_button, cursor)
    #how좌표------------
    howx = 1000
    howy = 50
    #게임방법이미지-------------
    howimage = pygame.image.load("./image/img/howscreen2.png").convert_alpha()
    howimage = pygame.transform.scale(howimage, (500, 400))


    running = True
    while running:
        for event in pygame.event.get():
            #마우스클릭------------------K
            if event.type == MOUSEBUTTONDOWN:
                #게임시작----------------
                if gamestart_button.rect.collidepoint(pygame.mouse.get_pos()):
                    lobby.play(screen,sound, cursor)
                #게임방법-----------------
                if how_button.rect.collidepoint(pygame.mouse.get_pos()): howx = 150
                elif back_button.rect.collidepoint(pygame.mouse.get_pos()): howx = 1000
            #게임종료-----------------------
            if event.type == pygame.QUIT:  # 종료시 입력시
                running = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE) :  #ESE 누르면 종료
                    running = False
            #창크기전환----------------------
            if keyboard.is_pressed('F12'):  # 화면 키우기
                screen = pygame.display.set_mode((800, 600),pygame.FULLSCREEN | HWSURFACE | DOUBLEBUF)  # 해상도 480*320, 전체화면모드, 하드웨어 가속사용, 더블버퍼모드
            if keyboard.is_pressed('F11'):  # 윈도우 모드
                screen = pygame.display.set_mode((800, 600), DOUBLEBUF)  # 해상도 480*320, 윈도우모드, 더블버퍼모드

        screen.blit(background, (0, 0))
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        screen.blit(howimage, (howx, howy))
        howSprites.draw(screen)

        pygame.display.update()




    pygame.quit()

if __name__ == "__main__" :
    play(screen, sound, cursor)