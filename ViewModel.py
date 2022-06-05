import networkx as nx
from tkinter import messagebox
from tkinter import *
from Constants import *
from Algo_Greedy import *
from Algo_MRV import *
from Algo_Degree import *


class ViewModel:
    '''Клас призначений для взаємодії візуального класу й класу алгоритму'''
    def __init__(self, input_text, rbnt_result, figure):
        self.__input_text = input_text
        self.__name_algo = rbnt_result
        self.__figure = figure
        self.__graph = nx.Graph()

    def get_graph(self):
        self.__graph = nx.Graph()
        i = 1
        line = self.__input_text.get(f"{i}.0", f"{i}.end")
        while line:
            pos = line.find(":")
            if pos != -1:
                self.__add_edges(pos, line)
                i += 1
                line = self.__input_text.get(f"{i}.0", f"{i}.end")
            else:
                messagebox.showerror("Помилка", "Некоректно введені дані (Відсутній символ ':')")
                return nx.Graph()
        self.__check_if_clear(i)
        self.__set_color_none()
        return self.__graph

    def __add_edges(self, pos, line):
        node = line[0:pos]
        self.__graph.add_node(node)
        edges = line[pos + 1:]
        edges = edges.strip()
        edges = edges.split(" ")
        for node2 in edges:
            if node == node2:
                messagebox.showwarning("Попередження", "Петлі у графах не створюються")
                continue
            elif node2:
                self.__graph.add_edge(node, node2)

    def __check_if_clear(self, i):
        line = self.__input_text.get(f"{i}.0", END)
        line = line.replace('\n', '')
        if line:
            messagebox.showerror("Помилка", "Некоректно введені дані (Зайві символи після введення)")
            return nx.Graph()

    def __set_color_none(self):
        for i in self.__graph.nodes:
            self.__graph.nodes[i]['color'] = None

    def get_color_map(self):
        if self.__name_algo.get() == "Жадібний":
            algo = Algo_Greedy(self.__graph)
            color_map = algo.greedy()
            return color_map

        elif self.__name_algo.get() == "MRV":
            algo = Algo_MRV(self.__graph)
            color_map = algo.mrv()
            return color_map

        elif self.__name_algo.get() == "Ступенева":
            algo = Algo_Degree(self.__graph)
            color_map = algo.degree()
            return color_map

        else:
            messagebox.showerror("Помилка", "Щось пішло не так")
            exit(0)

    def save_result(self):
        if len(self.__figure.axes):
            with open(SAVED_GRAPH, "wt") as file:
                file.write(self.__input_text.get("1.0", END))
            self.__figure.savefig(PHOTO_DIRECTION, format="PNG", dpi=200)
            messagebox.showinfo("", f"Граф збережений у {PHOTO_DIRECTION} та {SAVED_GRAPH}")
        else:
            messagebox.showwarning("Попередження", "Ви не розфарбували граф")

    def upload_result(self):
        try:
            file = open(SAVED_GRAPH, "rt")
            self.__input_text.delete('1.0', END)
            self.__input_text.insert("1.0", file.read())
            file.close()
        except IOError:
            messagebox.showerror("Помилка", f"Файлу {SAVED_GRAPH} не створено")

    @staticmethod
    def exit():
        choice = messagebox.askyesno("Вихід", "Ви хочете закрити програму?")
        if choice:
            exit(0)



