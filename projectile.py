import pygame

# define the class that will manage the projectile of our player
class Projectile(pygame.sprite.Sprite):

    # define the constructor of this class
    def __init__(self, player):
        super().__init__()
        self.velocity = 1
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # projectile rotation
        self.angle += 1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # check if the projectile collided with a monster
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            # delete the projectile
            self.remove()

        # check if our projectiles are no longer present on the screen
        if self.rect.x > 1080:
            # remove the projectile (outside the screen)
            self.remove()
            print('projectile delete')