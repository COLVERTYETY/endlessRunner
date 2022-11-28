import pygame as pg
import sys
from settings import *



class sprite():
    def __init__(self, images, ds):
        self.images = []
        for image in images:
            self.images.append(pg.image.load(image))
        self.ds = ds
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
    
    def update(self):
        self.index += self.ds
        if self.index >= len(self.images):
            self.index = 0
        elif self.index < 0:
            self.index = len(self.images) - 1
        # self.image = self.images[int(self.index)]
    
    def draw(self, i):
        return self.images[(int(self.index)+i)%len(self.images)]