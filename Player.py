import pygame
from Projectile import Projectile

class player:

    def __init__(self, x, y, width, height):

        self.walkLeft = [pygame.image.load("Images/L1.png"), pygame.image.load("Images/L2.png"), pygame.image.load("Images/L3.png"), pygame.image.load("Images/L4.png"), pygame.image.load("Images/L5.png"), pygame.image.load("Images/L6.png"), pygame.image.load("Images/L7.png"), pygame.image.load("Images/L8.png"), pygame.image.load("Images/L9.png")]

        self.walkRight = [pygame.image.load("Images/R1.png"), pygame.image.load("Images/R2.png"), pygame.image.load("Images/R3.png"), pygame.image.load("Images/R4.png"), pygame.image.load("Images/R5.png"), pygame.image.load("Images/R6.png"), pygame.image.load("Images/R7.png"), pygame.image.load("Images/R8.png"), pygame.image.load("Images/R9.png")]

        self.standing = pygame.image.load("Images/standing.png")

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
        pygame.display.update()

    def keyLogger(self):

        keys = pygame.key.get_pressed()

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

        if(keys[pygame.K_SPACE] and len(self.bullets) < 5):

            if self.left:
                facing = -1

            else:
                facing = +1

            self.bullets.append(Projectile(self.x + self.charSize // 2, self.y + self.charSize //2, 6, (0,0,0),facing))

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
