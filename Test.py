from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Hello")
frame = Frame(root)
frame.pack()

fig = plt.figure()
canvas = FigureCanvasTkAgg(fig, frame)
Node = nx.Graph()

Node.add_nodes_from(range(1, 6))
Node.add_edge(1, 3)
Node.add_edge(1, 2)
Node.add_edge(1, 4)
Node.add_edge(3, 2)





root.mainloop()