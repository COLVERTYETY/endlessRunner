from settings import *
from npc import *
from player import *
from map import *
from game import *
import pygame as pg
import sys

class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.event = pg.event.get()
        self.ticks = 0
        self.health = 100
        self.dmg = 0
        self.score = 0
            
    def new(self):
        self.player = Player()
        self.map = Map()
        self.enemies = enemies()
    
    def update(self):
        if self.health <= 0 and self.dmg <= 2:
            self.running = False
            pg.quit()
            print("GAME OVER")
            print(f"SCORE: {self.score:.2f}")
            sys.exit()
        self.ticks+=1
        self.player.update(self.event)
        self.map.update()
        self.enemies.update(*self.player.pos, self)

    def events(self):
        self.event = list(pg.event.get()).copy()
        for event in self.event:
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                    pg.quit()
                    sys.exit()
        

    def draw(self):
        self.map.draw(*self.player.vel,self.screen)
        self.enemies.draw(*self.player.pos,self.screen)
        if self.dmg > 0:
            self.dmg -= 1
            pg.draw.rect(self.screen, (255, 0, 0), (0, 0, WIDTH, HEIGHT))
        pg.display.flip()


def main():
    g = Game()
    g.new()
    while g.running:
        g.events()
        g.update()
        g.draw()
        g.clock.tick(FPS)
    pg.quit()
    sys.exit()


if __name__ == '__main__':
    main()