from ViewModel import *
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class View(Tk):
    """Клас призначений для представлення візуальної частини програми"""
    def __init__(self):
        super().__init__()
        """Рамка для розміщення графу"""
        self.__graph_frm = LabelFrame(self, text="Зображення графу", width=WINDOW_WIDTH // 3 * 2 - 50,
                                      font=("Comic Sans MS", 16))
        # Фігура й полотно призначене для відображення графу
        self.__figure = plt.figure(figsize=(8.15, WINDOW_HEIGHT / 100))
        self.__canvas = FigureCanvasTkAgg(self.__figure, self.__graph_frm)

        """Рамка для розміщення віджетів"""
        self.__widgets_frm = LabelFrame(self, text="Введення сипску суміжності", font=("Comic Sans MS", 16))
        # Віджет який приймає значення графу
        self.__input_text = ScrolledText(self.__widgets_frm, width=30, height=10, font=("Comic Sans MS", 16),
                                         wrap=WORD, pady=5, padx=5)
        # Змінна для збереження результату вибору алгоритму
        self.__name_algo = StringVar()
        self.__name_algo.set("Жадібний")
        # Rнопки для вибору алгоритму розфарбовування
        self.__algo_lbl = Label(self.__widgets_frm, text="Оберіть алгоритм розфарбовування", font=("Comic Sans MS", 14))
        self.__greedy_rbtn = Radiobutton(self.__widgets_frm, variable=self.__name_algo, value="Жадібний",
                                         text="Жадібний метод", font=("Comic Sans MS", 14))
        self.__mrv_rbtn = Radiobutton(self.__widgets_frm, variable=self.__name_algo, value="MRV",
                                      text="Пошук з поверненням (MRV)", font=("Comic Sans MS", 14))
        self.__seek_rbtn = Radiobutton(self.__widgets_frm, variable=self.__name_algo, value="Ступенева",
                                       text="Пошук з поверненням (Ступенева евристика)", font=("Comic Sans MS", 14))
        # Атрибут класу ViewModel для звернення до його методів
        self.__vm = ViewModel(self.__input_text, self.__name_algo, self.__figure)
        # Кнопки для виконання операцій
        self.__color_btn = Button(self.__widgets_frm, text="Розфарбувати граф", command=self.__color_graph,
                                  font=("Comic Sans MS", 14))

        self.__exit_btn = Button(self.__widgets_frm, text="Вихід", command=self.__vm.exit, font=("Comic Sans MS", 14))
        self.__save_btn = Button(self.__widgets_frm, text="Зберегти результат", command=self.__vm.save_result,
                                 font=("Comic Sans MS", 14))
        self.__upload_btn = Button(self.__widgets_frm, text="Завантажити граф", command=self.__vm.upload_result,
                                   font=("Comic Sans MS", 14))

    def run(self):
        # Відкритий метод який запускає програму
        self.__setup_window()
        self.__draw_widgets()

    def __setup_window(self):
        # Метод для налаштування головного вікна
        self.title(WINDOW_NAME)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}")
        self.iconbitmap(ICON_DIRECTION)
        self.resizable(False, False)

        self.__graph_frm.pack(side=LEFT, fill=BOTH, padx=5, pady=5)
        self.__widgets_frm.pack(side=RIGHT, fill=BOTH, pady=5)

    def __draw_widgets(self):
        # Метод який розміщує віджети на головному екрані
        self.__input_text.grid(row=0, column=0, columnspan=2, sticky="we")
        self.__input_text.insert("1.0", "Введіть в це поле список суміжності графу у форматі\n")
        self.__input_text.insert("2.0", "[назва_вершини: суміжні_вершини (1 2 3)]")
        self.__algo_lbl.grid(row=1, column=0, padx=10, pady=5, columnspan=2)
        self.__greedy_rbtn.grid(row=2, column=0, padx=10, pady=5, sticky="w", columnspan=2)
        self.__mrv_rbtn.grid(row=3, column=0, padx=10, pady=5, sticky="w", columnspan=2)
        self.__seek_rbtn.grid(row=4, column=0, padx=10, pady=5, sticky="w", columnspan=2)
        self.__color_btn.grid(row=5, column=0, padx=10, pady=5, sticky="we", columnspan=2)
        self.__save_btn.grid(row=6, column=0, padx=10, pady=5, sticky="we")
        self.__upload_btn.grid(row=6, column=1, padx=10, pady=5, sticky="we")
        self.__exit_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="we")

    def __color_graph(self):
        # Закритий метод який візуалізує граф
        # Отримуємо граф від класу ViewModel
        graph = self.__vm.get_graph()
        # Отримуємо список кольорів вершин від класу ViewModel
        color_map = self.__vm.get_color_map()
        self.__figure.clf()
        nx.draw_networkx(graph, pos=nx.spring_layout(graph, 15), with_labels=True, node_size=350, node_color=color_map)
        self.__canvas.get_tk_widget().pack()
        self.__canvas.draw()
