import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.parent=parent
        parent.title('Ingreso')
        parent.geometry("300x200")
        parent.grid_propagate(10)
        parent.grid()
        self.texto= tk.StringVar()
        self.entrada=ttk.Entry(self, textvariable=self.texto)
        self.entrada.grid(row=1, column=2) 
        self.entrada.focus()
        self.entrada.bind('<Return>',self.mostrar)
        ttk.Button(self,text='Mostrar',command=self.mostrar).grid(row=1, column=3)
        ttk.Button(self,text='Salir',command=lambda:parent.destroy()).grid(row=10, column=3)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        

    def mostrar(self,event=None):
        texto=self.texto.get()
        print(texto)
        self.entrada.delete(0, tk.END)
        self.entrada.focus()
        

root=tk.Tk()
App(root).grid()
root.mainloop()