import pygame
pygame.init()

# generate the game window
pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((1080, 720))

# game background
background = pygame.image.load('assets/bg.jpg')

running = True

# loop as long as this condition is true
while running:

    # apply game background
    screen.blit(background, (0, -200))

    # update screen
    pygame.display.flip()

    # if the player closes this window
    for event in pygame.event.get():
        # that the event is window closing
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Game Over")