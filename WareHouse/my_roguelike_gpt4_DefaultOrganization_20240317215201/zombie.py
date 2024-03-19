'''
Defines the Zombie class for the top-down 2D roguelike zombie game.
'''
import pygame
from settings import Settings
from random import randint
class Zombie(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game  # Store the game instance
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self._ensure_safe_distance_from_player()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def _ensure_safe_distance_from_player(self):
        safe_distance = 100  # Define a safe distance from the player's starting position
        player_pos = self.game.player.rect.center
        while (self.rect.x - player_pos[0])**2 + (self.rect.y - player_pos[1])**2 < safe_distance**2:
            self.rect.x = randint(0, self.settings.screen_width - self.rect.width)
            self.rect.y = randint(0, self.settings.screen_height - self.rect.height)
    def update(self):
        # Calculate the distance to move on each axis
        delta_x = self.game.player.rect.x - self.rect.x
        delta_y = self.game.player.rect.y - self.rect.y
        distance = (delta_x ** 2 + delta_y ** 2) ** 0.5  # Pythagorean theorem
        # Normalize the movement if the zombie is not already on the player's position
        if distance != 0:
            norm_x = delta_x / distance
            norm_y = delta_y / distance
            # Move the zombie at a constant speed towards the player
            self.x += norm_x * self.settings.zombie_speed
            self.y += norm_y * self.settings.zombie_speed
        # Update the rect position
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)