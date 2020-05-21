import random
import pygame

class Obstacle:

    def __init__(self, board_width, board_height, display):
        self.x = board_width
        self.y = 0
        self.board_height = board_height
        self.max_width = 90
        self.max_height = 80
        if random.randint(0,1) == 0:
            # Make a small cactus
            cactus_width = 30
            self.height = 50
            self.width = cactus_width * random.randint(1,4)
        else:
            # Make a big cactus
            cactus_width = 30
            self.height = 80
            self.width = cactus_width * random.randint(1,3)
        if display:
            self.color = pygame.Color(255,0,0)
    
    def update(self, speed):
        self.x -= speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.board_height-self.y-self.height, self.width, self.height))
