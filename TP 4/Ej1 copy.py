import tkinter as tk
from tkinter import ttk


class GUI:
    def __init__(self):
        self.principal=tk.Tk()
        self.principal.title('Trabajo Práctico Nº2')
        self.principal.geometry("800x600+100+100")
        
        self.frame= tk.Frame(self.principal)
        self.frame.grid()
        self.principal.grid_propagate(10)
        self.boton= ttk.Button(self.frame,text='Terminar',command=self.principal.destroy)
        self.boton.grid(column=3,row=10)
        self.principal.grid_rowconfigure(0, weight=1)
        self.principal.grid_columnconfigure(0, weight=1)
        
    def iniciar(self):
        self.principal.mainloop()


g= GUI()
g.iniciar()