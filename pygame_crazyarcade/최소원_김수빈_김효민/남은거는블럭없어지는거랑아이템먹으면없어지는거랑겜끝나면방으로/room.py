import pygame, keyboard
from pygame import *
from pygame.locals import *
import gameimage, music,lobby, nomal, monster, level

class ROOM:
    def __init__(self, screen, sound, cursor, state, back_button, quit_button):
        self.screen = screen
        self.cursor = cursor
        self.sound =sound
        self.back_button = back_button
        self.quit_button = quit_button
        self.state = state
        self.player1_level = level.Level()
        self.player2_level = level.Level2()
        self.player1_metal = pygame.image.load('./image/1.png').convert_alpha()
        self.player1_metal = pygame.transform.scale(self.player1_metal, (22,22))
        self.player2_metal = pygame.image.load('./image/1.png').convert_alpha()
        self.player2_metal = pygame.transform.scale(self.player2_metal, (22,22))
        p1level = self.player1_level.updateFile(0)  # 1
        p2level = self.player2_level.updateFile(0)
        if p1level == 2:
            self.player1_metal = pygame.image.load('./image/2.png').convert_alpha()
            self.player1_metal = pygame.transform.scale(self.player1_metal, (22, 22))
        if p2level == 2:
            self.player2_metal = pygame.image.load('./image/2.png').convert_alpha()
            self.player2_metal = pygame.transform.scale(self.player2_metal, (22,22))
        if p1level == 3:
            self.player1_metal = pygame.image.load('./image/3.png').convert_alpha()
            self.player1_metal = pygame.transform.scale(self.player1_metal, (22, 22))
        if p2level == 3:
            self.player2_metal = pygame.image.load('./image/3.png').convert_alpha()
            self.player2_metal = pygame.transform.scale(self.player2_metal, (22, 22))
        if p1level == 4:
            self.player1_metal = pygame.image.load('./image/4.png').convert_alpha()
            self.player1_metal = pygame.transform.scale(self.player1_metal, (22, 22))
        if p2level == 4:
            self.player2_metal = pygame.image.load('./image/4.png').convert_alpha()
            self.player2_metal = pygame.transform.scale(self.player2_metal, (22, 22))

        # bgm------------------------
        bgm = music.MUSIC('./music/room.mp3')
        bgm.musicplay(self.sound)
        if self.state == "nomal": self.nomal_game_room()
        elif self.state == "monster": self.monster_game_room()

    def nomal_game_room(self):
        #배경------------------------
        normal_game_room_background = pygame.image.load('./image/background/room_nomal.png').convert()
        village = pygame.image.load('./image/background/select_village.png').convert()
        desert = pygame.image.load('./image/background/select_desert.png').convert()
        one_p_bazzy = pygame.image.load('./image/moo.png').convert_alpha()
        two_p_bazzy = pygame.image.load('./image/background/2p가 배찌.png').convert()
        two_p_bazzy_1 = pygame.image.load('./image/background/2p가 배찌_1.png').convert()

        map = village
        charac = one_p_bazzy
        charac_number = 1

        #캐릭터 선택 버튼---------------
        charac_select_button = gameimage.BUTTON('./image/moo.png', (720, 155), True, (130, 45))
        #맵 선택 버튼----------------
        map_select_left = gameimage.BUTTON('./image/background/select_left.png', (660, 453), True, (35, 35))
        map_select_right = gameimage.BUTTON('./image/background/select_right.png', (754, 453), True, (35, 35))
        #게임 입장 버튼----------------
        game_start_button = gameimage.BUTTON('./image/moo.png', (610, 520), True, (200, 60))
        #이미지불러오기--------------
        allSprites = pygame.sprite.OrderedUpdates(map_select_left, map_select_right, game_start_button, charac_select_button, self.back_button, self.quit_button, self.cursor)
        mapSprites =  pygame.sprite.OrderedUpdates(map_select_left, map_select_right, self.cursor)
        running = True
        while running:
            for event in pygame.event.get():
                #마우스클릭--------------------
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # 로비이동------------------
                    if self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        lobby.play(self.screen, self.sound, self.cursor)
                    #왼쪽화살표------------------
                    if map_select_left.rect.collidepoint(pygame.mouse.get_pos()):
                        if map == village: map = desert
                        else: map = village
                    #오른쪽화살표-----------------
                    if map_select_right.rect.collidepoint(pygame.mouse.get_pos()):
                        if map == village: map = desert
                        else: map = village
                    #캐릭터바꾸기----------------
                    if charac_select_button.rect.collidepoint(pygame.mouse.get_pos()):
                        if charac == one_p_bazzy : charac =two_p_bazzy; charac_number = 2
                        else: charac = one_p_bazzy; charac_number = 1
                    #게임시작--------------------
                    if game_start_button.rect.collidepoint(pygame.mouse.get_pos()):
                        if map == village: nomal.village_play(self.screen, self.sound, self.cursor, charac_number, self.state, self.back_button, self.quit_button)
                        else: nomal.desert_play(self.screen, self.sound, self.cursor, charac_number, self.state, self.back_button, self.quit_button)
                # 게임종료------------------------
                    if self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                        running = False
                if event.type == pygame.QUIT:  # 종료시 입력시
                    running = False
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE):  # ESE 누르면 종료
                        running = False
                # 창크기전환----------------------
                if keyboard.is_pressed('F12'):  # 화면 키우기
                    self.screen = pygame.display.set_mode((800, 600),
                                                     pygame.FULLSCREEN | HWSURFACE | DOUBLEBUF)  # 해상도 480*320, 전체화면모드, 하드웨어 가속사용, 더블버퍼모드
                if keyboard.is_pressed('F11'):  # 윈도우 모드
                    self.screen = pygame.display.set_mode((800, 600), DOUBLEBUF)  # 해상도 480*320, 윈도우모드, 더블버퍼모드

            self.screen.blit(normal_game_room_background, (0, 0))
            allSprites.clear(self.screen, normal_game_room_background)
            allSprites.update()
            allSprites.draw(self.screen)
            if map == village:
                self.screen.blit(map, (477, 327))
            else : self.screen.blit(map, (477, 328))
            if charac == one_p_bazzy:
                self.screen.blit(charac, (500, 100))
            else :
                self.screen.blit(charac, (569, 35))
                self.screen.blit(two_p_bazzy_1, (24, 92))
            mapSprites.draw(self.screen)
            self.screen.blit(self.player1_metal, (97, 150))
            self.screen.blit(self.player2_metal, (202, 150))
            pygame.display.update()

        pygame.quit()

    def monster_game_room(self):
        # 배경------------------------
        monster_game_room_background = pygame.image.load('./image/background/room_monster.png')
        # 캐이미지 -----------------
        one_p_bazzy = pygame.image.load('./image/moo.png').convert_alpha()
        two_p_bazzy = pygame.image.load('./image/background/2p가 배찌.png').convert()
        two_p_bazzy_1 = pygame.image.load('./image/background/2p가 배찌_1.png').convert()

        charac = one_p_bazzy
        charac_number = 1

        #캐릭터 선택 버튼---------------
        charac_select_button = gameimage.BUTTON('./image/moo.png', (720, 155), True, (130, 45))

        # 게임 입장 버튼----------------
        game_start_button = gameimage.BUTTON('./image/moo.png', (610, 520), True, (200, 60))
        # 이미지불러오기--------------
        allSprites = pygame.sprite.OrderedUpdates(game_start_button,charac_select_button, self.back_button, self.quit_button, self.cursor)
        running = True
        while running:
            for event in pygame.event.get():
                # 마우스클릭--------------------
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # 로비이동------------------
                    if self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        lobby.play(self.screen, self.sound, self.cursor)
                    #캐릭터바꾸기----------------
                    if charac_select_button.rect.collidepoint(pygame.mouse.get_pos()):
                        if charac == one_p_bazzy : charac =two_p_bazzy; charac_number = 2
                        else: charac = one_p_bazzy; charac_number = 1
                    #게임시작--------------------
                    if game_start_button.rect.collidepoint(pygame.mouse.get_pos()):
                        monster.play(self.screen, self.sound, self.cursor, charac_number, self.state, self.back_button, self.quit_button)
                # 게임종료-------------------
                    if self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                        running = False
                if event.type == pygame.QUIT:  # 종료시 입력시
                    running = False
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE):  # ESE 누르면 종료
                        running = False
                # 창크기전환----------------------
                if keyboard.is_pressed('F12'):  # 화면 키우기
                    self.screen = pygame.display.set_mode((800, 600),
                                                          pygame.FULLSCREEN | HWSURFACE | DOUBLEBUF)  # 해상도 480*320, 전체화면모드, 하드웨어 가속사용, 더블버퍼모드
                if keyboard.is_pressed('F11'):  # 윈도우 모드
                    self.screen = pygame.display.set_mode((800, 600), DOUBLEBUF)  # 해상도 480*320, 윈도우모드, 더블버퍼모드

            self.screen.blit(monster_game_room_background, (0, 0))
            if charac == one_p_bazzy:
                self.screen.blit(charac, (500, 100))
            else :
                self.screen.blit(charac, (569, 35))
                self.screen.blit(two_p_bazzy_1, (24, 92))
            allSprites.clear(self.screen, monster_game_room_background)
            allSprites.update()
            allSprites.draw(self.screen)
            self.screen.blit(self.player1_metal, (97, 150))
            self.screen.blit(self.player2_metal, (202, 150))
            pygame.display.update()

        pygame.quit()