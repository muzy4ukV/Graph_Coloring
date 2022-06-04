import networkx as nx
from tkinter import messagebox
from tkinter import *

class Create_Graph:
    def __init__(self, input_text):
        self.__input_text = input_text

    def create_graph(self):
        graph = nx.Graph()
        i = 1
        line = self.__input_text.get(f"{i}.0", f"{i}.end")
        while line:
            pos = line.find(":")
            if pos != -1:
                node = line[0:pos]
                graph.add_node(node, color=None)
                edges = line[pos + 1:]
                edges = edges.strip()
                edges = edges.split(" ")
                for node2 in edges:
                    if node == node2:
                        messagebox.showwarning("Попередження", "Петлі у графах не створюються")
                        continue
                    elif node2:
                        graph.add_edge(node, node2)
                i += 1
                line = self.__input_text.get(f"{i}.0", f"{i}.end")
            else:
                messagebox.showerror("Помилка", "Некоректно введені дані (Відсутній символ ':')")
                return nx.Graph()
        line = self.__input_text.get(f"{i}.0", END)
        line = line.replace('\n', '')
        if line:
            messagebox.showerror("Помилка", "Некоректно введені дані (Зайвий символ перенесення рядку)")
            return nx.Graph()
        self.__set_color_none(graph)
        return graph

    def __set_color_none(self, graph):
        for i in graph.nodes:
            graph.nodes[i]['color'] = None
