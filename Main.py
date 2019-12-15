import pygame
from Player import Player
from Enemy import Enemy 

width,height = 820,480
pygame.display.init()
win = pygame.display.set_mode((width, height))
bg = pygame.image.load("Images/bg.jpg")
win.blit(bg, (0,0))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

man = Player(0, 500-20, width+25, height)
goblin = Enemy(100, 410, 64, 64, 300)

running = True
while running:
    
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    man.move(win, bg)
    goblin.draw(win)
    
pygame.display.quit()