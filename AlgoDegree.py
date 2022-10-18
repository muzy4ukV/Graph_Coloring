from Algo import *


class AlgoDegree(Algo):
    """Цей клас реалізує алгоритм розфарбовування пошук з поверненням з степеневою евристикою"""
    def __init__(self, graph,  algo_name="Backtraking algo (Degree)"):
        # Конструктор викликає контруктор базового класу й встановлює список можливих кольорів для вершин
        super().__init__(graph, algo_name)
        self._create_rand_colors()
        self.__flag = False


    def degree(self):
        # Реалізація алгоритму Backtracking Degree heuristic
        # Перевіряємо чи граф не пустий
        if len(self._graph) == 0:
            return []
        # Знаходимо вершину з найбільшим степенем й робимо перший рекурсивний виклик
        max_degree = list(self._graph)[0]
        for node in self._graph:
            if self._graph.degree[node] > self._graph.degree[max_degree]:
                max_degree = node
        self.__recursive_degree(max_degree)
        # Переписуємо присвоєні кольора для вершин у список та зберігаємо статистику
        self.__check_if_all_paint()
        self._set_color_map()
        self._save_statistics()
        return self._color_map

    def __recursive_degree(self, node):
        self._paint(node)
        while True:
            # Визанчаємо вершину-сусіда з найбільшим степенем для заданої
            next_node = self.__get_more_degrees_neighbor(node)
            # Якщо така існує і вона не розфарбована, то робимо наступний рекурсивний виклик для цієї вершини
            if next_node != '':
                self._num_of_changes_node -= 1
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
                if self._graph.degree[nbr] > max_degree:
                    self._num_of_changes_node += 1
                    max_degree = self._graph.degree[nbr]
                    next_node = nbr
        return next_node

    def __check_if_all_paint(self):
        for node in self._graph:
            if self._graph.nodes[node]['color'] == None:
                if not self.__flag:
                    self.__flag = True
                    messagebox.showwarning("Попередження", "В графі пристуні компоненти зв'язності")
                    self.__recursive_degree(node)
                else:
                    self.__recursive_degree(node)

