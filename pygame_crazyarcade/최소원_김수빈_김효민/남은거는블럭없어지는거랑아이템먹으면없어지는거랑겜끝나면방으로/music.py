import pygame
from pygame import *

class MUSIC:
    def __init__(self, music):
        pygame.mixer.init()
        self.music = music

    def musicplay(self, sound):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(sound)
        pygame.mixer.music.play(-1)

class SoundEffect(MUSIC):
    def seplay(self, sound):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(sound)
        pygame.mixer.music.play(-1)