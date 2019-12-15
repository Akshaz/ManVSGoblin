import pygame
from Player import Player
from Enemy import Enemy 

score = 0
width,height = 820,480
pygame.display.init()
pygame.font.init()
pygame.mixer.init()
win = pygame.display.set_mode((width, height))
bg = pygame.image.load("Images/bg.jpg")
win.blit(bg, (0,0))
pygame.display.set_caption("Man VS Goblin")
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 100, True)
text = font.render(f'Score: {score}', True, (0,0,0))
music = pygame.mixer.music.load("Music/music.mp3")
hit = pygame.mixer.Sound("Music/hit.wav")
pygame.mixer.music.play(-1)

def checkWinner():
    if goblin.health <= 0:
        text = font.render(f'You Win!', True, (0,0,0))
        win.blit(text, [width // 2 - 150, height // 2])

def detectCollision():
    global score
    if goblin.health > 0 and man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1] and man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0]  < goblin.hitbox[0] + goblin.hitbox[3]:
            score -= 5
            man.hit(win)
            
def bulletStruck():
    global score
    for bullet in man.bullets:
        if goblin.health > 0 and bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1] and bullet.x - bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[3]:
            man.bullets.pop(man.bullets.index(bullet))
            score += 10
            hit.play()
            goblin.hit()
                

man = Player(0, 500-20, width+25, height)
goblin = Enemy(410, 425, 64, 64, 820-64)

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
    detectCollision()
    checkWinner()
    pygame.display.update()
    
pygame.display.quit()