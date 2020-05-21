import pygame
from dino import Dino

class MathBot(Dino):

    def __init__(self, x, game_height):
        super().__init__(x, game_height, True)
        self.last = 0
        self.first = True
    
    def choose_action(self, env):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

        if self.is_jumping:
            return 0
        
        if self.first:
#            print("Jump distance was", (env.score - self.last) * env.speed)
            self.first = False
        
        if len(env.obstacles) == 0:
            return 0
        nearest = env.obstacles[0]
        if nearest.x < self.x + self.width:
            if len(env.obstacles) == 1:
                return 0
            nearest = env.obstacles[1]

        dist = nearest.x - self.x - self.width
        if dist < 10:
            # Panic jump
            return 1
        dist_end = nearest.x + nearest.width - self.x
        # Kinematics to figure out how far dino will travel during jump
        t_apex = self.jump_v / self.g
        h_apex = (self.jump_v ** 2) / (2 * self.g)
        h_obs = nearest.height
        h_diff = h_apex - h_obs
        t_obs = (2 * h_diff / self.g) ** (1/2)
#        print(t_apex, t_obs)
        t = t_apex + t_obs
        travel_dist = env.speed * t
        print(travel_dist, env.speed, t)
        # Buffer so u don't keep it toooo close
        buffer = 10
#        print("RETURNING 1", travel_dist, dist_end)
        if travel_dist + buffer > dist_end:
            self.last = env.score
            self.first = True
            return 1
        return 0

