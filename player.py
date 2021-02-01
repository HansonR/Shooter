import pygame
from projectile import Projectile


# create a first class that will represent our player
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # If the player has no more life points
            self.game.game_over()

    def update_health_bar(self, surface):
        # define the position of our life gauge as well as its width and thickness
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 7]
        # define the position of the background of our life gauge
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 7]

        # draw our life bar
        pygame.draw.rect(surface, (60, 63, 60), back_bar_position)
        pygame.draw.rect(surface, (111, 210, 46), bar_position)

    def launch_projectile(self):
        # create a new instance of the Projectile class
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # if the player does not collide with a monster
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity