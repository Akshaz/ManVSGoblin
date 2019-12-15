import pygame, sys
from Projectile import Projectile

pygame.font.init()
pygame.mixer.init()

class Player:

    walkLeft = [pygame.image.load("Images/L1.png"), pygame.image.load("Images/L2.png"), pygame.image.load("Images/L3.png"), pygame.image.load("Images/L4.png"), pygame.image.load("Images/L5.png"), pygame.image.load("Images/L6.png"), pygame.image.load("Images/L7.png"), pygame.image.load("Images/L8.png"), pygame.image.load("Images/L9.png")]

    walkRight = [pygame.image.load("Images/R1.png"), pygame.image.load("Images/R2.png"), pygame.image.load("Images/R3.png"), pygame.image.load("Images/R4.png"), pygame.image.load("Images/R5.png"), pygame.image.load("Images/R6.png"), pygame.image.load("Images/R7.png"), pygame.image.load("Images/R8.png"), pygame.image.load("Images/R9.png")]


    def __init__(self, x, y, width, height):

        self.width = width
        self.height = height
        self.charSize = 64
        self.x, self.y = x, y-self.charSize
        self.inJump = False
        self.JumpCount = 10
        self.left = False
        self.right = False
        self.steps = False
        self.walkCount = 0
        self.standing = True
        self.bullets = []
        self.hitbox = (self.x+20, self.y, 28, 60)
        self.shootLoop = 0
        self.health = 100
        self.bullet = pygame.mixer.Sound("Music/bullet.wav")

    def draw(self, win, bg):
        win.blit(bg, (0,0))

        for bullet in self.bullets:
            bullet.draw(win)

        if self.walkCount + 1>=27:
                self.walkCount = 0

        if not self.standing:    
            if self.left:
                win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(self.walkLeft[0], (self.x,self.y))
            else:
                win.blit(self.walkRight[0], (self.x,self.y))
        self.hitbox = (self.x+20, self.y+3, 28, 57)
        pygame.display.update()

    def keyLogger(self):
        
        keys = pygame.key.get_pressed()

        if self.shootLoop > 0:
            self.shootLoop += 1
        if self.shootLoop > 3:
            self.shootLoop = 0
        
        if(keys[pygame.K_LEFT] and self.x > 0):
            self.x = self.x - self.charSize
            self.left = True
            self.right = False
            self.standing = False

        if(keys[pygame.K_RIGHT] and self.x < self.width - (self.charSize + 20)):
            self.x = self.x + self.charSize
            self.left = False
            self.right = True
            self.standing = False

        if(keys[pygame.K_SPACE] and self.shootLoop == 0 and len(self.bullets) < 5):

            self.bullet.play()

            if self.left:
                facing = -1

            else:
                facing = +1

            self.bullets.append(Projectile(self.x + self.charSize // 2, self.y + self.charSize //2, 6, (0,0,0),facing))

            self.shootLoop = 1

        else:
            self.standing = True
            self.walkCount = 0

        if keys[pygame.K_UP] and not self.inJump:
                self.inJump = True
                self.left = False
                self.right = False
                self.walkCount = 0

        if self.inJump:

            if self.JumpCount >= -10:

                if self.JumpCount < 0:
                    neg = -1

                else:
                    neg = 1

                self.y -= self.JumpCount ** 2 * 0.5 * neg
                self.JumpCount -= 1

            else:
                self.JumpCount = 10
                self.inJump = False

    def checkBullets(self):
        for bullet in self.bullets:
            if bullet.move(self.width):
                self.bullets.pop(self.bullets.index(bullet))
                
    def move(self, win, bg):
        self.keyLogger()
        self.checkBullets()
        self.draw(win, bg)

    def hit(self, win):
        self.inJump = False
        self.JumpCount = 10
        self.x = 0
        self.y = 480-self.charSize
        self.walkCount = 0
        font = pygame.font.SysFont('comicsans', 100)
        text = font.render("-5", 1,(255, 0, 0), )
        win.blit(text, (410, 240))
        pygame.display.update()
        i = 0
        while(i<100):
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    