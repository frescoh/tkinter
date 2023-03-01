def saludar():
    print("Hola mundo")

# hola_mundo.py
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
frame = ttk.Frame(root).grid()
ttk.Button(frame, text="Hola", command=lambda: print("mundo")).grid()
ttk.Button(frame, text="Chau", command=saludar).grid()
root.mainloop()

