import networkx as nx
from tkinter import *
import matplotlib.pyplot as plt

class Draw_Graph:
    def __init__(self, entries, num_nodes):
        self.__entries = entries
        self.__num_nodes = num_nodes
        self.__graph = nx.Graph()

    def create_graph(self):
        # доробити перевірку
        if not self.__entries:
            return
        self.__graph.add_nodes_from(range(1, self.__num_nodes + 1))
        for i in range(0, self.__num_nodes):
            line = self.__entries[i].get()
            line = line.split(', ')
            for j in line:
                if not j == '':
                    self.__graph.add_edge(i + 1, int(j))
        print(self.__graph.nodes)
        print(self.__graph.edges)


    def draw_graph(self):
        self.create_graph()





