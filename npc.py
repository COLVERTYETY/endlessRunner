import pygame as pg
import sys
from settings import *
from sprites import *
import random

class enemies:
    sprites = {"soldier": sprite(["assets/soldier0.png","assets/soldier1.png","assets/soldier2.png","assets/soldier3.png"], 0.2),
        "demon": sprite(["assets/demon0.png","assets/demon1.png","assets/demon2.png","assets/demon3.png"], 0.1)}

    def __init__(self) -> None:
        self.ennemies = []
        self.rate = 0
    
    def add(self, name,i, x, y, dy):
        self.ennemies.append([name, i, x, y, dy])
    
    def update(self,x, y, game):
        self.rate += 1
        for i in enemies.sprites:
            enemies.sprites[i].update()
        # add a random enemie
        if len(self.ennemies) < (4+self.rate//1000) or random.randint(0, 100) < 1:
            self.add("soldier",random.randint(0, 10), x+WIDTH//2+random.randint(-1000, 1000), y + HEIGHT//2,(self.rate/500) + random.randint(20, 50)/100)
        if len(self.ennemies) < (1+self.rate//10000) or random.randint(0, 1000) < 1:
            self.add("demon",random.randint(0, 10), x+WIDTH//2+random.randint(-1000, 1000), y + HEIGHT//2,(self.rate/800) + random.randint(10, 30)/100)
            # print("added")
        # remove the ennemies that are too far
        for i,e in enumerate(self.ennemies):
            # check colision woith the player
            vel = e[4]*((e[3]-y)**2)/90000
            e[3]+= vel
            if e[3] - y > HEIGHT:
                if abs(e[2]-x - WIDTH)<WIDTH//3:
                    game.health -= 23
                    game.dmg = 5
                    # print(game.health)
                self.ennemies.pop(i)
                game.score += 7.3
                # print("removed")
                break
            # vel = (10000*e[4])/(abs( HEIGHT - e[3] + y)**4)
            # print(vel)
            # print(abs( HsEIGHT - e[3] + y))
        # SORT BY DISTANC EFOR RENDERING
        self.ennemies.sort(key=lambda x: x[3])
    
    def draw(self, x, y, screen):
        for e in self.ennemies:
            s = enemies.sprites[e[0]].draw(e[1])
            # scale the sprite
            size = TEXTURE_SIZE * ((2.5*(e[3]-y))**2)/900000
            # print("ssize is: ", size)
            s = pg.transform.scale(s, (size, size))
            # blit the sprite
            screen.blit(s, (e[2] - x - s.get_width(), e[3] - y - s.get_height()))
            # screen.blit(enemies.sprites[e[0]].draw(e[1]), (e[2]-x, e[3]))
    
    def get(self, i):
        return self.ennemies[i]