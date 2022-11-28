import pygame as pg

class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
    
    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def vel(self):
        return (self.dx, self.dy)
    
    def update(self, events):
        dx = 20
        dy = 5
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.dx = -dx
                if event.key == pg.K_RIGHT:
                    self.dx = dx
                if event.key == pg.K_UP:
                    self.dy = -dy
                if event.key == pg.K_DOWN:
                    self.dy = dy
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.dx = 0
                if event.key == pg.K_RIGHT:
                    self.dx = 0
                if event.key == pg.K_UP:
                    self.dy = 0
                if event.key == pg.K_DOWN:
                    self.dy = 0
        self.x += self.dx
        self.y += self.dy
