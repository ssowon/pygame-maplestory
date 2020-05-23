import pygame
from pygame import *

class BUTTON(pygame.sprite.Sprite):
    def __init__(self,image_position, position, transform,pixel): #경로, 화면위치, 크기변환, 픽셀
        pygame.sprite.Sprite.__init__(self)

        self.__button_image = pygame.image.load(image_position).convert_alpha()
        if transform == True:
            self.__button_image = pygame.transform.scale(self.__button_image, pixel)

        self.rect = self.__button_image.get_rect()
        self.rect.center = position
        self.image = self.__button_image

class MOUSE(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.mouse.set_visible(False)

        self.__mouse_image = pygame.image.load('./image/img/cursor.png').convert_alpha()
        self.__mouse_image = pygame.transform.scale(self.__mouse_image, (30, 35))
        self.__mouse_image.set_colorkey((0,0,0))
        self.image = self.__mouse_image
        self.rect = self.image.get_rect()
        self.rect.center = (400,300)


    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class stop_block(pygame.sprite.Sprite):
    #이미지 경로, 행, 열
    def __init__(self, image_position, row, column):
        pygame.sprite.Sprite.__init__(self)

        self.__block_image = pygame.image.load(image_position).convert_alpha()
        self.__block_Width, self.__block_Height = self.__block_image.get_rect().size
        self.rect = self.__block_image.get_rect()
        self.rect.center = (40*row,(40*column)+(40-self.__block_Height)+(self.__block_Height/2))
        self.image = self.__block_image

class nonstop_block(pygame.sprite.Sprite):
    #이미지 경로, 행, 열
    def __init__(self, image_position, row, column):
        pygame.sprite.Sprite.__init__(self)

        self.__block_image = pygame.image.load(image_position).convert_alpha()
        self.__block_Width, self.__block_Height = self.__block_image.get_rect().size
        self.rect = self.__block_image.get_rect()
        self.rect.center = (40*row,(40*column)+(40-self.__block_Height)+(self.__block_Height/2))
        self.image = self.__block_image

    def bump(self):
        self.rect.center = (1000,1000)

class item_speed(pygame.sprite.Sprite):
    def __init__(self, image_position, row, column):
        pygame.sprite.Sprite.__init__(self)

        self.__block_image = pygame.image.load(image_position).convert_alpha()
        self.__block_Width, self.__block_Height = self.__block_image.get_rect().size
        self.rect = self.__block_image.get_rect()
        self.rect.center = (40*row,(40*column)+(40-self.__block_Height)+(self.__block_Height/2))
        self.image = self.__block_image

class item_ball(pygame.sprite.Sprite):
    def __init__(self, image_position, row, column):
        pygame.sprite.Sprite.__init__(self)

        self.__block_image = pygame.image.load(image_position).convert_alpha()
        self.__block_Width, self.__block_Height = self.__block_image.get_rect().size
        self.rect = self.__block_image.get_rect()
        self.rect.center = (40*row,(40*column)+(40-self.__block_Height)+(self.__block_Height/2))
        self.image = self.__block_image

class item_mulyak(pygame.sprite.Sprite):
    def __init__(self, image_position, row, column):
        pygame.sprite.Sprite.__init__(self)

        self.__block_image = pygame.image.load(image_position).convert_alpha()
        self.__block_Width, self.__block_Height = self.__block_image.get_rect().size
        self.rect = self.__block_image.get_rect()
        self.rect.center = (40*row,(40*column)+(40-self.__block_Height)+(self.__block_Height/2))
        self.image = self.__block_image

#-------------------물풍선---------------건드리지말것------------------
class WaterBall(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.__ball_list = []
        self.ball1 = pygame.image.load("./image/water_ball/basic/waterball (1).png").convert_alpha()
        self.ball2 = pygame.image.load("./image/water_ball/basic/waterball (2).png").convert_alpha()
        self.ball3 = pygame.image.load("./image/water_ball/basic/waterball (3).png").convert_alpha()
        self.ball4 = pygame.image.load("./image/water_ball/basic/waterball (4).png").convert_alpha()
        self.ball5 = pygame.image.load("./image/water_ball/pop/pop_waterball (1).png").convert_alpha()
        self.ball6 = pygame.image.load("./image/water_ball/pop/pop_waterball (2).png").convert_alpha()
        self.ball7 = pygame.image.load("./image/water_ball/pop/pop_waterball (3).png").convert_alpha()
        self.ball8 = pygame.image.load("./image/water_ball/pop/pop_waterball (4).png").convert_alpha()

        self.__ball_list = [self.ball1, self.ball2, self.ball3, self.ball4,self.ball1, self.ball2, self.ball3, self.ball4,self.ball5,self.ball6,self.ball7,self.ball8]

        self.__ball_pop = []
        for i in range(1,5):
            self.__temp_image = pygame.image.load('./image/water_ball/pop/pop_waterball (' + str(i) + ').png').convert_alpha()
            self.__ball_pop.append(self.__temp_image)

        self.__ball_pop_up = []
        for i in range(1,3):
            self.__temp_image = pygame.image.load('./image/water_ball/up/end_waterball_up (' + str(i) + ').png').convert_alpha()
            self.__ball_pop_up.append(self.__temp_image)

        self.__ball_pop_down = []
        for i in range(1,4):
            self.__temp_image = pygame.image.load('./image/water_ball/down/end_waterball_down (' + str(i) + ').png').convert_alpha()
            self.__ball_pop_down.append(self.__temp_image)

        self.__ball_pop_left = []
        for i in range(1,4):
            self.__temp_image = pygame.image.load('./image/water_ball/left/end_waterball_left (' + str(i) + ').png').convert_alpha()
            self.__ball_pop_left.append(self.__temp_image)

        self.__ball_pop_right = []
        for i in range(1,4):
            self.__temp_image = pygame.image.load('./image/water_ball/right/end_waterball_right (' + str(i) + ').png').convert_alpha()
            self.__ball_pop_right.append(self.__temp_image)

        self.__ball_length_up = []
        self.ball1 = pygame.image.load("./image/water_ball/up/pop_half_up (1).png").convert_alpha()
        self.ball2 = pygame.image.load("./image/water_ball/up/pop_half_up (2).png").convert_alpha()
        self.ball3 = pygame.image.load("./image/moo.png").convert_alpha()
        self.__ball_length_up = [self.ball1, self.ball2, self.ball1, self.ball2, self.ball3]

        self.__ball_length_down = []
        self.ball1 = pygame.image.load("./image/water_ball/down/pop_half_down (1).png").convert_alpha()
        self.ball2 = pygame.image.load("./image/water_ball/down/pop_half_down (2).png").convert_alpha()
        self.ball3 = pygame.image.load("./image/moo.png").convert_alpha()
        self.__ball_length_down = [self.ball1, self.ball2, self.ball1, self.ball2, self.ball3]

        self.__ball_length_left = []
        self.ball1 = pygame.image.load("./image/water_ball/left/pop_half_left (1).png").convert_alpha()
        self.ball2 = pygame.image.load("./image/water_ball/left/pop_half_left (2).png").convert_alpha()
        self.ball3 = pygame.image.load("./image/moo.png").convert_alpha()
        self.__ball_length_left = [self.ball1, self.ball2, self.ball1, self.ball2, self.ball3]

        self.__ball_length_right = []
        self.ball1 = pygame.image.load("./image/water_ball/right/pop_half_right (1).png").convert_alpha()
        self.ball2 = pygame.image.load("./image/water_ball/right/pop_half_right (2).png").convert_alpha()
        self.ball3 = pygame.image.load("./image/moo.png").convert_alpha()
        self.__ball_length_right = [self.ball1, self.ball2, self.ball1, self.ball2, self.ball3]

        self.image = self.__ball_list[0]
        self.rect = self.ball1.get_rect()
        self.rect.left = 1000
        self.rect.top = 1000

        self.__index = 0
        self.__counter = 0
        self.__putting = False

    def put(self, left, top):
        self.rect.left = left
        self.rect.top = top
        self.__putting = True

    def ball_put(self):
        ball_list = [self.ball1, self.ball2, self.ball3, self.ball4]
        return ball_list

    def ball_length_up(self):
        self.ball1 = pygame.image.load("./image/water_ball/up/pop_half_up (1).png").convert_alpha()
        self.ball2 = pygame.image.load("./image/water_ball/up/pop_half_up (2).png").convert_alpha()
        self.ball3 = pygame.image.load("./image/moo.png").convert_alpha()
        ball_list = [self.ball1, self.ball2, self.ball1, self.ball2, self.ball3]

        return ball_list

    def ball_length_down(self):
        self.ball1 = pygame.image.load("./image/water_ball/down/pop_half_down (1).png").convert_alpha()
        self.ball2 = pygame.image.load("./image/water_ball/down/pop_half_down (2).png").convert_alpha()
        self.ball3 = pygame.image.load("./image/moo.png").convert_alpha()
        ball_list = [self.ball1, self.ball2, self.ball1, self.ball2, self.ball3]

        return ball_list

    def ball_length_left(self):
        self.ball1 = pygame.image.load("./image/water_ball/left/pop_half_left (1).png").convert_alpha()
        self.ball2 = pygame.image.load("./image/water_ball/left/pop_half_left (2).png").convert_alpha()
        self.ball3 = pygame.image.load("./image/moo.png").convert_alpha()
        ball_list = [self.ball1, self.ball2, self.ball1, self.ball2, self.ball3]

        return ball_list

    def ball_length_right(self):
        self.ball1 = pygame.image.load("./image/water_ball/right/pop_half_right (1).png").convert_alpha()
        self.ball2 = pygame.image.load("./image/water_ball/right/pop_half_right (2).png").convert_alpha()
        self.ball3 = pygame.image.load("./image/moo.png").convert_alpha()
        ball_list = [self.ball1, self.ball2, self.ball1, self.ball2, self.ball3]

        return ball_list

    def update(self):
        self.__counter += 1
        if self.__putting == True and self.__counter % 12 == 0:
            try:
                self.__index += 1
                self.image = self.__ball_list[self.__index]
            except IndexError:
                self.__putting = False
                self.__index = 0
                self.rect.left = 1000
                self.rect.top = 1000
                self.image = self.__ball_length_up[4]

        # else : self.image = self.__ball_list[0]

class Popleft(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)

        self.__ball_list = []
        self.ball0 = pygame.image.load("./image/moo.png").convert_alpha()
        self.ball1 = pygame.image.load("./image/water_ball/left/end_waterball_left (1).png").convert_alpha()
        self.ball2 = pygame.image.load("./image/water_ball/left/end_waterball_left (2).png").convert_alpha()
        self.ball3 = pygame.image.load("./image/water_ball/left/end_waterball_left (3).png").convert_alpha()
        self.__ball_list = [self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball1, self.ball2, self.ball3, self.ball2]

        self.image = self.ball0
        self.rect = self.ball1.get_rect()
        self.rect.left = 0
        self.rect.top = 0
        self.__index = 0
        self.__counter = 0
        self.__putting = False

    def put(self):
        self.__putting = True

    def update(self,left,top):
        self.__counter += 1
        if self.__putting == True and self.__counter % 12 == 0:
            try:
                self.__index += 1
                self.image = self.__ball_list[self.__index]
                if self.__index > 7: self.rect.left = left-40;  self.rect.top = top
            except IndexError:
                self.__putting = False
                self.__index = 0
                self.rect.left = 1000
                self.rect.top = 1000

class Popright(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)

        self.__ball_list = []
        self.ball0 = pygame.image.load("./image/moo.png").convert_alpha()
        self.ball1 = pygame.image.load("./image/water_ball/right/end_waterball_right (1).png").convert_alpha()
        self.ball2 = pygame.image.load("./image/water_ball/right/end_waterball_right (2).png").convert_alpha()
        self.ball3 = pygame.image.load("./image/water_ball/right/end_waterball_right (3).png").convert_alpha()
        self.__ball_list = [self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball1, self.ball2, self.ball3, self.ball2]

        self.image = self.ball0
        self.rect = self.ball1.get_rect()
        self.rect.left = 0
        self.rect.top = 0
        self.__index = 0
        self.__counter = 0
        self.__putting = False

    def put(self):
        self.__putting = True

    def update(self,left,top):
        self.__counter += 1
        if self.__putting == True and self.__counter % 12 == 0:
            try:
                self.__index += 1
                self.image = self.__ball_list[self.__index]
                if self.__index > 7: self.rect.left = left+40;  self.rect.top = top

            except IndexError:
                self.__putting = False
                self.__index = 0
                self.rect.left = 1000
                self.rect.top = 1000

class Popup(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)

        self.__ball_list = []
        self.ball0 = pygame.image.load("./image/moo.png").convert_alpha()
        self.ball1 = pygame.image.load("./image/water_ball/up/end_waterball_up (1).png").convert_alpha()
        self.ball2 = pygame.image.load("./image/water_ball/up/end_waterball_up (2).png").convert_alpha()
        self.ball3 = pygame.image.load("./image/water_ball/up/end_waterball_up (3).png").convert_alpha()
        self.__ball_list = [self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball1, self.ball2, self.ball3, self.ball2]

        self.image = self.ball0
        self.rect = self.ball1.get_rect()
        self.rect.left = 0
        self.rect.top = 0
        self.__index = 0
        self.__counter = 0
        self.__putting = False

    def put(self):
        self.__putting = True

    def update(self,left,top):
        self.__counter += 1
        if self.__putting == True and self.__counter % 12 == 0:
            try:
                self.__index += 1
                self.image = self.__ball_list[self.__index]
                if self.__index > 7: self.rect.left = left;  self.rect.top = top-40

            except IndexError:
                self.__putting = False
                self.__index = 0
                self.rect.left = 1000
                self.rect.top = 1000
class Popdown(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)

        self.__ball_list = []
        self.ball0 = pygame.image.load("./image/moo.png").convert_alpha()
        self.ball1 = pygame.image.load("./image/water_ball/down/end_waterball_down (1).png").convert_alpha()
        self.ball2 = pygame.image.load("./image/water_ball/down/end_waterball_down (2).png").convert_alpha()
        self.ball3 = pygame.image.load("./image/water_ball/down/end_waterball_down (3).png").convert_alpha()
        self.__ball_list = [self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball0,self.ball1, self.ball2, self.ball3, self.ball2]

        self.image = self.ball0
        self.rect = self.ball1.get_rect()
        self.rect.left = 0
        self.rect.top = 0
        self.__index = 0
        self.__counter = 0
        self.__putting = False

    def put(self):
        self.__putting = True

    def update(self,left,top):
        self.__counter += 1
        if self.__putting == True and self.__counter % 12 == 0:
            try:
                self.__index += 1
                self.image = self.__ball_list[self.__index]
                if self.__index > 7: self.rect.left = left;  self.rect.top = top+40
            except IndexError:
                self.__putting = False
                self.__index = 0
                self.rect.left = 1000
                self.rect.top = 1000

    # # 노란블록사라지는이미지-------
    # yblock1 = pygame.image.load("./image/빌리지/노란블럭 (2).png").convert_alpha()
    # yblock2 = pygame.image.load("./image/빌리지/노란블럭 (3).png").convert_alpha()
    # yblock3 = pygame.image.load("./image/빌리지/노란블럭 (4).png").convert_alpha()
    # yblock4 = pygame.image.load("./image/빌리지/노란블럭 (5).png").convert_alpha()
    # yblock5 = pygame.image.load("./image/빌리지/노란블럭 (6).png").convert_alpha()
    # yblock6 = pygame.image.load("./image/빌리지/노란블럭 (7).png").convert_alpha()
    # yblock7 = pygame.image.load("./image/빌리지/노란블럭 (8).png").convert_alpha()
    # yblock8 = pygame.image.load("./image/moo.png").convert_alpha()
    # # 노란블록리스트--------------
    # remove_block1 = [yblock1, yblock2, yblock3, yblock4, yblock5, yblock6, yblock7, yblock8]
    # # 빨간블록사라지는이미지-------
    # rblock1 = pygame.image.load("./image/빌리지/빨간블럭 (2).png").convert_alpha()
    # rblock2 = pygame.image.load("./image/빌리지/빨간블럭 (3).png").convert_alpha()
    # rblock3 = pygame.image.load("./image/빌리지/빨간블럭 (4).png").convert_alpha()
    # rblock4 = pygame.image.load("./image/빌리지/빨간블럭 (5).png").convert_alpha()
    # rblock5 = pygame.image.load("./image/빌리지/빨간블럭 (6).png").convert_alpha()
    # rblock6 = pygame.image.load("./image/빌리지/빨간블럭 (7).png").convert_alpha()
    # rblock7 = pygame.image.load("./image/빌리지/빨간블럭 (8).png").convert_alpha()
    # rblock8 = pygame.image.load("./image/moo.png").convert_alpha()
    # #빨간블록리스트--------------
    # remove_block2 = [rblock1, rblock2, rblock3, rblock4, rblock5, rblock6, rblock7, rblock8]
    # #박스블록사라지는이미지-------
    # bblock1 = pygame.image.load("./image/빌리지/박스사라짐 (1).png").convert_alpha()
    # bblock2 = pygame.image.load("./image/빌리지/박스사라짐 (2).png").convert_alpha()
    # bblock3 = pygame.image.load("./image/빌리지/박스사라짐 (3).png").convert_alpha()
    # bblock4 = pygame.image.load("./image/빌리지/박스사라짐 (4).png").convert_alpha()
    # bblock5 = pygame.image.load("./image/빌리지/박스사라짐 (5).png").convert_alpha()
    # bblock6 = pygame.image.load("./image/빌리지/박스사라짐 (6).png").convert_alpha()
    # bblock7 = pygame.image.load("./image/빌리지/박스사라짐 (7).png").convert_alpha()
    # bblock8 = pygame.image.load("./image/moo.png").convert_alpha()
    # #박스블록리스트--------------
    # remove_block3 = [bblock1, bblock2, bblock3, bblock4, bblock5, bblock6, bblock7, bblock8]
