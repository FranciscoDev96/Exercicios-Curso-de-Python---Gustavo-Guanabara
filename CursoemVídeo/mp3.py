import pygame.base
from pygame import mixer
mixer.init()
mixer.music.load('light.mp3')
mixer.music.play()
mixer.music.set_volume(1.0) #1.0 é o volume máximo
mixer.music.get_busy()










