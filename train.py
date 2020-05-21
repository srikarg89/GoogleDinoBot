from environment import Environment
from ai import AI

width = 800
height = 300
player = AI(30, height, None)
env = Environment(width, height, True, player)
env.run()