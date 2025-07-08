import pygame
from .constants import TILE_HEIGHT, TILE_WIDTH
from . color import *

map = [
    ['b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b'],
    ['b','x','x','x','x','x','x','x','x','x','b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','b'],   
    ['b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b'],
]

class Tile:
    def __init__(self, x, y):
        self.place = pygame.Rect(x, y, TILE_WIDTH, TILE_HEIGHT)
        self.color = GREEN

class Boundary(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = DARK_GREEN

    def checkCollision(self, hitbox):
        if self.place.colliderect(hitbox):
            return True

tiles = []
bound = []

for i in range(len(map)):
    for j in range(len(map[0])):
        if(map[i][j]=='x'):
            tiles.append(Tile(j*TILE_WIDTH, i*TILE_HEIGHT))
        elif(map[i][j]=='b'):
            tiles.append(Boundary(j*TILE_WIDTH, i*TILE_HEIGHT))
            bound.append(tiles[i*len(map[0])+j].place)