import tkinter as tk
from tkinter import ttk

class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        parent.title('Trabajo Práctico Nº2')
        parent.geometry("800x600")
        ttk.Button(self,text='Terminar',command=parent.destroy).grid(row=10, column=2)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

root=tk.Tk()
App(root).grid()
root.mainloop()