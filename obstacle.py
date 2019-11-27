import random
import pygame

class Obstacle:

    def __init__(self, board_width, board_height, display):
        self.x = board_width
        self.y = 0
        self.board_height = board_height
        self.width = random.randint(40,80)
        self.height = random.randint(30,50)
        if display:
            self.color = pygame.Color(255,0,0)
    
    def update(self, speed):
        self.x -= speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.board_height-self.y-self.height, self.width, self.height))
