import tkinter as tk
from tkinter import ttk, messagebox




class EJ3(ttk.Frame):

    def __init__(self, root):

        super().__init__(root, padding=(10))
        self.root = root
        root.title("EJ3")
        root.geometry("300x300")

        self.text = tk.StringVar()
    

        root.texto = ttk.Label(self, text="Ingrese un texto").grid(row=1, column=1)
        root.texto_obt = ttk.Entry(self, textvariable=self.text).grid(row=1, column=2)

        root.g_btn = ttk.Button(self, text="Guardar", command=self.guardar).grid(row=2, column=1)



    def guardar(self):
        self.texto = self.text.get()
        messagebox.showinfo("Mensaje", "El texto ingresado es: " + self.texto)

d = EJ3(tk.Tk())
d.grid()  # <--- SIN ESTO NO MUESTRA NADA EN LA VENTANA
d.mainloop()  
