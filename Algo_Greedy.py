from Algo import *


class Algo_Greedy(Algo):
    def __init__(self, graph):
        super().__init__(graph)
        self._create_rand_colors()

    def greedy(self):
        for i in self._graph.nodes:
            self._paint(i)
        self._set_color_map()
        return self._color_map
