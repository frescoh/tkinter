# Trabajo Práctico 2

Las interfaces solicitadas en este Trabajo Práctico deben ser programadas aplicando POO.  
  

### **Ejercicio 1**

Escribir una GUI con una ventana de un tamaño de 800x600 pixeles y que se posicione a 100 pixeles del borde izquierdo y 100 pixeles del borde superior de la pantalla. Como título, la ventana debe tener el texto, "Trabajo Práctico Nº2".  
  
La ventana debe contener solo un botón con la leyenda "Terminar" y este debe terminar la ejecución del programa.    
  

```python
import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.geometry("600x400+100+100")
        parent.title("Trabajo Práctico Nº2")
        
        ttk.Button(self, text="Terminar",
                   command=parent.destroy).grid(padx=10, pady=10)

root = tk.Tk()
App(root).grid()
root.mainloop()
```

### **Ejercicio 2**

Escribir una GUI que tenga una entrada de texto y un botón con la leyenda "Cambiar título". El botón debe tomar lo que el usuario haya escrito en la entrada y colocarlo como título de la ventana. Si no hay nada escrito en la entrada de texto debe mostrar una ventana emergente informando al usuario.  
  
#### Opcional

Marcar al botón como predeterminado, y hacer que también se accione cuando usuario presione la tecla Enter.  
  

```python
import tkinter as tk
from tkinter import ttk, messagebox

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.window = parent
        self.entrada = tk.StringVar()
    
        ttk.Entry(self, width=60,
                  textvariable=self.entrada).grid(row=1, column=1,
                                                  padx=10, pady=10)
        boton = ttk.Button(self, text="Cambiar título",
                           default="active",
                           command=self.modificar_titulo)
        boton.grid(row=1, column=2, padx=10, pady=10)
        parent.bind("<Return>", lambda e: boton.invoke())
    
    def modificar_titulo(self):
        texto = self.entrada.get()
        if texto:
            self.window.title(texto)
        else:
            messagebox.showinfo(message="Debe escribir algo >.<")

root = tk.Tk()
App(root).grid()
root.mainloop()
```

### **Ejercicio 3**

Escribir una GUI que tenga un botón con la leyenda "Iniciar sesión" que al accionarlo abra otra ventana, sobre la anterior, que sirva como inicio de sesión (log-in). Debe tener un formulario que solicite al usuario un nombre de usuario y contraseña, y dos botones, para "Iniciar sesión" o "Cancelar" la acción.  
  
Si el inicio de sesión es correcto debe destruir la ventana de inicio de sesión y mostrar una etiqueta en la ventana principal con el mensaje "Bienvenido". El botón para iniciar sesión debe cambiar de leyenda y decir "Cerrar sesión".  
  
Si el inicio de sesión no es correcto debe permitirle al usuario volver a intentarlo.  
  
Si el usuario presiona el botón de "Cancelar" solo debe cerrarse la ventana.  
  
La lógica para saber si el inicio de sesión es correcto o no puede implementarla como Ud. desee.  
  
Ayuda: puede mantener un atributo en la ventana principal que indique si la sesión está activa).  
  
```python
import tkinter as tk
from tkinter import ttk, messagebox

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.window = parent
        self.window.title("Ejercicio 3")
        self.window.geometry("400x200+400+200")
        self.sesion = False
    
        self.etiqueta = ttk.Label(text="").grid(row=1, column=1, padx=3, pady=3)
        self.boton = ttk.Button(self, text="Iniciar sesión",
                                default="active",
                                command=self.login)
        self.boton.grid(row=1, column=2, padx=10, pady=10)
    
    def login(self):
        if self.sesion:
            self.logout()
        else:
            ventana_login = tk.Toplevel(self.window)
            Login(ventana_login, self).grid()
    
    def login_correcto(self):
        self.boton["text"] = "Cerrar sesión"
        self.sesion = True
    
    def logout(self):
        self.boton["text"] = "Iniciar sesión"
        self.sesion = False

class Login(ttk.Frame):
    def __init__(self, parent, main_window):
        super().__init__(parent, padding=10)
        self.main_window = main_window
        self.window = parent
        self.window.title("Iniciar sesión")
        self.usuario = tk.StringVar()
        self.passw = tk.StringVar()
        
        ttk.Label(self, text="Nombre de usuario", padding=3).grid(row=1, column=1)
        ttk.Entry(self, textvariable=self.usuario).grid(row=1, column=2)
        ttk.Label(self, text="Contraseña", padding=3).grid(row=2, column=1)
        ttk.Entry(self, textvariable=self.passw, show="*").grid(row=2, column=2)
        btn_guardar = ttk.Button(self, text="Iniciar", command=self.iniciar_sesion)
        btn_cancelar = ttk.Button(self, text="Cancelar", command=self.window.destroy)
        btn_cancelar.grid(row=10, column=2)
        btn_guardar.grid(row=10, column=3)
    
    def iniciar_sesion(self):
        if True:
            self.main_window.login_correcto()
        self.window.destroy()

root = tk.Tk()
App(root).grid()
root.mainloop()
```