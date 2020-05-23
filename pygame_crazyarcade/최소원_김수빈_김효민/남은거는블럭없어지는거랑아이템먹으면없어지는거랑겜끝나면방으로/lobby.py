import pygame, keyboard, random
from pygame import *
from pygame.locals import *
import gameimage, music, main, room, level

def play(screen,sound, cursor):
    pygame.init()

    # bgm------------------------
    bgm = music.MUSIC('./music/로비.mp3')
    bgm.musicplay(sound)
    # 배경------------------------
    background = pygame.image.load("./image/background/lobby.png").convert()
    background = pygame.transform.scale(background, (800, 600))
    #버튼-------------------------
    quit_button = gameimage.BUTTON('./image/moo.png', (765, 582), True, (35, 35)) #종료
    back_button = gameimage.BUTTON('./image/moo.png', (116, 582), True, (35, 35)) #이전으로
    fastgame_button = gameimage.BUTTON('./image/moo.png', (305, 38), True, (130, 43)) #빠른게임
    room_create_button = gameimage.BUTTON('./image/moo.png', (288, 88), True, (110, 35)) #방만들기
    nomal_button = gameimage.BUTTON('./image/moo.png', (195, 260), True, (125, 165)) #일반모드
    monster_button = gameimage.BUTTON('./image/moo.png', (340, 260), True, (165, 165)) #몬스터모드
    confirm_button = gameimage.BUTTON('./image/moo.png', (345, 485), True, (100, 35)) #확인
    cancel_button = gameimage.BUTTON('./image/moo.png', (460, 485), True, (100, 35)) #취소
    #create좌표------------
    createx = 1000
    createy = 100
    #메달-------------------------
    player1_level = level.Level()
    player1_metal = pygame.image.load('./image/1.png').convert_alpha()
    player1_metal = pygame.transform.scale(player1_metal, (45, 45))
    p1level = player1_level.updateFile(0)  # 1
    if p1level == 2:
        player1_metal = pygame.image.load('./image/2.png').convert_alpha()
        player1_metal = pygame.transform.scale(player1_metal, (45, 45))
    if p1level == 3:
        player1_metal = pygame.image.load('./image/3.png').convert_alpha()
        player1_metal = pygame.transform.scale(player1_metal, (45, 45))
    if p1level == 4:
        player1_metal = pygame.image.load('./image/4.png').convert_alpha()
        player1_metal = pygame.transform.scale(player1_metal, (45, 45))

    #방생성이미지-------------
    nomal_image = pygame.image.load("./image/background/nomal.png").convert_alpha()
    monster_image = pygame.image.load("./image/background/monster.png").convert_alpha()
    createimage = nomal_image
    state = "nomal"
    random_state = ["nomal", "monster"]
    #이미지불러오기-------------
    allSprites = pygame.sprite.OrderedUpdates(quit_button, back_button, room_create_button,cursor, fastgame_button)
    createSprites = pygame.sprite.OrderedUpdates(nomal_button, monster_button, confirm_button, cancel_button, cursor)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                #시작화면-------------
                if back_button.rect.collidepoint(pygame.mouse.get_pos()):
                    main.play(screen, sound, cursor)
                #빠른시작--------------
                if fastgame_button.rect.collidepoint(pygame.mouse.get_pos()):
                    state = random.choice(random_state)
                    room.ROOM(screen, sound, cursor, state, back_button, quit_button)
                #방만들기--------------
                if room_create_button.rect.collidepoint(pygame.mouse.get_pos()): createx = 100
                #일반모드---------------
                if nomal_button.rect.collidepoint(pygame.mouse.get_pos()):
                    createimage = nomal_image
                    state = "nomal"
                #몬스터모드---------------
                if monster_button.rect.collidepoint(pygame.mouse.get_pos()):
                    createimage = monster_image
                    state = "monster"
                #방생성확인---------------
                if confirm_button.rect.collidepoint(pygame.mouse.get_pos()):
                    room.ROOM(screen, sound, cursor, state, back_button, quit_button)
                #방생성취소---------------
                if cancel_button.rect.collidepoint(pygame.mouse.get_pos()):  createx = 1000
            #게임종료----------------------
                if quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                    running = False
            if event.type == pygame.QUIT:  # 종료시 입력시
                running = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE) :  #ESE 누르면 종료
                    running = False
            #창크기전환----------------
            if keyboard.is_pressed('F12'):  # 화면 키우기
                screen = pygame.display.set_mode((800, 600),pygame.FULLSCREEN | HWSURFACE | DOUBLEBUF)  # 해상도 480*320, 전체화면모드, 하드웨어 가속사용, 더블버퍼모드
            if keyboard.is_pressed('F11'):  # 윈도우 모드
                screen = pygame.display.set_mode((800, 600), DOUBLEBUF)  # 해상도 480*320, 윈도우모드, 더블버퍼모드

        screen.blit(background, (0, 0))
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        screen.blit(createimage, (createx, createy))
        screen.blit(player1_metal, (60, 210))
        createSprites.draw(screen)

        pygame.display.update()




    pygame.quit()