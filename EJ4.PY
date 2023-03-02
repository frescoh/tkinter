from math import sqrt
import tkinter as tk
from tkinter import ttk, messagebox




class EJ3(ttk.Frame):

    def __init__(self, root):

        super().__init__(root, padding=(10))
        self.root = root
        root.title("EJ3")
        root.geometry("300x300")

        self.text = tk.IntVar()
    

        root.texto = ttk.Label(self, text="Ingrese un Numero").grid(row=1, column=1)
        root.texto_obt = ttk.Entry(self, textvariable=self.text).grid(row=1, column=2)

        root.g_btn = ttk.Button(self, text="Calcular Raiz Cuadrada", command=self.raiz).grid(row=2, column=1)



    def raiz(self):
        self.texto = self.text.get()
        self.raiz = float(self.texto)**(1/2) # transofrma el texto a float y calcula la raiz cuadrada
        messagebox.showinfo("Mensaje", "La raiz cuadrada de " + str(self.texto) + " es: " + str(self.raiz))

    

    
d = EJ3(tk.Tk())
d.grid()  # <--- SIN ESTO NO MUESTRA NADA EN LA VENTANA
d.mainloop()  
