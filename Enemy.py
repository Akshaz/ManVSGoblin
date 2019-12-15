import pygame

class Enemy:
    walkRight = [pygame.image.load('Images/R1E.png'), pygame.image.load('Images/R2E.png'), pygame.image.load('Images/R3E.png'), pygame.image.load('Images/R4E.png'), pygame.image.load('Images/R5E.png'), pygame.image.load('Images/R6E.png'), pygame.image.load('Images/R7E.png'), pygame.image.load('Images/R8E.png'), pygame.image.load('Images/R9E.png'), pygame.image.load('Images/R10E.png'), pygame.image.load('Images/R11E.png')]
    walkLeft = [pygame.image.load('Images/L1E.png'), pygame.image.load('Images/L2E.png'), pygame.image.load('Images/L3E.png'), pygame.image.load('Images/L4E.png'), pygame.image.load('Images/L5E.png'), pygame.image.load('Images/L6E.png'), pygame.image.load('Images/L7E.png'), pygame.image.load('Images/L8E.png'), pygame.image.load('Images/L9E.png'), pygame.image.load('Images/L10E.png'), pygame.image.load('Images/L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [0, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x+20, self.y, 28, 60)
        self.health = 100

    def draw(self, win):
        if self.health > 0:
            self.move()
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            
            self.hitbox = (self.x+20, self.y, 28, 57)
            pygame.draw.rect(win, (0, 255, 0), (820 - 3*self.health, 0, 300, 50))
            pygame.display.update()
            
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def hit(self):
        self.health -= 10