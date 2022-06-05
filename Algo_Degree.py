from Algo import *


class Algo_Degree(Algo):
    '''Цей клас реалізує алгоритм розфарбовування пошук з поверненням з степеневою евристикою'''
    def __init__(self, graph):
        super().__init__(graph)
        self._create_rand_colors()

    def degree(self):
        self.__recursive_degree(list(self._graph)[0])
        self._set_color_map()
        return self._color_map

    def __recursive_degree(self, node):
        self._paint(node)
        while True:
            next_node = self.__get_more_degrees_neighbor(node)
            if next_node:
                self.__recursive_degree(next_node)
            else:
                break

    def __get_more_degrees_neighbor(self, node):
        max_degree = 0
        next_node = ''
        for nbr in self._graph.neighbors(node):
            if self._graph.degree[nbr] > max_degree and self._graph.nodes[nbr]['color'] == None:
                max_degree = self._graph.degree[nbr]
                next_node = nbr
        return next_node
