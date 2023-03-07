import tkinter as tk 
from tkinter import ttk, messagebox  

class App(ttk.Frame):     
    def __init__(self, parent):         
        super().__init__(parent, padding=10) 
        self.parent=parent
        parent.title('Ventana Emergente')
        parent.geometry("300x200")
        parent.grid_propagate(10)
        parent.grid()
        ttk.Button(self, text="Informacion", command=self.mensaje_info).grid(column=0,row=0)
        ttk.Button(self, text="Advertencia", command=self.mensaje_adv).grid(column=1,row=0)
        ttk.Button(self,text='Salir',command=lambda:parent.destroy()).grid(row=10, column=2)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    @staticmethod     
    def mensaje_info(msj='Este es un mensaje de información'):
        messagebox.showinfo(message=msj,title='Info')
        

    @staticmethod     
    def mensaje_adv(msj='Este es un mensaje de advertencia'):
        messagebox.showwarning(message=msj,title='Cuidado!')
    
root = tk.Tk() 
App(root).grid()
root.mainloop() 