import sys

import pygame
import button
import level_1_kid
import level_2_adult
from pygame import mixer #importing the music library
pygame.mixer.init() # initializing the music library



# create display window
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
blue = (0,0,255)
green = (102,204,0)
mixer.music.load('Background.wav')  # initialized background music
mixer.music.play(0)  # playing music
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load('Memory_Background1.jpg')  # Set the background image
pygame.display.set_caption('Memory Puzzle')

# load button images
level1_img = pygame.image.load('level1.jpg').convert_alpha()
level2_img = pygame.image.load('level2.jpg').convert_alpha()
exit_img = pygame.image.load('exit_btn.jpg').convert_alpha()
Welcome_img = pygame.image.load('Welcome.jpg').convert_alpha()

# create button instances
Welcome_button = button.Button(220,90,Welcome_img,0.8)
level1_button = button.Button(100, 200, level1_img, 0.8)
level2_button = button.Button(400, 200, level2_img, 0.8)
exit_button = button.Button(275, 300, exit_img, 0.8)

# game loop

run = True
while run:

    screen.fill((202, 228, 241))
    screen.blit(background, (0, 0))

    if Welcome_button.draw(screen):
        print('Welcome to memory puzzle!!')

    if level1_button.draw(screen):
        pygame.mixer.music.stop()
        level_1_kid.main()
    if level2_button.draw(screen):
        pygame.mixer.music.stop()
        level_2_adult.main()
    if exit_button.draw(screen):
        print('EXIT')
        sys.exit(0)
    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
