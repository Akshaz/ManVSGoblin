import pygame

class Projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

    def move(self, width):
        if self.x > 0 and self.x < width:
            self.x += self.vel
            return False
        else: return True

