from Algo import *


class AlgoGreedy(Algo):
    """Цей клас реалізує жадібний алгоритм розфарбовування"""
    def __init__(self, graph, algo_name="Greedy algo"):
        # Конструктор викликає контруктор базового класу й встановлює список можливих кольорів для вершин
        super().__init__(graph, algo_name)
        self._create_rand_colors()

    def greedy(self):
        # Реалізація алгоритму жадібного розфарбовування: намагаємося встановити перший доступний колір для кожної вершини
        for i in self._graph.nodes:
            self._paint(i)
        self._set_color_map()
        self._save_stastics()
        # повертаємо список кольрів для кожної вершини графу
        return self._color_map
