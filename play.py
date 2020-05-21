from environment import Environment
from human import Human
from mathbot import MathBot

width = 1000
height = 350
#player = Human(30, height)
player = MathBot(35, height)
env = Environment(width, height, True, player)
env.run()