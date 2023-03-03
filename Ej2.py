# Ej2 con TKINTER  del Trabajo Practio 1
# Guillermo Villagra

# Ejercicio 2
# Escribir una GUI con dos botones, uno con la leyenda “Info” y otro con la leyenda
# “Advertencia”. Al hacer click a uno, debe mostrar una ventana emergente de
# información con el mensaje que Ud. quiera. Y el otro debe mostrar una ventana
# emergente de advertencia, también, con el mensaje que Ud. quiera.
import tkinter as tk
from tkinter import ttk, messagebox

class EJ2(ttk.Frame):
    """
    Clase de dos botones que muestra un mensaje de advertencia
    Args:
        ttk (_type_): ttk inter de tkinter
    """
    def __init__(self, root):

        """parametros de lanza de la ventana y el botn
        """        
        super().__init__(root,)
        self.root = root
        root.title("EJ2")
        root.geometry("300x300")

        #botnes de advertencia e info
        root.btn_info = ttk.Button(root, text="Info", command=self.info).grid(column=0, row=0)
        root.btn_advertencia = ttk.Button(root, text="Advertencia", command=self.advertencia).grid(column=5,row=0)


    def advertencia(self):
        """ muestra un mensaje de advertencia en una ventana nueva la cual se cierra al presionar el boton ok
        """   
        # esto devuelve true o false si se presiona el boton ok dado caso una vez echo click en el ok la misma cierra la ventana de advertencia creada anteriromente
        messagebox.showwarning("Advertencia", "Diste click en el boton Advertencia")

    def info(self):
        """ 
        muestra un mensaje de advertencia en una ventana nueva la cual se cierra al presionar el boton ok
        """        
        messagebox.showinfo("Info", "Diste click en el boton Info")


d = EJ2(tk.Tk())
d.mainloop()
