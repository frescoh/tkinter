import tkinter as tk
from tkinter import ttk,messagebox
import math

class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        parent.title('Raiz Cuadrada')
        parent.geometry("500x200")
        parent.grid_propagate(10)
        parent.grid()
        self.numero=tk.StringVar()
        ttk.Label(self, text='Ingrese un numero:',padding=10).grid(row=1,column=1)
        self.entrada=ttk.Entry(self, textvariable=self.numero)
        self.entrada.grid(row=1, column=2)
        self.entrada.focus()
        self.entrada.bind('<Return>',self.raiz)
        ttk.Button(self,text='Calcular la raiz cuadrada',command=self.raiz).grid(row=2,column=3)
        ttk.Button(self,text='Salir',command=lambda:parent.destroy()).grid(row=10, column=2)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    def raiz(self,event=None):
        if self.numero.get()=='':
            messagebox.showwarning(message='Debe ingresar un numero', title='Cuidado')
        else:           
            try:
                raiz=math.sqrt(float(self.numero.get()))
                print(raiz)
            except ValueError:
                messagebox.showerror(message='Debe ingresar un numero', title='Error')
            finally:
                self.entrada.delete(0, tk.END)
                self.entrada.focus() 

root=tk.Tk()
App(root).grid()
root.mainloop()