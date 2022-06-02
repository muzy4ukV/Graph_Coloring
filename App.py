from Constants import *
from tkinter import *
from Draw_Graph import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App(Tk):
    def __init__(self):
        super().__init__()
        # Рамка для вводу
        self.__input_frm = LabelFrame(self, text="Введення сипску ребер", relief=RAISED, borderwidth=7)
        self.__input_canvas = Canvas(self.__input_frm)
        self.__scrollbar = Scrollbar(self.__input_frm, orient=VERTICAL, command=self.__input_canvas.yview)
        self.__help_frm = Frame(self.__input_canvas)
        # Рамка для розміщення графу
        self.__graph_frm = LabelFrame(self, text="Зображення графу", relief=RAISED, borderwidth=7)
        # Рамка для розміщення віджетів
        self.__widgets_frm = Frame(self, relief=RAISED, borderwidth=7)
        self.__choose_lbl = Label(self.__widgets_frm, text="Оберіть кількість вершин")
        self.__num_nodes = StringVar()
        self.__num_nodes.set("60")
        self.__spn = Spinbox(self.__widgets_frm, from_=2, to=100, textvariable=self.__num_nodes,
                             command=self.__create_entries)
        self.__entries = list()

        self.__choose_algo = IntVar()
        self.__algo_lbl = Label(self.__widgets_frm, text="Оберіть алгоритм розфарбовування")
        self.__greedy_rbtn = Radiobutton(self.__widgets_frm, variable=self.__choose_algo, value=1,
                                         text="Жадібний метод")
        self.__mrv_rbtn = Radiobutton(self.__widgets_frm, variable=self.__choose_algo, value=2,
                                      text="Пошук з поверненням (MRV)")
        self.__seek_rbtn = Radiobutton(self.__widgets_frm, variable=self.__choose_algo, value=3,
                                       text="Пошук з поверненням (Ступенева евристика)")
        self.__color_btn = Button(self.__widgets_frm, text="Розфарбувати граф", command=self.__draw_graph)

        self.__exit_btn = Button(self.__widgets_frm, text="Вихід", command=self.__exit)


    def run(self):
        self.__setup_window()
        self.__draw_widgets()

    def __draw_widgets(self):
        self.__put_scrollbar()

        self.__create_entries()
        self.__choose_lbl.pack()
        self.__spn.pack()
        self.__algo_lbl.pack()
        self.__greedy_rbtn.pack()
        self.__mrv_rbtn.pack()
        self.__seek_rbtn.pack()
        self.__color_btn.pack()

        self.__exit_btn.pack()

    def __setup_window(self):
        self.title(WINDOW_NAME)
        x = (self.winfo_screenwidth() - WINDOW_WIDTH) // 2
        y = (self.winfo_screenheight() - WINDOW_HEIGHT) // 2 - 50
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
        self.iconbitmap(ICON_DIRECTION)
        self.resizable(False, False)

        self.__input_frm.grid(row=0, column=1, sticky="nswe")
        self.__graph_frm.grid(row=0, column=0, rowspan=2, sticky="nswe")
        self.__widgets_frm.grid(row=1, column=1, sticky="nswe")

        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)

    def __put_scrollbar(self):
        self.__input_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.__scrollbar.pack(side=RIGHT, fill=Y)
        self.__input_canvas.configure(yscrollcommand=self.__scrollbar.set)
        self.__input_canvas.bind('<Configure>',
                                 lambda e: self.__input_canvas.configure(scrollregion=self.__input_canvas.bbox(ALL)))
        self.__input_canvas.create_window((0, 0), window=self.__help_frm, anchor=NW)

    def __create_entries(self):
        num_nodes = int(self.__num_nodes.get())
        self.__entries.clear()
        self.clear_frame(self.__help_frm)
        for i in range(num_nodes):
            Label(self.__help_frm, text=f"{i + 1}: ").grid(row=i, column=0)
            tmp = Entry(self.__help_frm, width=ENTRIES_WIDTH)
            tmp.grid(row=i, column=1)
            self.__entries.append(tmp)

    def __exit(self):
        self.destroy()

    def __draw_graph(self):
        self.__graph = Draw_Graph(self.__entries, int(self.__num_nodes.get()))
        self.__graph.create_graph()

    def clear_frame(self, frame):
        # destroy all widgets from frame
        for widget in frame.winfo_children():
            widget.destroy()
