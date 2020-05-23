import pygame, keyboard, random, time
from pygame import *
from pygame.locals import *
import monster_map, music, gameimage, lobby,charactor, room, level
import time

def play(screen, sound, cursor, charac, state, back_button, quit_button):
    pygame.init()

    state = "monster"
    clock = pygame.time.Clock()
    #bgm------------------------
    bgm = music.MUSIC('./music/batmap.mp3')
    bgm.musicplay(sound)
    #배경------------------------
    main_background = pygame.image.load('./image/background/game_map.png')
    boss_ground = pygame.image.load('./image/background/bg_monster.png')
    boss_ground = pygame.transform.scale(boss_ground, (600, 520))
    win_image = pygame.image.load('win.png').convert_alpha()
    win_y = 1000
    lose_image = pygame.image.load('lose.png').convert_alpha()
    lose_y = 1000

    player1_level = level.Level()
    player2_level = level.Level2()

    #플레이어 데려오기
    if charac == 1:
        p1= charactor.BAZZY(screen)
        p2= charactor.RODU(screen)
    else :
        p1= charactor.RODU(screen)
        p2= charactor.BAZZY(screen)
    boss = charactor.BOSS(screen)
    testballa = gameimage.WaterBall(screen)
    testballa_left = gameimage.Popleft(screen)
    testballa_right = gameimage.Popright(screen)
    testballa_up = gameimage.Popup(screen)
    testballa_down = gameimage.Popdown(screen)

    testballb = gameimage.WaterBall(screen)
    testballb_left = gameimage.Popleft(screen)
    testballb_right = gameimage.Popright(screen)
    testballb_up = gameimage.Popup(screen)
    testballb_down = gameimage.Popdown(screen)

    group = pygame.sprite.Group()
    group.add(testballa_left,testballa_up,testballa_right,testballa_down,testballb_down,testballb_left,testballb_right,testballb_up)
    #버튼-------------------------
    quit_game = gameimage.BUTTON('./image/moo.png',(720,580),True,(140,30))
    #못부수는맵불러오기-----------
    stop_block_Sprites = monster_map.stop_block() #안움직이는 맵
    #노란블록사라지는이미지-------
    yblock1 = pygame.image.load("./image/무덤/벽돌노란_사라짐 (1).png").convert_alpha()
    yblock2 = pygame.image.load("./image/무덤/벽돌노란_사라짐 (2).png").convert_alpha()
    yblock3 = pygame.image.load("./image/무덤/벽돌노란_사라짐 (3).png").convert_alpha()
    yblock4 = pygame.image.load("./image/무덤/벽돌노란_사라짐 (4).png").convert_alpha()
    yblock5 = pygame.image.load("./image/무덤/벽돌노란_사라짐 (5).png").convert_alpha()
    yblock6 = pygame.image.load("./image/무덤/벽돌노란_사라짐 (6).png").convert_alpha()
    yblock7 = pygame.image.load("./image/무덤/벽돌노란_사라짐 (7).png").convert_alpha()
    yblock8 = pygame.image.load("./image/moo.png").convert_alpha()
    #노란블록리스트--------------
    remove_block1 = [yblock1,yblock2,yblock3,yblock4,yblock5,yblock6,yblock7,yblock8]
    #살구블록사라지는이미지------
    fblock1 = pygame.image.load("./image/무덤/벽돌살구_사라짐 (1).png").convert_alpha()
    fblock2 = pygame.image.load("./image/무덤/벽돌살구_사라짐 (2).png").convert_alpha()
    fblock3 = pygame.image.load("./image/무덤/벽돌살구_사라짐 (3).png").convert_alpha()
    fblock4 = pygame.image.load("./image/무덤/벽돌살구_사라짐 (4).png").convert_alpha()
    fblock5 = pygame.image.load("./image/무덤/벽돌살구_사라짐 (5).png").convert_alpha()
    fblock6 = pygame.image.load("./image/무덤/벽돌살구_사라짐 (6).png").convert_alpha()
    fblock7 = pygame.image.load("./image/무덤/벽돌살구_사라짐 (7).png").convert_alpha()
    fblock8 = pygame.image.load("./image/moo.png").convert_alpha()
    #살구블록리스트--------------
    remove_block2 = [fblock1, fblock2, fblock3, fblock4, fblock5, fblock6, fblock7, fblock8]
    #황토블록사라지는이미지------
    oblock1 = pygame.image.load("./image/무덤/벽돌황토_사라짐 (1).png").convert_alpha()
    oblock2 = pygame.image.load("./image/무덤/벽돌황토_사라짐 (2).png").convert_alpha()
    oblock3 = pygame.image.load("./image/무덤/벽돌황토_사라짐 (3).png").convert_alpha()
    oblock4 = pygame.image.load("./image/무덤/벽돌황토_사라짐 (4).png").convert_alpha()
    oblock5 = pygame.image.load("./image/무덤/벽돌황토_사라짐 (5).png").convert_alpha()
    oblock6 = pygame.image.load("./image/무덤/벽돌황토_사라짐 (6).png").convert_alpha()
    oblock7 = pygame.image.load("./image/무덤/벽돌황토_사라짐 (7).png").convert_alpha()
    oblock8 = pygame.image.load("./image/moo.png").convert_alpha()
    #황토블록리스트--------------
    remove_block3 = [oblock1, oblock2, oblock3, oblock4, oblock5, oblock6, oblock7, oblock8]
    #움직이는 블록들(벽돌노란,벽돌살구,벽돌황토)
    move_block1= gameimage.stop_block('./image/무덤/벽돌노란.png',6,3)
    move_block2 = gameimage.stop_block('./image/무덤/벽돌노란.png', 10, 3)
    move_block3 = gameimage.stop_block('./image/무덤/벽돌노란.png', 6, 4)
    move_block4 = gameimage.stop_block('./image/무덤/벽돌노란.png', 10, 4)
    move_block5 = gameimage.stop_block('./image/무덤/벽돌노란.png', 3, 5)
    move_block6 = gameimage.stop_block('./image/무덤/벽돌노란.png', 4, 5)
    move_block7 = gameimage.stop_block('./image/무덤/벽돌노란.png', 7, 5)
    move_block8 = gameimage.stop_block('./image/무덤/벽돌노란.png', 12, 5)
    move_block9 = gameimage.stop_block('./image/무덤/벽돌노란.png', 13, 5)
    #-------------------------------------------
    move_block10 = gameimage.stop_block('./image/무덤/벽돌황토.png', 3, 6)
    move_block11 = gameimage.stop_block('./image/무덤/벽돌황토.png', 4, 6)
    move_block12 = gameimage.stop_block('./image/무덤/벽돌황토.png', 5, 6)
    move_block13 = gameimage.stop_block('./image/무덤/벽돌황토.png', 6, 6)
    move_block14 = gameimage.stop_block('./image/무덤/벽돌살구.png', 7, 6)
    move_block15 = gameimage.stop_block('./image/무덤/벽돌살구.png', 8, 6)
    move_block16 = gameimage.stop_block('./image/무덤/벽돌살구.png', 9, 6)
    move_block17 = gameimage.stop_block('./image/무덤/벽돌황토.png', 10, 6)
    move_block18 = gameimage.stop_block('./image/무덤/벽돌황토.png', 11, 6)
    move_block19 = gameimage.stop_block('./image/무덤/벽돌황토.png', 12, 6)
    move_block20 = gameimage.stop_block('./image/무덤/벽돌황토.png', 13, 6)
    move_block21 = gameimage.stop_block('./image/무덤/벽돌황토.png', 4, 7)
    move_block22 = gameimage.stop_block('./image/무덤/벽돌황토.png', 5, 7)
    move_block23 = gameimage.stop_block('./image/무덤/벽돌황토.png', 11, 7)
    move_block24 = gameimage.stop_block('./image/무덤/벽돌황토.png', 12, 7)
    #-----------------------------------------------
    move_block25 = gameimage.stop_block('./image/무덤/벽돌노란.png', 6, 8)
    move_block26 = gameimage.stop_block('./image/무덤/벽돌노란.png', 8, 8)
    move_block27 = gameimage.stop_block('./image/무덤/벽돌노란.png', 10, 8)
    move_block28 = gameimage.stop_block('./image/무덤/벽돌노란.png', 7, 9)
    move_block29 = gameimage.stop_block('./image/무덤/벽돌노란.png', 9, 9)
    #-------------------------------------------------
    move_block30 = gameimage.stop_block('./image/무덤/벽돌황토.png', 3, 9)
    move_block31 = gameimage.stop_block('./image/무덤/벽돌살구.png', 4, 9)
    move_block32 = gameimage.stop_block('./image/무덤/벽돌황토.png', 12, 9)
    move_block33 = gameimage.stop_block('./image/무덤/벽돌살구.png', 13, 9)
    move_block34 = gameimage.stop_block('./image/무덤/벽돌살구.png', 1, 10)
    move_block35 = gameimage.stop_block('./image/무덤/벽돌황토.png', 2, 10)
    move_block36 = gameimage.stop_block('./image/무덤/벽돌황토.png', 4, 10)
    move_block37 = gameimage.stop_block('./image/무덤/벽돌살구.png', 5, 10)
    move_block38 = gameimage.stop_block('./image/무덤/벽돌황토.png', 11, 10)
    move_block39 = gameimage.stop_block('./image/무덤/벽돌살구.png', 12, 10)
    move_block40 = gameimage.stop_block('./image/무덤/벽돌살구.png', 14, 10)
    move_block41 = gameimage.stop_block('./image/무덤/벽돌황토.png', 15, 10)
    move_block42 = gameimage.stop_block('./image/무덤/벽돌황토.png', 1, 11)
    move_block43 = gameimage.stop_block('./image/무덤/벽돌황토.png', 5, 11)
    move_block44 = gameimage.stop_block('./image/무덤/벽돌살구.png', 11, 11)
    move_block45 = gameimage.stop_block('./image/무덤/벽돌살구.png', 15, 11)
    move_block46 = gameimage.stop_block('./image/무덤/벽돌살구.png', 1, 12)
    move_block47 = gameimage.stop_block('./image/무덤/벽돌황토.png', 2, 12)
    move_block48 = gameimage.stop_block('./image/무덤/벽돌황토.png', 4, 12)
    move_block49 = gameimage.stop_block('./image/무덤/벽돌살구.png', 5, 12)
    move_block50 = gameimage.stop_block('./image/무덤/벽돌황토.png', 11, 12)
    move_block51 = gameimage.stop_block('./image/무덤/벽돌살구.png', 12, 12)
    move_block52 = gameimage.stop_block('./image/무덤/벽돌살구.png', 14, 12)
    move_block53 = gameimage.stop_block('./image/무덤/벽돌황토.png', 15, 12)
    move_block54 = gameimage.stop_block('./image/무덤/벽돌황토.png', 1, 13)
    move_block55 = gameimage.stop_block('./image/무덤/벽돌살구.png', 2, 13)
    move_block56 = gameimage.stop_block('./image/무덤/벽돌황토.png', 3, 13)
    move_block57 = gameimage.stop_block('./image/무덤/벽돌살구.png', 4, 13)
    move_block58 = gameimage.stop_block('./image/무덤/벽돌황토.png', 5, 13)
    move_block59 = gameimage.stop_block('./image/무덤/벽돌살구.png', 11, 13)
    move_block60 = gameimage.stop_block('./image/무덤/벽돌황토.png', 12, 13)
    move_block61 = gameimage.stop_block('./image/무덤/벽돌살구.png', 13, 13)
    move_block62 = gameimage.stop_block('./image/무덤/벽돌황토.png', 14, 13)
    move_block63 = gameimage.stop_block('./image/무덤/벽돌살구.png', 15, 13)
    #----------------------------
    move_block_Sprite = sprite.OrderedUpdates(move_block1,move_block2,move_block3,move_block4,move_block5,move_block6,move_block7,move_block8,
                                              move_block9,move_block10,move_block11,move_block12,move_block13,move_block14,move_block15,move_block16,
                                              move_block17,move_block18,move_block19,move_block20,move_block21,move_block22,move_block23,move_block24,
                                              move_block25,move_block26,move_block27,move_block28,move_block29,move_block30,move_block31,move_block32,
                                              move_block33,move_block34,move_block35,move_block36,move_block37,move_block38,move_block39,move_block40,
                                              move_block41,move_block42,move_block43,move_block44,move_block45,move_block46,move_block47,move_block48,
                                              move_block49,move_block50,move_block51,move_block52,move_block53,move_block54,move_block55,move_block56,
                                              move_block57,move_block58,move_block59,move_block60,move_block61,move_block62,move_block63)
    ball_left_1p = 0
    ball_top_1p = 0
    ball_left_2p = 0
    ball_top_2p = 0
    speed_1p = 2.5
    speed_2p = 2.5
    #모든이미지불러오기----------
    allSprites = pygame.sprite.OrderedUpdates(p1,p2,boss,testballa,testballb,quit_game, cursor)
    ballaSprites = pygame.sprite.OrderedUpdates(testballa_left,testballa_right,testballa_down,testballa_up)
    ballbSprites = pygame.sprite.OrderedUpdates(testballb_up, testballb_right, testballb_left, testballb_down)
    #충돌함수하기위해 그룹으로 만드는거임
    p1_collide = pygame.sprite.Group()
    p1_collide.add(p1)
    p2_collide = pygame.sprite.Group()
    p2_collide.add(p2)

    win = 0
    lose = 0
    game_end = 0
    end_count = 0
    boss_die = 0
    running = True
    while running:
        for event in pygame.event.get():
            # 게임종료-----------------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_game.rect.collidepoint(pygame.mouse.get_pos()):
                    lobby.play(screen,sound, cursor)
            if event.type == pygame.QUIT:  # 종료시 입력시
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                #1p움직임
                if keyName == 'a' :
                    p1.moving(0-(speed_1p),0)
                if keyName == 'd':
                    p1.moving(speed_1p,0)
                if keyName == 'w':
                    p1.moving(0,0-speed_1p)
                if keyName == 's':
                    p1.moving(0,speed_1p)
                # 1p 아이템------------------------
                if keyName == '3':
                    p1.pin()
                if keyName == '1':
                    speed_1p += 1
                # 1p 물풍선-------------------------
                if keyboard.is_pressed("shift"):
                    for i in range(1, 16):
                        if 20 + 40 * (i - 1) < p1.rect.centerx < 20 + 40 * i: ball_left_1p = 20 + 40 * (i - 1)
                    for i in range(1, 14):
                        if 40 + 40 * (i - 1) < p1.rect.centery + 30 < 40 + 40 * i: ball_top_1p = 40 + 40 * (i - 1)
                    testballa.put(ball_left_1p, ball_top_1p)
                    testballa_left.put()
                    testballa_right.put()
                    testballa_up.put()
                    testballa_down.put()

                #2p움직임
                if keyName == 'left' :
                    p2.moving(0-speed_2p,0)
                if keyName == 'right':
                    p2.moving(speed_2p,0)
                if keyName == 'up':
                    p2.moving(0,0-speed_2p)
                if keyName == 'down':
                    p2.moving(0,speed_1p)
                # 2p 아이템---------------------------------
                if keyName == 'l':
                    p2.pin()
                if keyName == 'j':
                    speed_2p += 1

                #2p물풍선------------------------------------
                if keyboard.is_pressed("space"):
                    for i in range(1, 16):
                        if 20 + 40 * (i - 1) < p2.rect.centerx < 20 + 40 * i: ball_left_2p = 20 + 40 * (i - 1)
                    for i in range(1, 14):
                        if 40 + 40 * (i - 1) < p2.rect.centery + 30 < 40 + 40 * i: ball_top_2p = 40 + 40 * (i - 1)
                    testballb.put(ball_left_2p, ball_top_2p)
                    testballb_left.put()
                    testballb_right.put()
                    testballb_up.put()
                    testballb_down.put()
                if (event.key == pygame.K_ESCAPE):  # ESE 누르면 종료
                    running = False
                    pygame.quit()
            if event.type == pygame.KEYUP:
                keyName = pygame.key.name(event.key)
                #1p 멈춤
                if keyName == 'a':
                    p1.moving(0,0)
                if keyName == 'd':
                    p1.moving(0,0)
                if keyName == 'w':
                    p1.moving(0,0)
                if keyName == 's':
                    p1.moving(0,0)
                #2p 멈춤
                if keyName == 'left':
                    p2.moving(0,0)
                if keyName == 'right':
                    p2.moving(0,0)
                if keyName == 'up':
                    p2.moving(0,0)
                if keyName == 'down':
                    p2.moving(0,0)

            # 창크기전환----------------
            if keyboard.is_pressed('F12'):  # 화면 키우기
                screen = pygame.display.set_mode((800, 600),
                                                 pygame.FULLSCREEN | HWSURFACE | DOUBLEBUF)  # 해상도 480*320, 전체화면모드, 하드웨어 가속사용, 더블버퍼모드
            if keyboard.is_pressed('F11'):  # 윈도우 모드
                screen = pygame.display.set_mode((800, 600), DOUBLEBUF)  # 해상도 480*320, 윈도우모드, 더블버퍼모드

        # 1p 물풍선에 닿아서 물에 갇히는거랑 그때 2p랑 닿으면 죽는거-------------
        if pygame.sprite.spritecollide(p1, group, False):
            p1.in_waterball()
        in_water_1p = p1.in_water()
        if in_water_1p == True :
            if pygame.sprite.collide_rect_ratio(0.75)(p1, p2):
                p1.pin()
        # 2p 물풍선에 닿아서 물에 갇히는거랑 그때 1p랑 닿으면 죽는거
        if pygame.sprite.spritecollide(p2, group, False):
            p2.in_waterball()
        in_water_2p = p2.in_water()
        if in_water_2p == True :
            if pygame.sprite.collide_rect_ratio(0.75)(p2, p1):
                p2.pin()
        if pygame.sprite.collide_rect_ratio(0.5)(p1, boss):
            p1.die()
            lose = 1
        if pygame.sprite.collide_rect_ratio(0.5)(p2, boss):
            p2.die()
            lose = 1

        if pygame.sprite.spritecollide(boss, group, False):
            boss_die += 1
        if boss_die > 40:
            boss.die()
            win = 1


        if p1.rect.left < 10: p1.rect.left = 10
        if p2.rect.left < 10: p2.rect.left = 10
        if p1.rect.right > 630: p1.rect.right = 630
        if p2.rect.right > 630: p2.rect.right = 630
        if p1.rect.bottom < 80: p1.rect.bottom = 80
        if p2.rect.bottom < 80: p2.rect.bottom = 80
        if p1.rect.bottom > 560: p1.rect.bottom = 560
        if p2.rect.bottom > 560: p2.rect.bottom = 560

        #게임 승리----------------------------------
        if win == 1:
            win_y = 200
            game_end = 1

        if lose == 1:
            lose_y = 200
            game_end = 1


        screen.blit(boss_ground, (30, 30))
        screen.blit(main_background, (0, 0))
        screen.blit(boss_ground, (20, 40))
        move_block_Sprite.draw(screen)
        stop_block_Sprites.draw(screen)
        allSprites.draw(screen)
        ballaSprites.draw(screen)
        ballbSprites.draw(screen)
        allSprites.update()
        ballaSprites.update(ball_left_1p, ball_top_1p)
        ballbSprites.update(ball_left_2p, ball_top_2p)
        screen.blit(win_image, (200, win_y))
        screen.blit(lose_image, (200, lose_y))


        if game_end == 1:
                end_count+=1
                if end_count == 100:
                    p1level = player1_level.updateFile(1)  # 1
                    p2level = player2_level.updateFile(1)
                    end = room.ROOM(screen, sound, cursor, state, back_button, quit_button)
                    end.monster_game_room()


        pygame.display.update()
    pygame.quit()