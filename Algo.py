import networkx as nx
from random import randrange
from tkinter import messagebox

class Algo:
    def __init__(self, graph, algo):
        self.__graph = graph
        self.__algo_name = algo
        self.__list_of_colors = list()
        self.__color_map = list()

    def get_colors(self):
        self.__create_rand_colors()
        if self.__algo_name == "Жадібний":
            self.greedy()
            self.set_color_map()
            return self.__color_map
        elif self.__algo_name == "MRV":
            self.mrv()
            self.set_color_map()
            return self.__color_map
        elif self.__algo_name == "Ступенева":
            self.step()
            self.set_color_map()
            return self.__color_map
        else:
            messagebox.showerror("Помилка", "Щось пішло не так")
            exit(0)

    def __create_rand_colors(self):
        i = 1
        while len(self.__graph) >= i:
            color = (randrange(0, 10, 2) / 10, randrange(0, 10, 2) / 10, randrange(0, 10, 2) / 10)
            if not color in self.__list_of_colors:
                self.__list_of_colors.append(color)
                i += 1

    def greedy(self):
        for i in self.__graph.nodes:
            self.paint(i)

    def paint(self, node):
        num_color = 0
        num_neighbor = 0
        node_color = self.__list_of_colors[num_color]
        neighbors = self.get_neighbors(node)
        while num_neighbor < len(neighbors):
            if self.__graph.nodes[neighbors[num_neighbor]]['color'] == node_color:
                num_color += 1
                num_neighbor = 0
                node_color = self.__list_of_colors[num_color]
            else:
                num_neighbor += 1
        self.__graph.nodes[node]['color'] = node_color

    def get_neighbors(self, node):
        neighbours = list()
        for nbr in self.__graph.neighbors(node):
            neighbours.append(nbr)
        return neighbours

    def mrv(self):
        self.recursive_mrv(list(self.__graph)[0])

    def recursive_mrv(self, current_node):
        self.paint(current_node)
        for nbr in self.__graph.neighbors(current_node):
            if self.__graph.nodes[nbr]['color'] == None:
                self.recursive_mrv(nbr)

    def step(self):
        pass

    def set_color_map(self):
        for node in self.__graph.nodes:
            self.__color_map.append(self.__graph.nodes[node]['color'])

'''
    def try_color(self, i):
        try:
            self.__graph.nodes[i]['color'] = self.__color_map[i]
        except IndexError:
            pass
            
        neighbours = list()
        for num_node in self.__graph.neighbours(node):
            neighbours.append(self.__graph)
'''