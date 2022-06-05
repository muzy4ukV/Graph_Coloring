from random import randrange


class Algo:
    def __init__(self, graph):
        self._graph = graph
        self._list_of_colors = list()
        self._color_map = list()

    def _create_rand_colors(self):
        i = 1
        while len(self._graph) >= i:
            color = (randrange(0, 10, 2) / 10, randrange(0, 10, 2) / 10, randrange(0, 10, 2) / 10)
            if not(color in self._list_of_colors):
                self._list_of_colors.append(color)
                i += 1

    def _paint(self, node):
        num_color = 0
        num_neighbor = 0
        node_color = self._list_of_colors[num_color]
        neighbors = self._get_neighbors(node)
        while num_neighbor < len(neighbors):
            if self._graph.nodes[neighbors[num_neighbor]]['color'] == node_color:
                num_color += 1
                num_neighbor = 0
                node_color = self._list_of_colors[num_color]
            else:
                num_neighbor += 1
        self._graph.nodes[node]['color'] = node_color

    def _get_neighbors(self, node):
        neighbours = list()
        for nbr in self._graph.neighbors(node):
            neighbours.append(nbr)
        return neighbours

    def _set_color_map(self):
        for node in self._graph.nodes:
            self._color_map.append(self._graph.nodes[node]['color'])
