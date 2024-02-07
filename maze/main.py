import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Player
player_size = 20
player_x = 50
player_y = 50
player_speed = 5

# Maze
maze = [
        "*****************",
        "*               *",
        "*               *",
        "*               *",
        "*               *",
        "*               *",
        "*               *",
        "*               *",
        "*               *",
        "*               *",
        "*               *",
        "*               *",
        "*****************",
        ]

# Objects
objects = [(200, 200, red), (600, 400, green), (400, 300, blue)]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > player_speed:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size - player_speed:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > player_speed:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < height - player_size - player_speed:
        player_y += player_speed

    # Check for collisions with objects
    for obj_x, obj_y, obj_color in objects:
        obj_rect = pygame.Rect(obj_x, obj_y, player_size, player_size)
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        if player_rect.colliderect(obj_rect):
            objects.remove((obj_x, obj_y, obj_color))
            objects.append((random.randint(0, width - player_size), random.randint(0, height - player_size), random.choice([red, green, blue])))

    # Draw the maze
    screen.fill(white)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "*":
                pygame.draw.rect(screen, black, (j * player_size, i * player_size, player_size, player_size))

    # Draw the player
    pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))

    # Draw the objects
    for obj_x, obj_y, obj_color in objects:
        pygame.draw.rect(screen, obj_color, (obj_x, obj_y, player_size, player_size))

    pygame.display.flip()
    pygame.time.Clock().tick(30)
