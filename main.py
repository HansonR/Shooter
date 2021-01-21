import pygame
from game import Game
pygame.init()

# generate the game window
pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((1080, 720))

# game background
background = pygame.image.load('assets/bg.jpg')

# load the game
game = Game()

running = True

# loop as long as this condition is true
while running:

    # apply game background
    screen.blit(background, (0, -200))

    # apply my player image
    screen.blit(game.player.image, game.player.rect)

    # collect player projectiles
    for projectile in game.player.all_projectiles:
        projectile.move()

    # get the monsters from our game
    for monster in game.all_monsters:
        monster.forward()

    # apply all the images of my group of projectiles
    game.player.all_projectiles.draw(screen)

    # apply the set of images of my monster group
    game.all_monsters.draw(screen)

    # check if the players prefer to go left or right
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x)

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