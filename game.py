from player import Player
from monster import Monster
import pygame

# create a second class that will represent our game
class Game:

    def __init__(self):
        # define if our game has started or not
        self.is_playing = False
        # generate our player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Group of monster
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # Reset the game, remove the monsters, restore the players to maximum health and the game on hold
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # apply my player image
        screen.blit(self.player.image, self.player.rect)

        # refresh player life bar
        self.player.update_health_bar(screen)

        # collect player projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # get the monsters from our game
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # apply all the images of my group of projectiles
        self.player.all_projectiles.draw(screen)

        # apply the set of images of my monster group
        self.all_monsters.draw(screen)

        # check if the players prefer to go left or right
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)