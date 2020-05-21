import pygame
from dino import Dino

class Human(Dino):

    def __init__(self, x, game_height):
        super().__init__(x, game_height, True)
    
    def choose_action(self, env):
        if self.is_jumping:
            return 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 1
        return 0

