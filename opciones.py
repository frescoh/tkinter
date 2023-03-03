# opciones.py
import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.boton = ttk.Button(self, text="Cambiar texto",
                                padding=3,
                                command=self.cambiar,
                                width=50)
        self.boton.grid()
        print(self.boton)
    def cambiar(self):
        if self.boton["width"] == 50:  # accedemos a la opcion
            self.boton["width"] = 100  # cambiamos la opcion
            self.boton["text"] = "Volver a cambiar"
        else:
            self.boton["width"] = 50
            self.boton["text"] = "Cambiar texto"

root = tk.Tk()
App(root).grid()
root.mainloop()
