import pygame
import random


# create the class that will manage the notion of monster in our game
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 2)

    def damage(self, amount):
        # inflict damage
        self.health -= amount

        # check if his new number of life points is less than or equal to 0
        if self.health <= 0:
            # Reappear as a new monster
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health


    def update_health_bar(self, surface):

        # define the position of our life gauge as well as its width and thickness
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        # define the position of the background of our life gauge
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # draw our life bar
        pygame.draw.rect(surface, (60, 63, 60), back_bar_position)
        pygame.draw.rect(surface, (111, 210, 46), bar_position)


    def forward(self):
        # the movement is only done if there is no collision with a group of player
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # If the monster collides with the player
        else:
            # inflict damage (to the player)
            self.game.player.damage(self.attack)