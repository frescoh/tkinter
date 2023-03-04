import tkinter as tk 
from tkinter import ttk
from datetime import datetime as dt

class App(ttk.Frame):     
    def __init__(self, parent):         
        super().__init__(parent) 
        self.parent=parent
        parent.title('Ejercicio 1')
        parent.geometry("300x200")
        parent.grid_propagate(10)
        parent.grid()
        ttk.Button(self, text="Mostrar Fecha", command=self.mensaje).grid()
        self.etiqueta=ttk.Label(self, text=' ', padding=5)
        self.etiqueta.grid()
        ttk.Button(self,text='Salir',command=lambda:parent.destroy()).grid(row=10, column=0)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
           
    def mensaje(self):
        mensaje=dt.now().strftime('%d/%m/%Y')  
        print(mensaje)
        self.etiqueta.config(text=mensaje)

root = tk.Tk() 
App(root).grid()
root.mainloop() 