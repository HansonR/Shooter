import pygame
import math
from game import Game
pygame.init()

# generate the game window
pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((1080, 720))

# game background
background = pygame.image.load('assets/bg.jpg')

# import and load our banner
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# import and load the launch button
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# load the game
game = Game()

running = True

# loop as long as this condition is true
while running:

    # apply game background
    screen.blit(background, (0, -200))

    # check if our has started or not
    if game.is_playing:
        # trigger game instructions
        game.update(screen)
    # check if our game has not started
    else:
        # add my welcome screen
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # update screen
    pygame.display.flip()

    # if the player closes this window
    for event in pygame.event.get():
        # that the event is window closing
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Game Over")
        # if a player releases a key on the keyboard
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detect if the space key is engaged to launch our projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check to see if the mouse collides with the play button
            if play_button_rect.collidepoint(event.pos):
                # put the game in "running" mode
                game.start()