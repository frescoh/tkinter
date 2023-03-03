# ventanas_multiples.py
import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
 def __init__(self, parent):
    super().__init__(parent, padding=(20))
    self.parent = parent  # guardamos una referencia de la ventana ppal
    parent.title("Ventana Principal")
    parent.geometry("400x200+100+100")
    self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
    parent.columnconfigure(0, weight=1)
    parent.rowconfigure(0, weight=1)
    parent.resizable(False, False)
    ttk.Button(self, text="Abrir ventana", command=self.abrir_ventana).grid()

 def abrir_ventana(self):
    # creamos la ventana secundaria
    # como padre indicamos la ventana principal
    toplevel = tk.Toplevel(self.parent)
    # agregamos el frame (Secundaria) a la ventana (toplevel)
    Secundaria(toplevel).grid()


class Secundaria(ttk.Frame):
     def __init__(self, parent):
        super().__init__(parent, padding=(20))
        parent.title("Ventana Secundaria")
        parent.geometry("350x100-5+40")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        parent.resizable(False, False)
        ttk.Button(self, text="Cerrar", command=parent.destroy).grid()

root = tk.Tk()
App(root).grid()
root.mainloop()