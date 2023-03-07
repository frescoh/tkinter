import tkinter as tk
from tkinter import ttk,messagebox

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.parent=parent
        parent.title('Ejercicio 2')
        parent.geometry("300x200")
        parent.grid_propagate(10)
        parent.grid()
        self.texto= tk.StringVar()
        self.entrada=ttk.Entry(self, textvariable=self.texto)
        self.entrada.grid(row=1, column=2) 
        self.entrada.focus()
        self.entrada.bind('<Return>',self.cambiar)
        boton_pred=ttk.Button(self,text='Cambiar Titulo',command=self.cambiar)
        boton_pred.grid(row=1, column=3)
        boton_pred.state(["pressed"])
        boton_pred.bind('<Return>',self.cambiar)
        ttk.Button(self,text='Salir',command=lambda:parent.destroy()).grid(row=10, column=3)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    def cambiar(self,event=None):
        if self.parent.title()!='':
            texto=self.texto.get()
            self.parent.title(texto)
            self.entrada.delete(0, tk.END)
            self.entrada.focus()
        else:
            messagebox.showwarning(message='El titulo esta vacio',title='Cuidado!')

root=tk.Tk()
App(root).grid()
root.mainloop()