from Constants import *
from ViewModel import *
from Algo import *
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App(Tk):
    def __init__(self):
        super().__init__()
        # Рамка для вводу
        self.__input_frm = LabelFrame(self, text="Введення сипску ребер", relief=RAISED, borderwidth=7, font=("Arial", 16))
        self.__input_text = ScrolledText(self.__input_frm, width=30, height=10, font=("Arial", 16), padx=5, pady=5)
        self.__graph = ViewModel(self.__input_text)

        # Рамка для розміщення графу
        self.__graph_frm = LabelFrame(self, text="Зображення графу", relief=RAISED, borderwidth=7)
        self.__fig = plt.figure(figsize=(5 , 5))
        self.__canvas = FigureCanvasTkAgg(self.__fig, self.__graph_frm)

        # Рамка для розміщення віджетів
        self.__widgets_frm = Frame(self, relief=RAISED, borderwidth=7)
        self.__choose_algo = StringVar()
        self.__choose_algo.set("Жадібний")
        self.__algo_lbl = Label(self.__widgets_frm, text="Оберіть алгоритм розфарбовування")
        self.__greedy_rbtn = Radiobutton(self.__widgets_frm, variable=self.__choose_algo, value="Жадібний",
                                         text="Жадібний метод")
        self.__mrv_rbtn = Radiobutton(self.__widgets_frm, variable=self.__choose_algo, value="MRV",
                                      text="Пошук з поверненням (MRV)")
        self.__seek_rbtn = Radiobutton(self.__widgets_frm, variable=self.__choose_algo, value="Ступенева",
                                       text="Пошук з поверненням (Ступенева евристика)")
        self.__color_btn = Button(self.__widgets_frm, text="Розфарбувати граф", command=self.__color_graph)

        self.__exit_btn = Button(self.__widgets_frm, text="Вихід", command=self.__exit)
        self.__save_btn = Button(self.__widgets_frm, text="Зберегти результат", command=self.save_result)
        self.__upload_btn = Button(self.__widgets_frm, text="Зберегти результат", command=self.upload_result)

    def run(self):
        self.__setup_window()
        self.__draw_widgets()

    def __setup_window(self):
        self.title(WINDOW_NAME)
        # x = (self.winfo_screenwidth() - WINDOW_WIDTH) // 2
        # y = (self.winfo_screenheight() - WINDOW_HEIGHT) // 2 - 50
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}")
        self.iconbitmap(ICON_DIRECTION)
        self.resizable(False, False)

        self.__input_frm.grid(row=0, column=1, sticky="nswe")
        self.__graph_frm.grid(row=0, column=0, rowspan=2, sticky="nswe")
        self.__widgets_frm.grid(row=1, column=1, sticky="nswe")

        self.grid_columnconfigure(0, weight=10, minsize=700)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)

    def __draw_widgets(self):
        self.__input_text.pack()
        self.__input_text.insert("0.1", "Введіть список графу у форматі[1: 2 3 4]")

        self.__algo_lbl.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        self.__greedy_rbtn.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.__mrv_rbtn.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.__seek_rbtn.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.__color_btn.grid(row=4, column=0, padx=10, pady=5, sticky="we")
        self.__save_btn.grid(row=5, column=0, padx=10, pady=5, sticky="we")
        self.__exit_btn.grid(row=5, column=1, padx=10, pady=5, sticky="we")

    def __color_graph(self):
        graph = self.__graph.create_graph()
        colors = Algo(graph, self.__choose_algo.get())
        color_map = colors.get_colors()
        self.__fig.clf()
        nx.draw_networkx(graph, pos=nx.spring_layout(graph, 25),
                         with_labels=True, node_size=300, node_color=color_map)
        self.__canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
        self.__canvas.draw()

    def save_result(self):
        if len(self.__fig.axes):
            self.__fig.savefig(PHOTO_DIRECTION, format="PNG", dpi=200)
            messagebox.showinfo("", f"Граф збережений у {PHOTO_DIRECTION}")
        else:
            messagebox.showwarning("Попередження", "Ви не створили граф")

    def __exit(self):
        choice = messagebox.askyesno("Вихід", "Ви хочете закрити програму?")
        if choice:
            exit(0)
    def upload_result(self):
        pass