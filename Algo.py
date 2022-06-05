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
            self.mrv(list(self.__graph)[0])
            self.set_color_map()
            return self.__color_map
        elif self.__algo_name == "Ступенева":
            self.degree()
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

    def mrv(self, current_node):
        self.__graph.nodes[current_node]['color'] = self.__list_of_colors[0]
        stack = [current_node]
        while len(stack) > 0:
            node = stack[-1]
            max_color_num = -1
            max_node = ''
            for nbr in self.__graph.neighbors(node):
                if self.__graph.nodes[nbr]['color'] == None:
                    current_color_num = self.get_amount_of_colors(nbr)
                    if current_color_num > max_color_num:
                        max_color_num = current_color_num
                        max_node = nbr
            if not max_color_num == -1:
                self.paint(max_node)
                stack.append(max_node)
            else:
                stack.pop()

    def get_amount_of_colors(self, node):
        color_list = list()
        for nbr in self.__graph.neighbors(node):
            if self.__graph.nodes[nbr]['color'] != None and not self.__graph.nodes[nbr]['color'] in color_list:
                color_list.append(self.__graph.nodes[nbr]['color'])
        return len(color_list)


    def degree(self):
        self.recursive_degree(list(self.__graph)[0])

    def recursive_degree(self, node):
        self.paint(node)
        while True:
            next_node = self.get_more_degrees_neighbor(node)
            if next_node:
                self.recursive_degree(next_node)
            else:
                break

    def get_more_degrees_neighbor(self, node):
        max_degree = 0
        next_node = ''
        for nbr in self.__graph.neighbors(node):
            if self.__graph.degree[nbr] > max_degree and self.__graph.nodes[nbr]['color'] == None:
                max_degree = self.__graph.degree[nbr]
                next_node = nbr
        return next_node

    def set_color_map(self):
        for node in self.__graph.nodes:
            self.__color_map.append(self.__graph.nodes[node]['color'])