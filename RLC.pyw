import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

from Regresion import Regresion

def transformArray():
    global x,y

    xArray = np.array([])
    yArray = np.array([])

    x = x.get()
    y = y.get()

    x = x.split(',')
    y = y.split(',')
    
    print("Transform x{} to numpy array".format(x))
    for i in x:
        xArray = np.append(xArray ,int(i))

    print(xArray, type(xArray))

    print("Transform y{} to numpy array".format(y))
    for i in y:
        yArray = np.append(yArray ,int(i))
    
    print(yArray, type(yArray))

"""GRAPH seccion code"""
def rlgraph():
    #Label del titulo "Grafica"
    textGrafica = tk.Label(frame, text="GRAPH", font=("Helvetica", 16))
    textGrafica.grid(row=5, column=1, padx=5)

    graph = Figure(figsize=(5, 4), dpi=100)

    arrayX, arrayY = 0, 0
    Recta = 0

    graph.add_subplot().grid()

    graph.add_subplot().plot(arrayX, arrayY, 'o', label="Datos")
    graph.add_subplot().plot(Recta , color="red", label="Ajuste")
    graph.add_subplot().legend()

    canvas = FigureCanvasTkAgg(graph, master=frame)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=6, column=1)


#Crea la ventana
window = tk.Tk()
window.resizable(False, False)

window.title("RLC")                        #Window name
window.iconbitmap('RLC.ico')               #icon

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