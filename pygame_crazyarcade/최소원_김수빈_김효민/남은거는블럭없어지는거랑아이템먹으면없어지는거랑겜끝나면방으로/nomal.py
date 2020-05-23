import pygame, keyboard
from pygame import *
from pygame.locals import *
import village_map, desert_map, music, gameimage, lobby, charactor,level,room

def village_play(screen, sound, cursor, charac, state, back_button, quit_button):
    pygame.init()

    player1_level = level.Level()
    player2_level = level.Level2()
    #bgm------------------------
    bgm = music.MUSIC('./music/빌리지.mp3')
    bgm.musicplay(sound)
    #배경------------------------
    main_background = pygame.image.load('./image/background/game_map.png')
    billage_ground = pygame.image.load('./image/background/bg_village.png')
    billage_ground = pygame.transform.scale(billage_ground, (600, 520))
    win1_image = pygame.image.load('1p_win.png').convert_alpha()
    win2_image = pygame.image.load('2p_win.png').convert_alpha()
    win_y = 1000
    win2_y = 1000

    #플레이어 데려오기
    if charac == 1:
        p1= charactor.BAZZY(screen)
        p2= charactor.RODU(screen)
    else :
        p1= charactor.RODU(screen)
        p2= charactor.BAZZY(screen)
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
    #못움직이는블록----------------
    stop_block_Sprites = village_map.stop_block() #안움직이는 맵
    # nonstop_block_Sprites = village_map.nonstop_block()

    block1 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 2, 1)
    block2 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 4, 1)
    block5 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 2, 5)
    block6 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 4, 5)
    block7 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 1, 6)
    block8 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 3, 6)
    block9 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 5, 6)
    block12 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 1, 10)
    block13 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 3, 10)
    block14 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 5, 10)
    box1 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 3, 2)
    box2 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 5, 2)
    box3 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 1, 4)
    box4 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 3, 4)
    box5 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 5, 4)
    box6 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 2, 9)
    box7 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 4, 9)
    box8 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 2, 11)
    box9 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 4, 11)
    rblock3 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 4, 3)
    rblock7 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 1, 8)
    rblock8 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 3, 8)
    rblock9 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 5, 8)
    rblock12 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 3, 12)
    rblock13 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 5, 12)
    rblock14 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 4, 13)
    g1 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 2, 7)
    g2 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 4, 7)
    g3 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 7)
    g4 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 1)
    g5 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 3)
    g6 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 5)
    g7 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 9)
    g8 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 11)
    g9 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 6, 13)
    g10 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 1)
    g11 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 3)
    g12 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 5)
    g13 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 7)
    g14 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 9)
    g15 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 11)
    g16 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 10, 13)
    g17 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 12, 7)
    g18 = gameimage.nonstop_block('./image/빌리지/풀 (1).png', 14, 7)
    tblock1 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 12, 1)
    tblock2 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png',11, 2)
    tblock3 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 13, 2)
    tblock6 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 11, 6)
    tblock7 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 13, 6)
    tblock8 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 15, 6)
    tblock9 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 11, 8)
    tblock10 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 13, 8)
    tblock11 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 15, 8)
    tblock12 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 12, 9)
    tblock13 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 14, 9)
    tblock16 = gameimage.nonstop_block('./image/빌리지/빨간블럭 (1).png', 12, 13)
    qblock2 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 11, 4)
    qblock3 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 13, 4)
    qblock4 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 15, 4)
    qblock10 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 12,11)
    qblock11 = gameimage.nonstop_block('./image/빌리지/노란블럭 (1).png', 14, 11)
    qbox1 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 12, 3)
    qbox2 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 14, 3)
    qbox3 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 12, 5)
    qbox4 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 14, 5)
    qbox5 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 11, 10)
    qbox6 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 13, 10)
    qbox7 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 15, 10)
    qbox8 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 11, 12)
    qbox9 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 13, 12)

    sbox1 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 7, 2)
    sbox2 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 7, 4)
    sbox4 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 7, 8)
    sbox5 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 7, 10)
    sbox6 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 7, 12)
    sbox7 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 8, 3)
    sbox8 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 8, 6)
    sbox9 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 8, 9)
    sbox11 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 9, 1)
    sbox13 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 9, 5)
    sbox14 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 9, 7)
    sbox16 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 9, 11)
    sbox17 = gameimage.nonstop_block('./image/빌리지/박스 (1).jpg', 9, 13)


    nonstop_block_Sprites = pygame.sprite.OrderedUpdates(
        g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12,g13,g14,g15,g16,
        block1,block2,box1,box2,
        rblock3,box3,box4,box5,block5,block6,
        block7,block8,block9,rblock8,rblock9,rblock7,
        box6,box7,block12,block13,block14,box8,box9,
        rblock12,rblock13,rblock14,
        tblock1,tblock2,qbox1,qbox2,qblock2,qblock3,qblock4,tblock3,qbox3,qbox4,
        g17,g18,tblock6,tblock7,tblock8,tblock9,tblock10,tblock11,qbox5,qbox6,qbox7,
        tblock12,tblock13,qblock10,qblock11,tblock16,qbox8,qbox9,
        sbox1,sbox2,sbox4,sbox5,sbox6,sbox7,sbox8,sbox9,sbox11,sbox13,sbox14,sbox16,sbox17)

    item_Sprites = village_map.item()
    # 노란블록사라지는이미지-------
    yblock1 = pygame.image.load("./image/빌리지/노란블럭 (2).png").convert_alpha()
    yblock2 = pygame.image.load("./image/빌리지/노란블럭 (3).png").convert_alpha()
    yblock3 = pygame.image.load("./image/빌리지/노란블럭 (4).png").convert_alpha()
    yblock4 = pygame.image.load("./image/빌리지/노란블럭 (5).png").convert_alpha()
    yblock5 = pygame.image.load("./image/빌리지/노란블럭 (6).png").convert_alpha()
    yblock6 = pygame.image.load("./image/빌리지/노란블럭 (7).png").convert_alpha()
    yblock7 = pygame.image.load("./image/빌리지/노란블럭 (8).png").convert_alpha()
    yblock8 = pygame.image.load("./image/moo.png").convert_alpha()
    # 노란블록리스트--------------
    remove_block1 = [yblock1, yblock2, yblock3, yblock4, yblock5, yblock6, yblock7, yblock8]
    # 빨간블록사라지는이미지-------
    rblock1 = pygame.image.load("./image/빌리지/빨간블럭 (2).png").convert_alpha()
    rblock2 = pygame.image.load("./image/빌리지/빨간블럭 (3).png").convert_alpha()
    rblock3 = pygame.image.load("./image/빌리지/빨간블럭 (4).png").convert_alpha()
    rblock4 = pygame.image.load("./image/빌리지/빨간블럭 (5).png").convert_alpha()
    rblock5 = pygame.image.load("./image/빌리지/빨간블럭 (6).png").convert_alpha()
    rblock6 = pygame.image.load("./image/빌리지/빨간블럭 (7).png").convert_alpha()
    rblock7 = pygame.image.load("./image/빌리지/빨간블럭 (8).png").convert_alpha()
    rblock8 = pygame.image.load("./image/moo.png").convert_alpha()
    #빨간블록리스트--------------
    remove_block2 = [rblock1, rblock2, rblock3, rblock4, rblock5, rblock6, rblock7, rblock8]
    #박스블록사라지는이미지-------
    bblock1 = pygame.image.load("./image/빌리지/박스사라짐 (1).png").convert_alpha()
    bblock2 = pygame.image.load("./image/빌리지/박스사라짐 (2).png").convert_alpha()
    bblock3 = pygame.image.load("./image/빌리지/박스사라짐 (3).png").convert_alpha()
    bblock4 = pygame.image.load("./image/빌리지/박스사라짐 (4).png").convert_alpha()
    bblock5 = pygame.image.load("./image/빌리지/박스사라짐 (5).png").convert_alpha()
    bblock6 = pygame.image.load("./image/빌리지/박스사라짐 (6).png").convert_alpha()
    bblock7 = pygame.image.load("./image/빌리지/박스사라짐 (7).png").convert_alpha()
    bblock8 = pygame.image.load("./image/moo.png").convert_alpha()
    #박스블록리스트--------------
    remove_block3 = [bblock1, bblock2, bblock3, bblock4, bblock5, bblock6, bblock7, bblock8]

    ball_left_1p = 0
    ball_top_1p = 0
    ball_left_2p = 0
    ball_top_2p = 0
    speed_1p = 2.5
    speed_2p = 2.5
    #이미지불러오기------------------
    allSprites = pygame.sprite.OrderedUpdates(p1,p2,testballa,testballb,quit_game, cursor)
    ballaSprites = pygame.sprite.OrderedUpdates(testballa_left,testballa_right,testballa_down,testballa_up)
    ballbSprites = pygame.sprite.OrderedUpdates(testballb_up, testballb_right, testballb_left, testballb_down)
    #충돌함수하기위해 그룹으로 만드는거임
    p1_collide = pygame.sprite.Group()
    p1_collide.add(p1)
    p2_collide = pygame.sprite.Group()
    p2_collide.add(p2)

    win = 0
    game_end = 0
    end_count = 0
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
                    p1.moving(0 - (speed_1p), 0)
                if keyName == 'd':
                    p1.moving(speed_1p, 0)
                if keyName == 'w':
                    p1.moving(0, 0 - speed_1p)
                if keyName == 's':
                    p1.moving(0, speed_1p)
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
                    p2.moving(0 - speed_2p, 0)
                if keyName == 'right':
                    p2.moving(speed_2p, 0)
                if keyName == 'up':
                    p2.moving(0, 0 - speed_2p)
                if keyName == 'down':
                    p2.moving(0, speed_1p)
                    # 2p 아이템---------------------------------
                if keyName == 'l':
                    p2.pin()
                if keyName == 'j':
                    speed_2p += 1

                    # 2p물풍선------------------------------------
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
                p1.die()
                win = 2
        # 2p 물풍선에 닿아서 물에 갇히는거랑 그때 1p랑 닿으면 죽는거
        if pygame.sprite.spritecollide(p2, group, False):
            p2.in_waterball()
        in_water_2p = p2.in_water()
        if in_water_2p == True :
            if pygame.sprite.collide_rect_ratio(0.75)(p2, p1):
                p2.die()
                win = 1

        if pygame.sprite.spritecollide(block1, group, False):
            block1.bump()

        #맵밖으로 못벗어나게 하는거
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
        elif win == 2:
            win2_y = 200
            game_end = 1

        screen.blit(main_background, (0, 0))
        screen.blit(billage_ground, (20, 40))
        item_Sprites.draw(screen)
        nonstop_block_Sprites.draw(screen)
        stop_block_Sprites.draw(screen)
        allSprites.draw(screen)
        ballaSprites.draw(screen)
        ballbSprites.draw(screen)
        allSprites.update()
        ballaSprites.update(ball_left_1p, ball_top_1p)
        ballbSprites.update(ball_left_2p, ball_top_2p)
        screen.blit(win1_image, (200, win_y))
        screen.blit(win2_image, (200, win2_y))

        if game_end == 1:
                end_count+=1
                if end_count == 100:
                    if win == 1:
                        p1level = player1_level.updateFile(1)  # 1
                    if win == 2:
                        p1leve2 = player1_level.updateFile(1)  # 1
                    end = room.ROOM(screen, sound, cursor, state, back_button, quit_button)
                    end.monster_game_room()

        pygame.display.update()

def desert_play(screen, sound, cursor, charac, state, back_button, quit_button):
    pygame.init()

    player1_level = level.Level()
    player2_level = level.Level2()
    # bgm------------------------
    bgm = music.MUSIC('./music/사막.mp3')
    bgm.musicplay(sound)
    # 배경------------------------
    main_background = pygame.image.load('./image/background/game_map.png')
    boss_ground = pygame.image.load('./image/background/bg_desert.png')
    boss_ground = pygame.transform.scale(boss_ground, (600, 520))
    win1_image = pygame.image.load('1p_win.png').convert_alpha()
    win2_image = pygame.image.load('2p_win.png').convert_alpha()
    win_y = 1000
    win2_y = 1000

    #플레이어 데려오기
    if charac == 1:
        p1= charactor.BAZZY(screen)
        p2= charactor.RODU(screen)
    else :
        p1= charactor.RODU(screen)
        p2= charactor.BAZZY(screen)
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

    #플레이어 데려오기
    if charac == 1:
        p1= charactor.BAZZY(screen)
        p2= charactor.RODU(screen)
    else :
        p1= charactor.RODU(screen)
        p2= charactor.BAZZY(screen)
    # 버튼-------------------------
    quit_game = gameimage.BUTTON('./image/moo.png', (720, 580), True, (140, 30))
    #안움직임----------------------
    # stop_block_Sprites = desert_map.stop_block()  # 안움직이는 맵
    uncrushed_block1 = gameimage.stop_block('./image/사막/보급 (2).png', 2, 2)
    uncrushed_block2 = gameimage.stop_block('./image/사막/보급 (2).png', 10, 2)
    uncrushed_block3 = gameimage.stop_block('./image/사막/보급 (2).png', 6, 4)
    uncrushed_block4 = gameimage.stop_block('./image/사막/보급 (2).png', 2, 8)
    uncrushed_block5 = gameimage.stop_block('./image/사막/보급 (2).png', 10, 12)
    uncrushed_block6 = gameimage.stop_block('./image/사막/돌.png', 6, 2)
    uncrushed_block7 = gameimage.stop_block('./image/사막/돌.png', 8, 2)
    uncrushed_block8 = gameimage.stop_block('./image/사막/돌.png', 14, 2)
    uncrushed_block9 = gameimage.stop_block('./image/사막/돌.png', 2, 4)
    uncrushed_block10 = gameimage.stop_block('./image/사막/돌.png', 10, 4)
    uncrushed_block11 = gameimage.stop_block('./image/사막/돌.png', 14, 4)
    uncrushed_block12 = gameimage.stop_block('./image/사막/돌.png', 6, 6)
    uncrushed_block13 = gameimage.stop_block('./image/사막/돌.png', 6, 10)
    uncrushed_block14 = gameimage.stop_block('./image/사막/돌.png', 10, 10)
    uncrushed_block15 = gameimage.stop_block('./image/사막/돌.png', 6, 12)
    uncrushed_block16 = gameimage.stop_block('./image/사막/돌.png', 12, 12)
    uncrushed_block17 = gameimage.stop_block('./image/사막/보급 (1).png', 4, 4)
    uncrushed_block18 = gameimage.stop_block('./image/사막/보급 (1).png', 14, 8)
    uncrushed_block19 = gameimage.stop_block('./image/사막/보급 (1).png', 2, 12)
    uncrushed_block20 = gameimage.stop_block('./image/사막/보급 (1).png', 4, 12)
    uncrushed_block21 = gameimage.stop_block('./image/사막/선인장 (1).png', 8, 4)
    uncrushed_block22 = gameimage.stop_block('./image/사막/선인장 (1).png', 6, 8)
    uncrushed_block23 = gameimage.stop_block('./image/사막/선인장 (1).png', 12, 8)
    uncrushed_block24 = gameimage.stop_block('./image/사막/선인장 (2).png', 12, 4)
    uncrushed_block25 = gameimage.stop_block('./image/사막/선인장 (2).png', 4, 6)
    uncrushed_block26 = gameimage.stop_block('./image/사막/선인장 (2).png', 4, 10)
    uncrushed_block27 = gameimage.stop_block('./image/사막/선인장 (2).png', 8, 10)
    uncrushed_block28 = gameimage.stop_block('./image/사막/선인장 (2).png', 12, 10)
    uncrushed_block29 = gameimage.stop_block('./image/사막/텐트노란.png', 4, 2)
    uncrushed_block30 = gameimage.stop_block('./image/사막/텐트노란.png', 14, 10)
    uncrushed_block31 = gameimage.stop_block('./image/사막/텐트노란.png', 8, 12)
    uncrushed_block32 = gameimage.stop_block('./image/사막/텐트빨강.png', 12, 2)
    uncrushed_block33 = gameimage.stop_block('./image/사막/텐트빨강.png', 2, 6)
    uncrushed_block34 = gameimage.stop_block('./image/사막/텐트빨강.png', 10, 6)
    uncrushed_block35 = gameimage.stop_block('./image/사막/텐트빨강.png', 14, 12)
    uncrushed_block36 = gameimage.stop_block('./image/사막/텐트파란.png', 12, 6)
    uncrushed_block37 = gameimage.stop_block('./image/사막/텐트파란.png', 4, 8)
    uncrushed_block38 = gameimage.stop_block('./image/사막/텐트파란.png', 2, 10)
    uncrushed_block39 = gameimage.stop_block('./image/사막/오아시스 (1).png', 8.5, 8)

    stop_block_Sprites = pygame.sprite.OrderedUpdates(uncrushed_block1, uncrushed_block2, uncrushed_block3,
                                                      uncrushed_block4, uncrushed_block5, uncrushed_block6,
                                                      uncrushed_block7, uncrushed_block8, uncrushed_block9,
                                                      uncrushed_block10, uncrushed_block11, uncrushed_block12,
                                                      uncrushed_block13, uncrushed_block14, uncrushed_block15,
                                                      uncrushed_block16, uncrushed_block17, uncrushed_block18,
                                                      uncrushed_block19, uncrushed_block20, uncrushed_block21,
                                                      uncrushed_block22, uncrushed_block23, uncrushed_block24,
                                                      uncrushed_block25, uncrushed_block26, uncrushed_block27,
                                                      uncrushed_block28, uncrushed_block29, uncrushed_block30,
                                                      uncrushed_block31, uncrushed_block32, uncrushed_block33,
                                                      uncrushed_block34, uncrushed_block35, uncrushed_block36,
                                                      uncrushed_block37, uncrushed_block38, uncrushed_block39)

    uncrushed_block = pygame.sprite.Group()
    uncrushed_block.add(uncrushed_block1, uncrushed_block2, uncrushed_block3,
                          uncrushed_block4, uncrushed_block5, uncrushed_block6,
                          uncrushed_block7, uncrushed_block8, uncrushed_block9,
                          uncrushed_block10, uncrushed_block11, uncrushed_block12,
                          uncrushed_block13, uncrushed_block14, uncrushed_block15,
                          uncrushed_block16, uncrushed_block17, uncrushed_block18,
                          uncrushed_block19, uncrushed_block20, uncrushed_block21,
                          uncrushed_block22, uncrushed_block23, uncrushed_block24,
                          uncrushed_block25, uncrushed_block26, uncrushed_block27,
                          uncrushed_block28, uncrushed_block29, uncrushed_block30,
                          uncrushed_block31, uncrushed_block32, uncrushed_block33,
                          uncrushed_block34, uncrushed_block35, uncrushed_block36,
                          uncrushed_block37, uncrushed_block38, uncrushed_block39)
    #블록사라지는이미지------------
    block1 = pygame.image.load("./image/사막/벽돌사라짐 (1).png").convert_alpha()
    block2 = pygame.image.load("./image/사막/벽돌사라짐 (2).png").convert_alpha()
    block3 = pygame.image.load("./image/사막/벽돌사라짐 (3).png").convert_alpha()
    block4 = pygame.image.load("./image/사막/벽돌사라짐 (4).png").convert_alpha()
    block5 = pygame.image.load("./image/사막/벽돌사라짐 (5).png").convert_alpha()
    block6 = pygame.image.load("./image/사막/벽돌사라짐 (6).png").convert_alpha()
    block7 = pygame.image.load("./image/사막/벽돌사라짐 (7).png").convert_alpha()
    block8 = pygame.image.load("./image/moo.png").convert_alpha()
    #블록리스트---------------------
    remove_block = [block1, block2, block3, block4, block5, block6, block7, block8]

    ball_left_1p = 0
    ball_top_1p = 0
    ball_left_2p = 0
    ball_top_2p = 0
    speed_1p = 2.5
    speed_2p = 2.5

    #이미지불러오기----------------
    allSprites = pygame.sprite.OrderedUpdates(p1,p2,testballa,testballb,quit_game, cursor)
    ballaSprites = pygame.sprite.OrderedUpdates(testballa_left,testballa_right,testballa_down,testballa_up)
    ballbSprites = pygame.sprite.OrderedUpdates(testballb_up, testballb_right, testballb_left, testballb_down)
    #충돌함수하기위해 그룹으로 만드는거임
    p1_collide = pygame.sprite.Group()
    p1_collide.add(p1)
    p2_collide = pygame.sprite.Group()
    p2_collide.add(p2)

    win = 0
    game_end = 0
    end_count = 0

    running = True
    while running:
        for event in pygame.event.get():
            # 게임종료-----------------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_game.rect.collidepoint(pygame.mouse.get_pos()):
                    lobby.play(screen, sound, cursor)
            if event.type == pygame.QUIT:  # 종료시 입력시
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                #1p움직임
                if keyName == 'a' :
                    p1.moving(0 - (speed_1p), 0)
                if keyName == 'd':
                    p1.moving(speed_1p, 0)
                if keyName == 'w':
                    p1.moving(0, 0 - speed_1p)
                if keyName == 's':
                    p1.moving(0, speed_1p)
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
                    p2.moving(0 - speed_2p, 0)
                if keyName == 'right':
                    p2.moving(speed_2p, 0)
                if keyName == 'up':
                    p2.moving(0, 0 - speed_2p)
                if keyName == 'down':
                    p2.moving(0, speed_1p)
                    # 2p 아이템---------------------------------
                if keyName == 'l':
                    p2.pin()
                if keyName == 'j':
                    speed_2p += 1

                    # 2p물풍선------------------------------------
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
                p1.die()
                win = 2
        # 2p 물풍선에 닿아서 물에 갇히는거랑 그때 1p랑 닿으면 죽는거
        if pygame.sprite.spritecollide(p2, group, False):
            p2.in_waterball()
        in_water_2p = p2.in_water()
        if in_water_2p == True :
            if pygame.sprite.collide_rect_ratio(0.75)(p2, p1):
                p2.die()
                win = 1

        #플레이어 맵밖에 못벗어나게 하는거
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
        elif win == 2:
            win2_y = 200
            game_end = 1

        screen.blit(main_background, (0, 0))
        screen.blit(boss_ground, (20, 40))
        stop_block_Sprites.draw(screen)
        allSprites.draw(screen)
        ballaSprites.draw(screen)
        ballbSprites.draw(screen)
        allSprites.update()
        ballaSprites.update(ball_left_1p, ball_top_1p)
        ballbSprites.update(ball_left_2p, ball_top_2p)
        screen.blit(win1_image, (200, win_y))
        screen.blit(win2_image, (200, win2_y))

        if game_end == 1:
                end_count+=1
                if end_count == 100:
                    if win == 1:
                        p1level = player1_level.updateFile(1)  # 1
                    if win == 2:
                        p1leve2 = player1_level.updateFile(1)  # 1
                    end = room.ROOM(screen, sound, cursor, state, back_button, quit_button)
                    end.monster_game_room()

        pygame.display.update()