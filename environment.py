from obstacle import Obstacle
import time
import numpy as np
# Manually comment this if display is False
import pygame

class Environment:

    def __init__(self, width, height, display, dino):
        self.width = width
        self.height = height
        self.display = display
        self.dino = dino
        #Min speed, max speed, speed increment, and speed increment interval
#        self.speed_data = (8,100,1,100)
        slowest = self.width / 16
        fastest = self.width / 5
        self.speed_data = (slowest,fastest,10,100)
        self.obstacle_rate = 20
        self.reset()
    
    def reset(self):
        self.speed = self.speed_data[0]
        self.game_over = False
        self.score = 0
        if self.display:
            pygame.init()
            self.surface = pygame.display.set_mode((self.width, self.height))
            background = pygame.Surface((self.width, self.height))
            self.surface.blit(background, (0,0))
        self.dino.reset()
        self.obstacles = []

    def update(self):
        for obs in self.obstacles:
            obs.update(self.speed)
        if self.display:
            self.surface.fill(self.white)
            self.dino.draw(self.surface)        
        if self.check_collision():
            print('Score: ', str(self.score))
            self.game_over = True
        self.score += 1

        if self.score % self.speed_data[3] == 0:
            self.speed += self.speed_data[2]            
            self.speed = min(self.speed, self.speed_data[1])
        
        if self.score % self.obstacle_rate == 0:
            self.obstacles.append(Obstacle(self.width, self.height, self.display))

        length = len(self.obstacles)
        count = 0
        i = 0
        while i < len(self.obstacles):
            obs = self.obstacles[i]
            if obs.x + obs.width <= 0:
                self.obstacles.remove(obs)
                continue
            if self.display:
                obs.draw(self.surface)
            i += 1
#        print(self.score, self.obstacles)

    def run(self):
        if self.display:
            self.white = pygame.Color(255,255,255)
            pygame.display.set_caption('Google Dino Game')
            clock = pygame.time.Clock()
        keypressed = False
        while not self.game_over:
            action = self.dino.choose_action(self)
            if action == None:
                self.game_over = True
                break
            self.dino.update(action)

            self.update()
            if self.display:
                pygame.display.update()
                clock.tick(15)
            if self.game_over:
                break
        print("Score", self.score)
    
    def check_collision(self):
        dino = self.dino
        for obs in self.obstacles:
            # Rectangle collision
            if dino.x + dino.width < obs.x or dino.x > obs.x + obs.width:
                continue
            if dino.y + dino.height < obs.y or dino.y > obs.y + obs.height:
                continue
            return True
        return False