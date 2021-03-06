import pygame
import random
from GameObject import GameObject

class Platform(GameObject):

    @staticmethod
    def init():
        Platform.platImage = pygame.transform.scale(pygame.image.load("assets/midTile.png"), (64, 64))


    def __init__(self, r, c, screenWidth, screenHeight, numRows, numCols):
        self.row, self.col = r, c
        x = ((screenWidth * 4) / numCols) * c
        y = (screenHeight / numRows) * r
        super(Platform, self).__init__(x, y, Platform.platImage)
        self.dx = 0

