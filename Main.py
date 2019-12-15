import pygame

width,height = 852,480
charSize = 64
pygame.display.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")
pygame.display.update()

x, y = 0, 500-(charSize + 20)
bullet = False
inJump = False
JumpCount = 10
left = False
right = False
steps = False
walkCount = 0

walkLeft = [pygame.image.load("Images/L1.png"), pygame.image.load("Images/L2.png"), pygame.image.load("Images/L3.png"), pygame.image.load("Images/L4.png"), pygame.image.load("Images/L5.png"), pygame.image.load("Images/L6.png"), pygame.image.load("Images/L7.png"), pygame.image.load("Images/L8.png"), pygame.image.load("Images/L9.png")]

walkRight = [pygame.image.load("Images/R1.png"), pygame.image.load("Images/R2.png"), pygame.image.load("Images/R3.png"), pygame.image.load("Images/R4.png"), pygame.image.load("Images/R5.png"), pygame.image.load("Images/R6.png"), pygame.image.load("Images/R7.png"), pygame.image.load("Images/R8.png"), pygame.image.load("Images/R9.png")]
standing = pygame.image.load("Images/standing.png")
bg = pygame.image.load("Images/bg.jpg")

clock = pygame.time.Clock()

def keyLogger():
    global x, y, inJump, JumpCount, left, right,walkCount
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT] and x > 0):
        x = x - charSize
        left = True
        right = False
    elif(keys[pygame.K_RIGHT] and x < width - (charSize + 20)):
        x = x + charSize
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0

    if keys[pygame.K_SPACE] and not inJump:
            inJump = True
            left = False
            right = False
            walkCount = 0
    if inJump:
        if JumpCount >= -10:
            if JumpCount < 0:
                neg = -1
            else:
                neg = 1
            y -= JumpCount ** 2 * 0.5 * neg
            JumpCount -= 1
        else:
            JumpCount = 10
            inJump = False

def draw():
    global walkCount
    win.blit(bg, (0,0))
    if walkCount + 1>=27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(standing, (x,y))
    pygame.display.update()

running = True
while running:
    
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keyLogger()
    draw()
    
pygame.display.quit()