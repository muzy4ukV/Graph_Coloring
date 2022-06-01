from Constants import *
from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()
        # рамка для графу
        self.__frm_graph = Frame(self, height=WINDOW_HEIGHT, width=WINDOW_WIDTH / 16 * 11, relief=RIDGE, borderwidth=7)
        # рамка для віджетів
        self.__frm_btn = Frame(self, height=WINDOW_HEIGHT / 2, width=WINDOW_WIDTH / 16 * 5, relief=RAISED, borderwidth=7)
        self.__lbl_nodes = Label(self.__frm_btn, text="Оберіть кількість вершин")
        self.__num_nodes = StringVar()
        self.__spn = Spinbox(self.__frm_btn, from_=2, to=30, textvariable=self.__num_nodes)
        self.__btn_nodes = Button(self.__frm_btn, text="Задати граф", command=self.__create_entries)
        self.__entries = list()

        self.__choose_algo = IntVar()
        self.__lbl_algo = Label(self.__frm_btn, text="Оберіть алгоритм розфарбовування")
        self.__rbtn_greegy = Radiobutton(self.__frm_btn, variable=self.__choose_algo, value=1, text="Жадібний метод")
        self.__rbtn_mrv = Radiobutton(self.__frm_btn, variable=self.__choose_algo, value=2, text="Пошук з поверненням (MRV)")
        self.__rbtn_seek = Radiobutton(self.__frm_btn, variable=self.__choose_algo, value=3, text="Пошук з поверненням (Ступенева евристика)")
        self.__btn_color = Button(self.__frm_btn, text="Розфарбувати граф")
        self.__btn_exit = Button(self.__frm_btn, text="Вихід", command=self.__exit)

        # рамка для вводу
        self.__frm_input = Frame(self, height=WINDOW_HEIGHT / 2, width=WINDOW_WIDTH / 16 * 5, relief=RAISED, borderwidth=7)
        self.__canvas = Canvas(self.__frm_input)
        self.__scrollbar = Scrollbar(self.__frm_input, orient=VERTICAL, command=self.__canvas.yview)

        self.__frm_scnd = Frame(self.__canvas)


    def run(self):
        self.__frm_scnd.bind('<Configure>', lambda e: self.__canvas.configure(scrollregion=self.__canvas.bbox("all")))
        self.__setup_window()
        self.__canvas.create_window((0, 0), window=self.__frm_scnd, anchor=NW)
        self.__canvas.configure(yscrollcommand=self.__scrollbar.set)
        self.__draw_widgets()

    def __setup_window(self):
        self.title(WINDOW_NAME)
        x = (self.winfo_screenwidth() - WINDOW_WIDTH) // 2
        y = (self.winfo_screenheight() - WINDOW_HEIGHT) // 2 - 50
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
        self.iconbitmap(ICON_DIRECTION)
        self.resizable(False, False)

        self.__frm_graph.pack(side=LEFT, fill=BOTH)
        self.__frm_btn.pack(side=TOP, fill=BOTH)
        self.__frm_input.pack(side=TOP, fill=BOTH, expand=1)


        self.__canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.__scrollbar.pack(side=RIGHT, fill=Y)

    def __draw_widgets(self):
        self.__lbl_nodes.pack()
        self.__spn.pack()
        self.__btn_nodes.pack()

        self.__lbl_algo.pack()
        self.__rbtn_greegy.pack()
        self.__rbtn_mrv.pack()
        self.__rbtn_seek.pack()
        self.__btn_color.pack()
        self.__btn_exit.pack()

    def __create_entries(self):
        num_nodes = int(self.__num_nodes.get())
        self.__entries.clear()
        self.clearFrame()
        for i in range(num_nodes):
            Label(self.__frm_input, text=f"{i+1}").pack()
            tmp = Entry(self.__frm_input).pack()
            self.__entries.append(tmp)

    def clearFrame(self):
        # destroy all widgets from frame
        for widget in self.__frm_input.winfo_children():
            widget.destroy()

    def __exit(self):
        self.destroy()






