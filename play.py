from environment import Environment
from human import Human

player = Human(30, 500)
env = Environment(500, 500, True, player)
env.run()