import pygame


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
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 1

    def forward(self):
        # the movement is only done if there is no collision with a group of player
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity