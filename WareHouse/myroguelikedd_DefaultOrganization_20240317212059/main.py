'''
This is the main file of the game.
'''
import pygame
from player import Player
# Initialize pygame
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Roguelike Game")
# Create the player object
player = Player(window_width // 2, window_height // 2)
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.stop_up()
            elif event.key == pygame.K_s:
                player.stop_down()
            elif event.key == pygame.K_a:
                player.stop_left()
            elif event.key == pygame.K_d:
                player.stop_right()
    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.move_up()
    if keys[pygame.K_s]:
        player.move_down()
    if keys[pygame.K_a]:
        player.move_left()
    if keys[pygame.K_d]:
        player.move_right()
    # Update the game state
    player.update()
    # Render the game
    window.fill((0, 0, 0))  # Clear the window
    player.draw(window)  # Draw the player
    pygame.display.flip()  # Update the display
# Quit the game
pygame.quit()