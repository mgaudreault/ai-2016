from random import choice
from game import Game
from pathfinding import navigate_towards, shortest_path
import webbrowser

class Bot:

    def __init__(self):
        self.viewUrl = None
        self.game = None

    def findNearestEmptyMine(self):
        nearestLen = 9999
        nearest = None
        for mine in self.game.mines_locs:
            # print(str(len(shortest_path(self.game.board, self.game.hero.pos, mine)))
            if str(self.game.mines_locs[mine]) != str(self.game.hero.id).strip():
                # print(self.game.mines_locs[mine])
                path = shortest_path(self.game.board, self.game.hero.pos, mine)
                dist = len(path)
                if dist < nearestLen:
                    nearestLen = dist
                    nearest = path[0]

        return nearest

    def move(self, state):
        self.game = Game(state)

        if not self.viewUrl:
            self.viewUrl = state['viewUrl']
            webbrowser.open(self.viewUrl,new=2)

        # TODO implement SkyNet here
        # Pathfinding example:
        # dir = navigate_towards(game.board, game.hero.pos, (0, 0))
        # dirs = ['Stay', 'North', 'South', 'East', 'West']


        dest = self.findNearestEmptyMine()
        dirs = navigate_towards(self.game.board, self.game.hero.pos, dest)


        return dirs
