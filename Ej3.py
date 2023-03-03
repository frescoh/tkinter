# Nicolas Gonza

# Ejercicio 3
# Escribir una GUI con una entrada de texto y un botón con la leyenda “Mostrar”. Al hacer
# click en el botón se debe mostrar el contenido de la entrada de texto por consola.
import tkinter as tk
from tkinter import ttk

class Entrada(ttk.Frame):
    """ Clase que permite la entrada de texto y guardarlo
    """
    def __init__(self, parent):
        super().__init__(parent, padding=(10))
        self.parent= parent
        parent.title("Formulario Simple")

        self.texto= tk.StringVar()
        ttk.Label(self, text= "Ingrese Texto", padding=3).grid(row=1, column= 1)
        ttk.Entry(self, textvariable= self.texto).grid(row= 1, column= 2)
        btn_guardar= ttk.Button(self, text="Guardar",padding=3, command= self.guardar)
        btn_guardar.grid(row=3, column=3)

        parent.bind('<Return>', lambda e: btn_guardar.invoke())
    
    def guardar(self):
        print(f"Guardado los datos: {self.texto.get()}")
        self.parent.destroy()

root= tk.Tk()
Entrada(root).grid()
root.resizable(False, False)
root.mainloop()