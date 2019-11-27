from abc import ABC, abstractmethod
import pygame

class Dino(ABC):

    def __init__(self, x, game_height, display):
        self.width = 30
        self.height = 70
        self.game_height = game_height
        self.x = x
        self.g = 1.5
        self.reset()
        if display:
            self.color = pygame.Color(0,255,0)

    def reset(self):
        self.v = 0
        self.y = 0
        self.is_jumping = False

    def jump(self):
        self.is_jumping = True
        self.v = 20
    
    def update(self, action):
        if self.is_jumping:
            self.v -= self.g
            self.y += self.v
            if self.y <= 0:
                self.y = 0
                self.v = 0
                self.is_jumping = False
        else:
            if action == 1:
                self.jump()
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.game_height-self.y-self.height, self.width, self.height))

    @abstractmethod
    def choose_action(self, state):
        return None