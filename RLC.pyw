import tkinter as tk

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
tk.Label(frame, image=title).grid(row=0, column=0, padx=5, pady=7, columnspan=3)

"""DATA Seccion code"""
#Label del titulo "DATA"
textData = tk.Label(frame, text="DATA", font=("Helvetica", 16))
textData.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

#Label del texto "X"
textX = tk.Label(frame, text="X", font=("Helvetica", 18))
textX.grid(row=2, column=0, padx=5, pady=5)

#Label del texto "Y"
textY = tk.Label(frame, text="Y", font=("Helvetica", 18))
textY.grid(row=2, column=1, padx=5, pady=5)

"""GRAPH seccion code"""
#Label del titulo "Grafica"
textGrafica = tk.Label(frame, text="GRAPH", font=("Helvetica", 16))
textGrafica.grid(row=1, column=2, padx=5, pady=5)

window.mainloop()