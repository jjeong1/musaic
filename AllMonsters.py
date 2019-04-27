import pygame
import random
from GameObject import GameObject
from Monster import Monster

class Slime(Monster):

    @staticmethod
    def init():
        image = pygame.image.load("assets/snake_idle.png")
        cellWidth, cellHeight = 41, 39
        Snake.idleFrame = list()
        for col in range(3):
            subImage = image.subsurface((col * cellWidth, 0, cellWidth, cellHeight))
            Snake.idleFrame.append(subImage)

        image = pygame.image.load("assets/snake_walk.png")
        cellWidth, cellHeight = 34, 38
        Snake.walkFrame = list()
        for col in range(3):
            subImage = image.subsurface((col * cellWidth, 0, cellWidth, cellHeight))
            Snake.walkFrame.append(subImage)

    def __init__(self, x, y, startingInterval):
        self.baseX = x
        self.baseY = y
        startingNote = random.randint([0, 11])
        super(Slime, self).__init__(x, y, startingNote, startingInterval, Slime.idleFrame[0])


class Snake(Monster):

    @staticmethod
    def init():
        image = pygame.image.load("assets/snake_idle.png")
        cellWidth, cellHeight = 41, 39
        Snake.idleFrame = list()
        for col in range(3):
            subImage = image.subsurface((col * cellWidth, 0, cellWidth, cellHeight))
            Snake.idleFrame.append(subImage)

        image = pygame.image.load("assets/snake_walk.png")
        cellWidth, cellHeight = 34, 38
        Snake.walkFrame = list()
        for col in range(3):
            subImage = image.subsurface((col * cellWidth, 0, cellWidth, cellHeight))
            Snake.walkFrame.append(subImage)

    def __init__(self, x, y, startingInterval):
        self.baseX = x
        self.baseY = y
        startingNote = random.randint([0, 11])
        super(Snake, self).__init__(x, y, startingNote, startingInterval, Snake.idleFrame[0])