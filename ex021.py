import pygame
import time

pygame.init()
pygame.mixer.init()

pygame.mixer_music.load('ex021.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer_music.play()

while pygame.mixer_music.get_busy():
    time.sleep(2)