import tkinter as tk 
from tkinter import ttk

class App(ttk.Frame):     
    def __init__(self, parent):         
        super().__init__(parent) 
        self.parent=parent
        parent.title('Trabajo Practico N°2')
        parent.geometry("800x600+100+100")
        parent.grid_propagate(10)
        parent.grid()
        
        ttk.Button(self,text='Terminar',command=lambda:parent.destroy()).grid(row=10, column=0)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
           
    

root = tk.Tk() 
App(root).grid()
root.mainloop() 