from Algo import *
from Stack import *


class AlgoMRV(Algo):
    """Цей клас реалізує алгоритм розфарбовування пошук з поверненням з MRV евристикою"""

    def __init__(self, graph,  algo_name="Backtraking algo (MRV)"):
        # Конструктор викликає контруктор базового класу й встановлює список можливих кольорів для вершин
        super().__init__(graph,  algo_name)
        self._create_rand_colors()
        self.__flag = False

    def mrv(self):
        self.__mrv_stack(list(self._graph)[0])
        # Переписуємо присвоєні кольора для вершин у список та зберігаємо статистику
        self._set_color_map()
        self._save_statistics()
        return self._color_map

    def __mrv_stack(self, current_node):
        # Реалізація алгоритму Backtracking MRV
        # Встановлюємо колір для першої вершини
        self._graph.nodes[current_node]['color'] = self._list_of_colors[0]
        self._num_of_graph_states += 1
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
                    if current_color_num > max_color_num:
                        self._num_of_changes_node += 1
                        max_color_num = current_color_num
                        max_node = nbr
            # Якщо поточна вершина має нерозфарбованого сусіда,
            # тоді розфарбовуємо піхдодящу вершину та поміщаємо її у вершину стеку
            if not max_color_num == -1:
                self._num_of_changes_node -= 1
                self._paint(max_node)
                stack.push(max_node)
            else:
                # Якщо всі сусіди для поточної вершини розфарбовані, то видаляємо поточну вершину зі стеку
                stack.pop()
        # Зберігаємо кількість рекрсивних викликів та перевіряємо чи всі вершини розфарбовані
        self.__check_if_all_paint()

    def __get_amount_of_colors(self, node):
        # Метод, який повертає кількість унікальних кольорів з якими межує задана вершина
        color_list = list()
        for nbr in self._graph.neighbors(node):
            if self._graph.nodes[nbr]['color'] != None and not self._graph.nodes[nbr]['color'] in color_list:
                color_list.append(self._graph.nodes[nbr]['color'])
        return len(color_list)

    def __check_if_all_paint(self):
        # Перевіряє чи не залишилися ще нерозфарбовані вершини у графі
        for node in self._graph:
            if self._graph.nodes[node]['color'] == None:
                if not self.__flag:
                    self.__flag = True
                    messagebox.showwarning("Попередження", "В графі пристуні компоненти зв'язності")
                    self.__mrv_stack(node)
                else:
                    self.__mrv_stack(node)




