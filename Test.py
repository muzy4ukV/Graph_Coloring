import psutil
import tkinter as tk
from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

root = Tk()
root.title("Hello")

mlist = psutil.net_connections(kind="all")
fig = plt.figure(frameon=True, figsize=(5,1), dpi=100)
canvas = FigureCanvasTkAgg(fig, root)
Node = nx.Graph()

for v, val in enumerate(mlist):
    if val[4] != () and val[4][0] != "127.0.0.1":
        print(str(val[4][0]) + " - " + str(val[6]))
        print(psutil.Process(val[6]).name())
        Node.add_node(str(val[4][0]))
        Node.add_edge(str(val[4][0]), "localhost")

plt.gca().set_facecolor("grey")
fig.set_facecolor("black")

nx.draw_networkx(Node, pos=nx.spring_layout(Node, 25), alpha=1,
                 with_labels=False, node_size=100, node_color="green")

canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

def Add():
    Node.add_node(str("LOL"))
    plt.clf()
    nx.draw_networkx(Node, pos=nx.spring_layout(Node, 25), alpha=1,
                     with_labels=False, node_size=100,
                         node_color="blue")
    canvas.draw()

ex = tk.Button(root, text="Update", command=lambda: Add())
ex.pack(side="bottom")

root.mainloop()
