# Ej2 con TKINTER  del Trabajo Practio 1
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
        root.btn_info = ttk.Button(root, text="Info", command=self.info).grid()
        root.btn_info = ttk.Button(root, text="Advertencia", command=self.advertencia).grid()


    def advertencia(self):
        """ muestra un mensaje de advertencia en una ventana nueva la cual se cierra al presionar el boton ok
        """        
        ventana = tk.Toplevel(self.root)
        ventana.title("Advertencia")
        # esto devuelve true o false si se presiona el boton ok dado caso una vez echo click en el ok la misma cierra la ventana de advertencia creada anteriromente
        if messagebox.showwarning("Advertencia", "Diste click en el boton Advertencia"):
            ventana.destroy()
    
    def info(self):
        """ 
        muestra un mensaje de advertencia en una ventana nueva la cual se cierra al presionar el boton ok
        """        
        ventana_nueva = tk.Toplevel(self.root)
        ventana_nueva.title("Info")
        if messagebox.showinfo("Info", "Diste click en el boton Info"):
            ventana_nueva.destroy()


d = EJ2(tk.Tk())
d.mainloop()


