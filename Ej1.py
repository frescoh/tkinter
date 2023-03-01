""" 
Ejercicio 1
Escribir una GUI con un botón con la leyenda “Mostrar fecha” y que al presionarlo
muestre por consola la fecha del día.

"""

import tkinter as tk
from tkinter import ttk
import datetime as dt

class Ej1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 1")
        self.geometry("300x300")
        self.boton = ttk.Button(self, text="Mostrar fecha", command=self.mostrar_fecha)
        self.boton.pack()
        self.mainloop()

    def mostrar_fecha(self):
        print("Fecha del día", dt.datetime.now())
        


root = Ej1()
