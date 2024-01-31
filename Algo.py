from random import randrange
from Constants import *
from tkinter import messagebox


class Algo:
    """Базовий клас для 3 алгоритмів розфарбовування, що містить спільні методи"""
    def __init__(self, graph, algo_name):
        # Конструктор приймає граф та створює два пустих списки для кольорів
        self._graph = graph
        self._list_of_colors = list()
        self._color_map = list()
        # Атрибути для збереження статистичних даних
        self._algo_name = algo_name
        self._num_of_colors = 0
        self._num_of_graph_states = 1
        self._num_of_changes_node = 0

    def _create_rand_colors(self):
        # Метод який створює список унікальних кольорів у форматі (R, G, B), для розфарбовування графу
        i = 1
        while len(self._graph) >= i:
            color = (randrange(0, 10) / 10, randrange(0, 10) / 10, randrange(0, 10) / 10)
            if not (color in self._list_of_colors):
                self._list_of_colors.append(color)
                i += 1

    def _paint(self, node):
        # Спільний метод для трьох алгоритмів, який присвоює вершині перший доступний колір з створеного списку
        num_color = 0
        num_neighbor = 0
        self._num_of_graph_states += 1
        neighbors = self.__get_neighbors(node)
        while num_neighbor < len(neighbors):
            node_color = self._list_of_colors[num_color]
            if self._graph.nodes[neighbors[num_neighbor]]['color'] == node_color:
                num_color += 1
                num_neighbor = 0
            else:
                num_neighbor += 1
        self._num_of_graph_states += num_color
        self._graph.nodes[node]['color'] = self._list_of_colors[num_color]

    def __get_neighbors(self, node):
        # Метод який повертає список вершин сусідів для заданої вершини
        neighbours = list()
        for nbr in self._graph.neighbors(node):
            neighbours.append(nbr)
        return neighbours

    def _set_color_map(self):
        # Заповнює атрибут _color_map кольорами, які присвоєні вершинам графу
        for node in self._graph.nodes:
            self._color_map.append(self._graph.nodes[node]['color'])

    def _save_statistics(self):
        # Метод призначений для збереження статистики
        self.__set_num_color()
        with open(ALGORITHM_STATISTICS, "wt") as file_out:
            print(self._algo_name, file=file_out)
            file_out.write(f"Number of used color: {self._num_of_colors}\n")
            file_out.write(f"Number of states of the graph: {self._num_of_graph_states}\n")
            file_out.write(f"The number of times we choose another node: {self._num_of_changes_node}")

    def __set_num_color(self):
        # Метод для обраховування кількості кольорів
        used_colors = list()
        for color in self._color_map:
            if not color in used_colors:
                used_colors.append(color)
        self._num_of_colors = len(used_colors)
