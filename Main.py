import pygame
from Player import Player
from Enemy import Enemy 

score = 0
width,height = 820,480
pygame.display.init()
pygame.font.init()
win = pygame.display.set_mode((width, height))
bg = pygame.image.load("Images/bg.jpg")
win.blit(bg, (0,0))
pygame.display.set_caption("Man VS Goblin")
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 100, True)

def bulletStruck():
    global score
    for bullet in man.bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1] and bullet.x - bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[3]:
            man.bullets.pop(man.bullets.index(bullet))
            score += 10
            goblin.hit()

man = Player(0, 500-20, width+25, height)
goblin = Enemy(0, 425, 64, 64, 820-64)

running = True
while running:
    
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    man.move(win, bg)
    goblin.draw(win)
    text = font.render(f'Score: {score}', True, (0,0,0))
    win.blit(text, [0,0])
    bulletStruck()
    pygame.display.update()
    
pygame.display.quit()