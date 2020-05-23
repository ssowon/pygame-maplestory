import pygame

class BAZZY(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        #시작할때 뾰로롱
        self.__start = []
        for i in range(1, 11):
            self.__temp_image = pygame.image.load('./image/Bazzy/start_bazzy (' + str(i) + ').png').convert_alpha()
            self.__start.append(self.__temp_image)
        #죽을때
        self.__die = []
        for i in range(1, 12):
            self.__temp_image = pygame.image.load('./image/Bazzy/diebazzy (' + str(i) + ').png').convert_alpha()
            self.__die.append(self.__temp_image)
        #이겼을때
        self.__win = []
        for i in range(1, 5):
            self.__temp_image = pygame.image.load('./image/Bazzy/win_bazzy (' + str(i) + ').png').convert_alpha()
            self.__win.append(self.__temp_image)
        #물풍선 갇혓을때
        self.__inwater = []
        for i in range(1, 3):
            self.__temp_image = pygame.image.load('./image/Bazzy/bazzy_in_water (' + str(i) + ').png').convert_alpha()
            self.__inwater.append(self.__temp_image)
        #오른쪽 가는거
        self.__right = []
        for i in range(1,6):
            self.__temp_image = pygame.image.load ('./image/Bazzy/right_bazzy ('+str(i)+').png').convert_alpha()
            self.__right.append(self.__temp_image)
        #왼쪽 가는거
        self.__left = []
        for i in range(1, 6):
            self.__temp_image = pygame.image.load('./image/Bazzy/left_bazzy (' + str(i) + ').png').convert_alpha()
            self.__left.append(self.__temp_image)
        #위로 가는거
        self.__up = []
        for i in range(1, 6):
            self.__temp_image = pygame.image.load('./image/Bazzy/back_bazzy (' + str(i) + ').png').convert_alpha()
            self.__up.append(self.__temp_image)
        #아래로 가는거
        self.__down = []
        for i in range(1, 6):
            self.__temp_image = pygame.image.load('./image/Bazzy/front_bazzy (' + str(i) + ').png').convert_alpha()
            self.__down.append(self.__temp_image)

        #오른쪽으로 거북이 위에서
        self.__onright = []
        for i in range(1, 5):
            self.__temp_image = pygame.image.load('./image/Bazzy/right_bazzy_on (' + str(i) + ').png').convert_alpha()
            self.__onright.append(self.__temp_image)
        #왼쪽으로 거북이 위에서
        self.__onleft = []
        for i in range(1, 5):
            self.__temp_image = pygame.image.load('./image/Bazzy/left_bazzy_on (' + str(i) + ').png').convert_alpha()
            self.__onleft.append(self.__temp_image)
        # 위쪽으로 거북이 위에서
        self.__onup = []
        for i in range(1, 5):
            self.__temp_image = pygame.image.load('./image/Bazzy/back_bazzy_on (' + str(i) + ').png').convert_alpha()
            self.__onup.append(self.__temp_image)
        # 아래쪽으로 거북이 위에서
        self.__ondown = []
        for i in range(1, 5):
            self.__temp_image = pygame.image.load('./image/Bazzy/front_bazzy_on (' + str(i) + ').png').convert_alpha()
            self.__ondown.append(self.__temp_image)
        #서잇을때
        self.__stop = []
        for i in range(1, 4):
            self.__temp_image = pygame.image.load('./image/Bazzy/bazzy_stop (' + str(i) + ').png').convert_alpha()
            self.__stop.append(self.__temp_image)
        #서잇을때 거북이 위에서
        self.__onright_stop = pygame.image.load('./image/Bazzy/right_bazzy_on_stop.png').convert_alpha()
        self.__onleft_stop = pygame.image.load('./image/Bazzy/left_bazzy_on_stop.png').convert_alpha()
        self.__ondown_stop = pygame.image.load('./image/Bazzy/front_bazzy_on_stop.png').convert_alpha()
        self.__onup_stop = pygame.image.load('./image/Bazzy/back_bazzy_on_stop.png').convert_alpha()

        self.__right_stop = pygame.image.load('./image/Bazzy/start_bazzy (6).png').convert_alpha()
        self.__left_stop = pygame.image.load('./image/Bazzy/start_bazzy (8).png').convert_alpha()
        self.__down_stop = pygame.image.load('./image/Bazzy/start_bazzy (9).png').convert_alpha()
        self.__up_stop = pygame.image.load('./image/Bazzy/back_bazzy (4).png').convert_alpha()

        self.image = self.__down[0]#처음 이미지
        self.rect = self.image.get_rect()
        self.rect.left = 10
        self.rect.bottom = 120

        self.__dx = 0
        self.__dy = 0
        self.__index = 1
        self.__counter = 0


        self.__resting = True
        self.__walking = False
        self.__facing = 'down'
        self.__inwaterball = False
        self.__bazzy_die = False

    def moving(self,x_integer,y_integer):
        self.__dx = x_integer
        self.__dy = y_integer
        self.__resting = False
        self.__walking = True
        if x_integer > 0 :
            self.__facing = 'right'
        elif x_integer < 0:
            self.__facing = 'left'
        elif y_integer < 0 :
            self.__facing = 'up'
        elif y_integer > 0 :
            self.__facing = 'down'
        else :
            self.__walking = False
            self.__resting = True

    def in_waterball(self):
        self.__inwaterball = True
    def in_water(self):
        return self.__inwaterball
    def pin(self):
        self.__inwaterball = False
    def die(self):
        self.__bazzy_die = True

    def update(self):
        self.rect.centerx += self.__dx
        self.rect.centery += self.__dy
        self.__counter += 1
        if self.__walking == True and self.__facing == 'right' and self.__inwaterball == False and self.__bazzy_die == False and self.__counter %5 == 0 :
            try :
                self.__index += 1
                self.image = self.__right[self.__index]
            except IndexError:
                self.__index = 0
        elif self.__walking == True and self.__facing == 'left' and self.__inwaterball == False and self.__bazzy_die == False and self.__counter %5 == 0 :
            try :
                self.__index += 1
                self.image = self.__left[self.__index]
            except IndexError:
                self.__index = 0
        elif self.__walking == True and self.__facing == 'up' and self.__inwaterball == False and self.__bazzy_die == False and  self.__counter %5 == 0 :
            try :
                self.__index += 1
                self.image = self.__up[self.__index]
            except IndexError:
                self.__index = 0
        elif self.__walking == True and self.__facing == 'down' and self.__inwaterball == False and  self.__bazzy_die == False and self.__counter %5 == 0 :
            try :
                self.__index += 1
                self.image = self.__down[self.__index]
            except IndexError:
                self.__index = 0
        if self.__inwaterball == True and self.__bazzy_die == False and self.__counter %2 == 0:
            try :
                self.__index += 1
                self.image = self.__inwater[self.__index]
            except IndexError:
                self.__index = 0
        if self.__bazzy_die == True and self.__counter %11 == 0:
            try :
                self.__index += 1
                self.image = self.__die[self.__index]
            except IndexError:
                self.__index = 0

        if self.__resting == True and self.__inwaterball == False and  self.__bazzy_die == False and  self.__facing == 'right':
            self.image = self.__right_stop
        if self.__resting == True and self.__inwaterball == False and  self.__bazzy_die == False and self.__facing == 'left':
            self.image = self.__left_stop
        if self.__resting == True and self.__inwaterball == False and self.__bazzy_die == False and  self.__facing == 'up':
            self.image = self.__up_stop
        if self.__resting == True and self.__inwaterball == False and self.__bazzy_die == False and  self.__facing == 'down':
            self.image = self.__down_stop


class RODU(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        #시작할때 뾰로롱
        self.__start = []
        for i in range(1, 11):
            self.__temp_image = pygame.image.load('./image/rodu/start_rodu (' + str(i) + ').png').convert_alpha()
            self.__start.append(self.__temp_image)
        # 죽을때
        self.__die = []
        for i in range(1, 12):
            self.__temp_image = pygame.image.load('./image/rodu/die_rodu (' + str(i) + ').png').convert_alpha()
            self.__die.append(self.__temp_image)
        # 이겼을때
        self.__win = []
        for i in range(1, 5):
            self.__temp_image = pygame.image.load('./image/rodu/win_rodu (' + str(i) + ').png').convert_alpha()
            self.__win.append(self.__temp_image)
        # 물풍선 갇혓을때
        self.__inwater = []
        for i in range(1, 3):
            self.__temp_image = pygame.image.load(
                './image/rodu/rodu_in_water (' + str(i) + ').png').convert_alpha()
            self.__inwater.append(self.__temp_image)
        # 오른쪽 가는거
        self.__right = []
        for i in range(1, 6):
            self.__temp_image = pygame.image.load('./image/rodu/right_rodu (' + str(i) + ').png').convert_alpha()
            self.__right.append(self.__temp_image)
        # 왼쪽 가는거
        self.__left = []
        for i in range(1, 6):
            self.__temp_image = pygame.image.load('./image/rodu/left_rodu (' + str(i) + ').png').convert_alpha()
            self.__left.append(self.__temp_image)
        # 위로 가는거
        self.__up = []
        for i in range(1, 6):
            self.__temp_image = pygame.image.load('./image/rodu/back_rodu (' + str(i) + ').png').convert_alpha()
            self.__up.append(self.__temp_image)
        # 아래로 가는거
        self.__down = []
        for i in range(1, 6):
            self.__temp_image = pygame.image.load('./image/rodu/front_rodu (' + str(i) + ').png').convert_alpha()
            self.__down.append(self.__temp_image)
        # 오른쪽으로 거북이 위에서
        self.__onright = []
        for i in range(1, 5):
            self.__temp_image = pygame.image.load('./image/rodu/right_rodu_on (' + str(i) + ').png').convert_alpha()
            self.__onright.append(self.__temp_image)
        # 왼쪽으로 거북이 위에서
        self.__onleft = []
        for i in range(1, 5):
            self.__temp_image = pygame.image.load('./image/rodu/left_rodu_on (' + str(i) + ').png').convert_alpha()
            self.__onleft.append(self.__temp_image)
        # 위쪽으로 거북이 위에서
        self.__onup = []
        for i in range(1, 5):
            self.__temp_image = pygame.image.load('./image/rodu/back_rodu_on (' + str(i) + ').png').convert_alpha()
            self.__onup.append(self.__temp_image)
        # 아래쪽으로 거북이 위에서
        self.__ondown = []
        for i in range(1, 5):
            self.__temp_image = pygame.image.load('./image/rodu/front_rodu_on (' + str(i) + ').png').convert_alpha()
            self.__ondown.append(self.__temp_image)
        # 서잇을때
        self.__stop = []
        for i in range(1, 4):
            self.__temp_image = pygame.image.load('./image/rodu/rodu_stop (' + str(i) + ').png').convert_alpha()
            self.__stop.append(self.__temp_image)

        # 서잇을때 거북이 위에서
        self.__onright_stop = pygame.image.load('./image/rodu/right_rodu_on_stop.png').convert_alpha()
        self.__onleft_stop = pygame.image.load('./image/rodu/left_rodu_on_stop.png').convert_alpha()
        self.__ondown_stop = pygame.image.load('./image/rodu/front_rodu_on_stop.png').convert_alpha()
        self.__onup_stop = pygame.image.load('./image/rodu/back_rodu_on_stop.png').convert_alpha()

        self.__right_stop = pygame.image.load('./image/rodu/right_rodu (2).png').convert_alpha()
        self.__left_stop = pygame.image.load('./image/rodu/left_rodu (2).png').convert_alpha()
        self.__down_stop = pygame.image.load('./image/rodu/front_rodu (2).png').convert_alpha()
        self.__up_stop = pygame.image.load('./image/rodu/start_rodu (9).png').convert_alpha()

        self.image = self.__stop[1]#처음 이미지
        self.rect = self.image.get_rect()
        self.rect.right = 590
        self.rect.bottom = 80

        self.__dx = 0
        self.__dy = 0
        self.__index = 1
        self.__counter = 0


        self.__resting = True
        self.__walking = False
        self.__facing = 'down'
        self.__inwaterball = False
        self.__rodu_die = False

    def moving(self,x_integer,y_integer):
        self.__dx = x_integer
        self.__dy = y_integer
        self.__resting = False
        self.__walking = True
        if x_integer > 0 :
            self.__facing = 'right'
        elif x_integer < 0:
            self.__facing = 'left'
        elif y_integer < 0 :
            self.__facing = 'up'
        elif y_integer > 0 :
            self.__facing = 'down'
        else :
            self.__walking = False
            self.__resting = True

    def in_waterball(self):
        self.__inwaterball = True
    def in_water(self):
        return self.__inwaterball
    def pin(self):
        self.__inwaterball = False
    def die(self):
        self.__rodu_die = True


    def update(self):
        self.rect.centerx += self.__dx
        self.rect.centery += self.__dy
        self.__counter += 1
        if self.__walking == True and self.__facing == 'right' and self.__inwaterball == False and self.__counter %5 == 0 :
            try :
                self.__index += 1
                self.image = self.__right[self.__index]
            except IndexError:
                self.__index = 0
        elif self.__walking == True and self.__facing == 'left' and self.__rodu_die == False and self.__inwaterball == False and self.__counter %5 == 0 :
            try :
                self.__index += 1
                self.image = self.__left[self.__index]
            except IndexError:
                self.__index = 0
        elif self.__walking == True and self.__facing == 'up' and self.__rodu_die == False and self.__inwaterball == False and self.__counter %5 == 0 :
            try :
                self.__index += 1
                self.image = self.__up[self.__index]
            except IndexError:
                self.__index = 0
        elif self.__walking == True and self.__facing == 'down' and self.__rodu_die == False and self.__inwaterball == False and self.__counter %5 == 0 :
            try :
                self.__index += 1
                self.image = self.__down[self.__index]
            except IndexError:
                self.__index = 0
        if self.__inwaterball == True and self.__rodu_die == False and self.__counter %2 == 0:
            try :
                self.__index += 1
                self.image = self.__inwater[self.__index]
            except IndexError:
                self.__index = 0
        if self.__rodu_die == True and self.__counter %11 == 0:
            try :
                self.__index += 1
                self.image = self.__die[self.__index]
            except IndexError:
                self.__index = 0

        if self.__resting == True and self.__inwaterball == False and self.__rodu_die == False and self.__facing == 'right':
            self.image = self.__right_stop
        if self.__resting == True and self.__inwaterball == False and self.__rodu_die == False and self.__facing == 'left':
            self.image = self.__left_stop
        if self.__resting == True and self.__inwaterball == False and self.__rodu_die == False and self.__facing == 'up':
            self.image = self.__up_stop
        if self.__resting == True and self.__inwaterball == False and self.__rodu_die == False and self.__facing == 'down':
            self.image = self.__down_stop

class BOSS(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.__start = []
        for i in range(1, 7):
            self.__temp_image = pygame.image.load('./image/zombie/red/redzombie_front (' + str(i) + ').png').convert_alpha()
            self.__temp_image = pygame.transform.scale(self.__temp_image, (200,200))
            self.__start.append(self.__temp_image)
        self.__die_image = []
        for i in range(1,10):
            self.__temp_image = pygame.image.load('./image/zombie/red/show_redzombie (' + str(i) + ').png').convert_alpha()
            self.__temp_image = pygame.transform.scale(self.__temp_image, (200,200))
            self.__die_image.append(self.__temp_image)

        self.image = self.__start[0]#처음 이미지
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.top = 40
        self.__index = 1
        self.__counter = 0
        self.__die = False
    def die(self):
        self.__die = True
    def update(self):
        self.__counter += 1
        if self.__die == False and self.__counter %6 == 0:
            try :
                self.__index += 1
                self.image = self.__start[self.__index]
            except IndexError:
                self.__index = 0
        elif self.__die == True:
            try :
                self.__index += 1
                self.image = self.__die_image[self.__index]
            except IndexError:
                self.__index = 0