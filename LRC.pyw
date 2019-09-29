import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

from LR import LR

def transformArray():
    #functions Error
    def xyDiferent_Error():
        tk.messagebox.showwarning(title="Number of items error", message="""The number of elements of x and y cannot be different!
The number of elements must be greater than 1!""")

    def character_Error():
        tk.messagebox.showwarning(title="Type Error", message="You can't use characters")

    xArray = np.array([])
    yArray = np.array([])

    x1 = x.get()
    y1 = y.get()

    x1 = x1.split(',')
    y1 = y1.split(',')
    
    if len(x1) == len(y1) and len(x1) != 1:
        print("Transform x{} to numpy array".format(x))
        try:
            for i in x1:
                xArray = np.append(xArray ,float(i))

            print(xArray, type(xArray))

            print("Transform y{} to numpy array".format(y))
            for i in y1:
                yArray = np.append(yArray ,float(i))
        
            print(yArray, type(yArray))

            #Graph
            LRCgraph(xArray, yArray)
        except ValueError:
            character_Error()

    else:
        xyDiferent_Error()

"""GRAPH seccion code"""
def LRCgraph(xArray, yArray):
    reg = LR(xArray, yArray)    #New object Linear Regression
    reg.get_m_b()               #get m, b

    line = reg.m * reg.x + reg.b
    print(reg.b)

    #Label "Graph"
    textGrafica = tk.Label(frame, text="GRAPH", font=("Helvetica", 16))
    textGrafica.grid(row=5, column=1, padx=5)
    graph = Figure(figsize=(3, 3), dpi=100)
    graph.add_subplot().grid()

    #m y b data
    

    #plot Data
    graph.add_subplot().plot(xArray, yArray, 'o', label="Data")
    #plot Linear Adjustment"
    graph.add_subplot().plot(xArray, line, color="red", label="Linear Adjustment")

    graph.add_subplot().legend()

    canvas = FigureCanvasTkAgg(graph, master=frame)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, rowspan=6, sticky='w')

    """Data y, m, b"""
    #y = mx + b
    lineOut = tk.StringVar()
    lineOut.set("y = "+ str(reg.m) + "x + " + str(reg.b))

    textE = tk.Label(frame, text="Linear Adjustment", font=("Helvetica", 10))
    textE.grid(row=6, column=2, padx=5, sticky='S')
    entryE = tk.Entry(frame, textvariable=lineOut, state="readonly", justify='center',font='large_font')
    entryE.grid(row=7, column=2, padx=5, pady=5)

    #m
    mOut = tk.StringVar()
    mOut.set("m = " + str(reg.m))

    textm = tk.Label(frame, text="m", font=("Helvetica", 10))
    textm.grid(row=8, column=2, padx=5, sticky='S')
    entryE = tk.Entry(frame, textvariable=mOut, state="readonly", justify='center',font='large_font')
    entryE.grid(row=9, column=2, padx=5, pady=5)


    #b
    bOut = tk.StringVar()
    bOut.set("b = " + str(reg.b))

    textm = tk.Label(frame, text="b", font=("Helvetica", 10))
    textm.grid(row=10, column=2, padx=5, sticky='S')
    entryE = tk.Entry(frame, textvariable=bOut, state="readonly", justify='center',font='large_font')
    entryE.grid(row=11, column=2, padx=5, pady=5)


"""GUI"""

#Create window
window = tk.Tk()
window.resizable(False, False)

window.title("LRC")                        #Window name
window.iconbitmap('images/LRC.ico')               #icon

#Create menu
#Functions menu
def quit():
    window.quit()     # stops mainloop
    window.destroy()

def howToUse():
    tk.messagebox.showinfo(message="""Enter the data of x and y using a "," for each item
Example:
1,2,3.2,4,5.7
Notes:
    -The number of elements of x and y cannot be different
    -The number of elements must be greater than 1""", title="How to use")

def codeInfo():
    import webbrowser
    webbrowser.open("https://github.com/Nyasper/LinearRegressionCalulator")

menubar = tk.Menu(window)
window.config(menu=menubar)

fileMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Exit", command=quit)

helpMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="How to use",command=howToUse)

infoMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Info", menu=infoMenu)
infoMenu.add_command(label="Code in GitHub", command=codeInfo)

#Frame 1
frame = tk.Frame(window, width=500, height=600)
frame.pack()

#Label de titulo
title = tk.PhotoImage(file='images/title.png')
tk.Label(frame, image=title).grid(row=0, column=0, columnspan=3, padx=5, pady=7)

"""DATA Seccion code"""
#Label del titulo "DATA"
textData = tk.Label(frame, text="DATA", font=("Helvetica", 16))
textData.grid(row=1, column=1, padx=5)

#Label del texto "X"
textX = tk.Label(frame, text="X", font=("Helvetica", 18))
textX.grid(row=2, column=0, padx=5, pady=5, sticky='e')

x = tk.StringVar()
entryX = tk.Entry(frame, textvariable=x)#, state="readonly")
entryX.grid(row=2, column=1, pady=5)

#Label del texto "Y"
textY = tk.Label(frame, text="Y", font=("Helvetica", 18))
textY.grid(row=3, column=0, padx=5, pady=5, sticky='e')

y = tk.StringVar()
entryY = tk.Entry(frame, textvariable=y)#, state="readonly")
entryY.grid(row=3, column=1, pady=5)

"""Button RLC"""
buttonRLC = tk.Button(frame, text="OK", command=transformArray)
buttonRLC.grid(row=4, column=1, padx=5, pady=5)

"""window mainloop"""
window.mainloop()