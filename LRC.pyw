import tkinter as tk

#Crea la ventana
window = tk.Tk()
window.resizable(False, False)

window.title("LRC")     #Titulo de la vemtana
window.iconbitmap('RLC.ico')                    #Se pone el icono

#Frame 1
frame = tk.Frame(window, width=500, height=600)
frame.pack()

#Label de titulo
title = tk.Label(frame, text="Imagen que va a contener el titulo y el logo")
title.grid(row=1, column=1)

window.mainloop()