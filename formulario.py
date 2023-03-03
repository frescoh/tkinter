# formulario.py
import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(10))
        self.parent = parent  # referencia a la ventana ppal
        parent.title("Fomulario simple")

        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.email = tk.StringVar()

        ttk.Label(self, text="Nombre", padding=3).grid(row=1, column=1)
        ttk.Entry(self, textvariable=self.nombre).grid(row=1, column=2)
        ttk.Label(self, text="Apellido", padding=3).grid(row=2, column=1)
        ttk.Entry(self, textvariable=self.apellido).grid(row=2, column=2)
        ttk.Label(self, text="email", padding=3).grid(row=3, column=1)
        ttk.Entry(self, textvariable=self.email).grid(row=3, column=2)
        btn_guardar = ttk.Button(self, text="Guardar",
                                padding=3, command=self.guardar)
        btn_guardar.grid(row=10, column=3)
        # para ejecutar el btn al presionar enter
        parent.bind('<Return>', lambda e: btn_guardar.invoke())
    def guardar(self):
        print(f"Guardados los datos: {self.nombre.get()}, {self.apellido.get()}, {self.email.get()} ")
        self.parent.destroy()  # terminamos el programa al destruir la ventana ppal

    

root = tk.Tk()
App(root).grid()
root.resizable(False, False)  # evita que se pueda cambiar de tamaño la ventana
root.mainloop()
