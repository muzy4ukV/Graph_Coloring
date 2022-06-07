from Algo import *
from Stack import *


class AlgoMRV(Algo):
    """Цей клас реалізує алгоритм розфарбовування пошук з поверненням з MRV евристикою"""

    def __init__(self, graph,  algo_name="Backtraking algo (MRV)"):
        # Конструктор викликає контруктор базового класу й встановлює список можливих кольорів для вершин
        super().__init__(graph,  algo_name)
        self._create_rand_colors()

    def mrv(self):
        # Реалізація алгоритму Backtracking MRV
        # Перевіряємо чи граф не пустий
        if len(self._graph) == 0:
            return []
        # Встановлюємо колір для першої вершини
        current_node = list(self._graph)[0]
        self._graph.nodes[current_node]['color'] = self._list_of_colors[0]
        stack = Stack()
        stack.push(current_node)
        while not stack.is_empty():
            # Обираємо поточну вершину з голови стеку
            node = stack.top()
            # Встановлюємо наступну вершину для розфарбовування
            max_color_num = -1
            max_node = ''
            # Обходимо кожного сусіда для поточної вершини
            for nbr in self._graph.neighbors(node):
                if self._graph.nodes[nbr]['color'] == None:
                    # Якщо вершина-сусід ще не розфарбована, то обраховуємо кількість унікальних сусідніх кольорів для неї
                    current_color_num = self.__get_amount_of_colors(nbr)
                    # Якщо кількість кольорів вершини-сусіда, більша за попереднього сусіда,
                    # то встановлюємо першу для розфарбовування
                    self._num_of_comparision += 1
                    if current_color_num > max_color_num:
                        self._num_of_changes_node += 1
                        max_color_num = current_color_num
                        max_node = nbr
            # Якщо поточна вершина має нерозфарбованого сусіда,
            # тоді розфарбовуємо піхдодящу вершину та поміщаємо її у вершину стеку
            if not max_color_num == -1:
                self._paint(max_node)
                stack.push(max_node)
            else:
                # Якщо всі сусіди для поточної вершини розфарбовані, то видаляємо поточну вершину зі стеку
                stack.pop()
        # Переписуємо присвоєні кольора для вершин у список та зберігаємо статистику
        self._set_color_map()
        self._num_recursion = stack.get_num_recursion()
        self._save_stastics()
        return self._color_map

    def __get_amount_of_colors(self, node):
        # Метод, який повертає кількість ункікальних кольорів з якими межує задана вершина
        color_list = list()
        for nbr in self._graph.neighbors(node):
            if self._graph.nodes[nbr]['color'] != None and not self._graph.nodes[nbr]['color'] in color_list:
                color_list.append(self._graph.nodes[nbr]['color'])
        return len(color_list)
