from settings import *
import pygame as pg


class Map():
    def __init__(self) -> None:
        # textures for the sky and the floor
        self.sky = self.get_texture('assets/sky.png', res = (WIDTH, HEIGHT//2))
        self.floor = self.get_texture('assets/floor.png')
        self.sky_offset = 0
        self.floor_offset = 0

    def update(self):
        pass
    
    def draw(self,dx,dy, screen):
        # render the background
        self.sky_offset = (self.sky_offset + 4.5 * -dx/10) % WIDTH
        screen.blit(self.sky, (self.sky_offset - WIDTH, 0))
        screen.blit(self.sky, (self.sky_offset, 0))
        # floor 
        # screen.blit(self.floor, (WIDTH, HEIGHT - TEXTURE_SIZE))
        pg.draw.rect(screen, (0, 0, 0), (0, HEIGHT//2, WIDTH, HEIGHT//2))
        # self.floor_offset = (self.floor_offset + dy)
        # render the floor with persepctive
        # for y in range(0, HEIGHT//2, TEXTURE_SIZE*4):
        #     x = WIDTH//2 - y//2
        #     w = WIDTH - 2*x
        #     h = TEXTURE_SIZE*4
        #     screen.blit(self.floor, (x, HEIGHT//2 + y), (0, 0, w, h))

        

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)