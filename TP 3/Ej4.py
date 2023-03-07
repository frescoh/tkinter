# Nicolas Gonza

# Ejercicio 4
# Mejorar el ejercicio anterior revisando si la entrada de texto contiene algo antes de
# mostrar. Si no contiene nada (la cadena vacía) mostrar una ventana emergente de
# información 

import tkinter as tk
from tkinter import ttk,messagebox

class Entrada(ttk.Frame):
    """ Clase que permite la entrada de texto y guardarlo
    """
    def __init__(self, parent):
        """Construct"""
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
        if self.texto.get() != "":
            print(f"Guardado los datos: {self.texto.get()}")
            self.parent.destroy()
        else:
            messagebox.showwarning("Falta texto!!!", "Debe ingresar un texto")
        

root= tk.Tk()
Entrada(root).grid()
root.resizable(False, False)
root.mainloop()