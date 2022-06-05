from Algo import *


class Algo_MRV(Algo):
    def __init__(self, graph):
        super().__init__(graph)
        self._create_rand_colors()

    def mrv(self):
        current_node = list(self._graph)[0]
        self._graph.nodes[current_node]['color'] = self._list_of_colors[0]
        stack = [current_node]
        while len(stack) > 0:
            node = stack[-1]
            max_color_num = -1
            max_node = ''
            for nbr in self._graph.neighbors(node):
                if self._graph.nodes[nbr]['color'] == None:
                    current_color_num = self.__get_amount_of_colors(nbr)
                    if current_color_num > max_color_num:
                        max_color_num = current_color_num
                        max_node = nbr
            if not max_color_num == -1:
                self._paint(max_node)
                stack.append(max_node)
            else:
                stack.pop()

        self._set_color_map()
        return self._color_map

    def __get_amount_of_colors(self, node):
        color_list = list()
        for nbr in self._graph.neighbors(node):
            if self._graph.nodes[nbr]['color'] != None and not self._graph.nodes[nbr]['color'] in color_list:
                color_list.append(self._graph.nodes[nbr]['color'])
        return len(color_list)

