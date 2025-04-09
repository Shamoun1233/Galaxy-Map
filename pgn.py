import pygame
import sys

# Initialize pygame
pygame.init()

# Set window title to appear in Discord
pygame.display.set_caption("GTA VI  Pre-Alpha Debug Build 0.1")

# Set up screen
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Just fill with a dark gray for the "debug" vibe
    screen.fill((30, 30, 30))

    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()
