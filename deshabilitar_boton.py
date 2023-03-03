# formulario.py
import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(10))
        self.parent = parent  # referencia a la ventana ppal
        parent.title("Ventana simple")

        self.boton = ttk.Button(self, text="deshabilitar",
                                padding=3, command=self.deshabilitar)
        self.boton.grid(row=10, column=3)
        # para ejecutar el btn al presionar enter
        parent.bind('<Return>', lambda e: self.boton.invoke())
        # btn_guardar.state(['!disabled']) # desabilita al boton
    def deshabilitar(self):
        self.boton.state(['disabled']) # desabilita al boton
        #boton.state(['!disabled']) # habilita al boton

    

root = tk.Tk()
App(root).grid()
root.resizable(False, False)  # evita que se pueda cambiar de tamaño la ventana
root.mainloop()
