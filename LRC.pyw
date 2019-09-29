import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

from LR import LR

def transformArray():
    xArray = np.array([])
    yArray = np.array([])

    x1 = x.get()
    y1 = y.get()

    x1 = x1.split(',')
    y1 = y1.split(',')
    
    print("Transform x{} to numpy array".format(x))
    for i in x1:
        xArray = np.append(xArray ,int(i))

    print(xArray, type(xArray))

    print("Transform y{} to numpy array".format(y))
    for i in y1:
        yArray = np.append(yArray ,int(i))
    
    print(yArray, type(yArray))

    #Graph
    LRCgraph(xArray, yArray)

"""GRAPH seccion code"""
def LRCgraph(xArray, yArray):
    reg = LR(xArray, yArray)    #New object Linear Regression
    reg.get_m_b()               #get m, b

    line = reg.m * reg.x + reg.b
    print(reg.b)

    #Label del titulo "Grafica"
    textGrafica = tk.Label(frame, text="GRAPH", font=("Helvetica", 16))
    textGrafica.grid(row=5, column=1, padx=5)

    graph = Figure(figsize=(5, 4), dpi=100)

    graph.add_subplot().grid()

    "plot Data"
    graph.add_subplot().plot(xArray, yArray, 'o', label="Data")
    "plot Linear Adjustment"
    graph.add_subplot().plot(xArray, line, color="red", label="Linear Adjustment")

    graph.add_subplot().legend()

    canvas = FigureCanvasTkAgg(graph, master=frame)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=6, column=1)


#Crea la ventana
window = tk.Tk()
window.resizable(False, False)

window.title("LRC")                        #Window name
window.iconbitmap('LRC.ico')               #icon

#Frame 1
frame = tk.Frame(window, width=500, height=600)
frame.pack()

#Label de titulo
title = tk.PhotoImage(file='title.png')
tk.Label(frame, image=title).grid(row=0, column=1, padx=5, pady=7)

"""DATA Seccion code"""
#Label del titulo "DATA"
textData = tk.Label(frame, text="DATA", font=("Helvetica", 16))
textData.grid(row=1, column=1, padx=5, sticky='w')

#Label del texto "X"
textX = tk.Label(frame, text="X", font=("Helvetica", 18))
textX.grid(row=2, column=0, padx=5, pady=5, sticky='e')

x = tk.StringVar()
entryX = tk.Entry(frame, textvariable=x)#, state="readonly")
entryX.grid(row=2, column=1, pady=5, sticky='w')

#Label del texto "Y"
textY = tk.Label(frame, text="Y", font=("Helvetica", 18))
textY.grid(row=3, column=0, padx=5, pady=5, sticky='e')

y = tk.StringVar()
entryY = tk.Entry(frame, textvariable=y)#, state="readonly")
entryY.grid(row=3, column=1, pady=5, sticky='w')

"""Button RLC"""
buttonRLC = tk.Button(frame, text="OK", command=transformArray)
buttonRLC.grid(row=4, column=1, padx=5, pady=5)

"""window mainloop"""
window.mainloop()