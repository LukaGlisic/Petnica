import pygame
import random

pygame.init()
pygame.font.init()

screen_width = 500
screen_height = screen_width

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Elektricno polje")

def drawGrid():
    grid_list = []
    blockSize = 50
    for x in range(screen_width):
        for y in range(screen_height):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, (255,255,255), rect, 1)

running = True
while running:
    screen.fill((0,0,0))
    drawGrid()
    krug1 = pygame.draw.circle(screen, pygame.Color("red"), (300, 300), 50)
    pygame.draw.circle(screen, pygame.Color("red"), (100, 100), 50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()