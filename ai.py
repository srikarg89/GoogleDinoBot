"""
Setup stuff:
State = [distance to cactus, y position of dino, speed of cactus, width of cactus, height of cactus]
"""

import pygame
from dino import Dino
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
import numpy as np

class AI(Dino):

    def __init__(self, x, game_height, model):
        super().__init__(x, game_height, True)
        self.state_size = 4
        self.num_actions = 2
        self.learning_rate = .0001
        if model == None:
            model = self.create_model()
        self.model = model

    def create_model(self):
        # Basic sequential model
        model = Sequential()
        
        # Dense is a basic neural network layer
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.num_actions, activation='relu'))

        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return model

    def choose_action(self, env):
        state = self.get_state(env)
        print(state.shape)
        print(state)
        if self.is_jumping:
            return 0
        prediction = self.model.predict(state)
        action = np.argmax(prediction)
        print(action, prediction)
        return action
    
    def get_state(self, env):
        # State = [distance to cactus, speed of cactus, width of cactus, height of cactus]
        state = []
        # Find closest cactus
        closest = None
        mindist = float("inf")
        for obs in env.obstacles:
            if obs.x < self.x + self.width:
                continue
            if obs.x - self.x - self.width < mindist:
                mindist = obs.x - self.x - self.width
                closest = obs
#        print(closest, mindist)
        """
        second = None
        mindist2 = float("inf")
        for obs in env.obstacles:
            if obs.x < self.x + self.width:
                continue
            if obs == closest:
                continue
            if obs.x - self.x - self.width < mindist2:
                mindist2 = obs.x - self.x - self.width
                second = obs
#        print(closest, mindist)
        """
        if closest is None:
            state.append(1)
        else:
            state.append((mindist / env.speed) / env.width)
        """
        if second is None:
            state.append(1)
        else:
            state.append((mindist2 / env.speed) / env.width)
        # Normalize speed
#        state.append(env.speed / env.speed_data[1])
        """
        # Add noramlized cactus width and height
        if closest is None:
            state.append(0)
            state.append(0)
        else:
            state.append((closest.width / env.speed) / closest.max_width)
            state.append(closest.height / closest.max_height)
        
        return np.array(state).reshape(1,self.state_size)
