from Algo import *


class AlgoDegree(Algo):
    """Цей клас реалізує алгоритм розфарбовування пошук з поверненням з степеневою евристикою"""
    def __init__(self, graph,  algo_name="Backtraking algo (Degree)"):
        # Конструктор викликає контруктор базового класу й встановлює список можливих кольорів для вершин
        super().__init__(graph, algo_name)
        self._create_rand_colors()

    def degree(self):
        # Реалізація алгоритму Backtracking MRV
        # Перевіряємо чи граф не пустий
        if len(self._graph) == 0:
            return []
        # Робимо перший рекурсивний виклик для першої вершини
        self.__recursive_degree(list(self._graph)[0])
        # Переписуємо присвоєні кольора для вершин у список та зберігаємо статистику
        self._set_color_map()
        self._save_stastics()
        return self._color_map

    def __recursive_degree(self, node):
        self._num_recursion += 1
        self._paint(node)
        while True:
            # Визанчаємо вершину-сусіда з найбільшим степенем для заданої
            next_node = self.__get_more_degrees_neighbor(node)
            # Якщо така існує і вона не розфарбована, то робимо наступний рекурсивний виклик для цієї вершини
            if next_node:
                self.__recursive_degree(next_node)
            else:
                # Якщо всі сусіди для поточної вершини розфарбовані, то закінчуємо виклики
                break

    def __get_more_degrees_neighbor(self, node):
        # Метод, який повертає сусідню вершину з найбільшим степенем
        max_degree = 0
        next_node = ''
        for nbr in self._graph.neighbors(node):
            if self._graph.nodes[nbr]['color'] == None:
                self._num_of_comparision += 1
                if self._graph.degree[nbr] > max_degree:
                    self._num_of_changes_node += 1
                    max_degree = self._graph.degree[nbr]
                    next_node = nbr
        return next_node
