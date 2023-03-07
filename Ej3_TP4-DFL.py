import tkinter as tk 
from tkinter import ttk,messagebox

class App(ttk.Frame):     
    def __init__(self, parent):         
        super().__init__(parent) 
        self.parent=parent
        parent.title('Ventana Principal')
        parent.geometry("300x200+100+100")
        parent.grid_propagate(10)
        parent.grid()
        self.etiqueta1=ttk.Label(self, text='',padding=10)
        self.etiqueta1.grid()
        self.boton_iniciar=ttk.Button(self,text='Iniciar Sesion',command=self.login)
        self.boton_iniciar.grid(row=10, column=0)
        self.boton_iniciar.focus()
        self.boton_iniciar.bind('<Return>',self.login)
        self.boton_iniciar.bind('<Escape>',lambda event: self.parent.destroy())
        self.etiqueta2=ttk.Label(self, text='Sesion Inactiva',padding=10)
        self.etiqueta2.grid()
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    
    def login(self,event=None):
        if self.boton_iniciar.cget('text')=='Iniciar Sesion':
            toplevel=tk.Toplevel(self.parent)
            toplevel.bind('<Escape>', lambda event: toplevel.destroy())
            Secundaria(toplevel,self.etiqueta1,self.etiqueta2,self.boton_iniciar).grid()
        else:
            self.boton_iniciar.configure(text='Iniciar Sesion')
            self.etiqueta1.configure(text='')
            self.etiqueta2.configure(text='Sesion Inactiva')


class Secundaria(ttk.Frame):     
    def __init__(self, parent,etiqueta1,etiqueta2,boton):         
        super().__init__(parent) 
        self.parent=parent
        self.etiqueta1=etiqueta1
        self.etiqueta2=etiqueta2
        self.boton=boton
        parent.title('Ventana LogIn')
        parent.geometry("600x400")
        parent.grid_propagate(10)
        parent.grid()
        self.usuario=tk.StringVar()
        self.password=tk.StringVar()
        ttk.Label(self, text='Usuario: ', padding=3).grid(row=1,column=1)
        self.entrada1=ttk.Entry(self, textvariable=self.usuario)
        self.entrada1.grid(row=1,column=2)
        self.entrada1.focus()
        self.entrada1.bind('<Return>', self.cambia_foco)
        ttk.Label(self, text='Contraseña', padding=3).grid(row=2,column=1)
        self.entrada2=ttk.Entry(self, textvariable=self.password,show='*')
        self.entrada2.grid(row=2,column=2)
        self.entrada2.bind('<Return>', self.iniciar)
        ttk.Button(self,text='Iniciar Sesion',command=self.iniciar).grid(row=10)
        ttk.Button(self,text='Cancelar',command=parent.destroy).grid(row=10,column=3)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    def iniciar(self,event=None):
        if self.usuario.get()=='usuario' and self.password.get()=='password':
            self.etiqueta1.configure(text='Bienvenido')
            self.etiqueta2.configure(text='Sesion Activa')
            self.boton.configure(text='Cerrar Sesion')
            self.parent.destroy()
        else:
            messagebox.showerror(message='Usuario o contraseña incorrectos', title='Error')
            self.entrada1.delete(0, tk.END)
            self.entrada2.delete(0, tk.END)
            self.entrada1.focus()

    def cambia_foco(self,event=None):
        self.entrada2.focus()
           
    

root = tk.Tk() 
App(root).grid()
root.mainloop() 