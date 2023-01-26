import pygame
from OnBoard import OnBoard

class Ladder(OnBoard):
    def __init__(self, raw_image, position):
        super(Ladder, self).__init__(raw_image, position)

    def updateImage(self, raw_image):
        self.image = raw_image
        self.image = pygame.transform.scale(self.image, (15, 15))
