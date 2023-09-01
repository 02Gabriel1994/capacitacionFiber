import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from Login.Forms.master import masterPanel
from Login.Forms.Capacitaciones import RCapacitacion
from Login.utilidades.generic import acercaDe
from Login.Forms.Config import config

class principal:
    def abrirRmaster(self):
        self.ventana.withdraw()
        self.masterPanel = masterPanel(self.ventana, self)
        
    def abrirRCapacitacion(self):
        self.ventana.withdraw()
        self.RCapacitacion = RCapacitacion(self.ventana, self)
        self.RCapacitacion.mainloop()
    def cerrarSesion(self):
        self.ventana.destroy()
        
    
    def __init__(self, root) :
        self.ventana = root
        self.ventana.title('MENU PRINCIPAL') 
        menu = Menu (self.ventana)
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        ancho = int(w * 0.8) 
        alto = int(h * 0.8)
        x = (w - ancho) // 2
        y = (h - alto) // 2

        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.ventana.config(bg='#ffcc00', menu=menu) 
        self.ventana.resizable(width=10, height=10) 
        self.ventana.iconbitmap("./Login/Imagenes/sombrero-de-graduacion.ico")
        sesion= Menu(menu, tearoff=0)
        sesion.add_command(label="Configuración", command=lambda: config())
        sesion.add_command(label="Cerrar Sesión", command=self.cerrarSesion)
        sesion.add_separator()
        sesion.add_command(label="Acerca de", command=lambda: acercaDe())
        menu.add_cascade(label="Sesión", menu= sesion)
        frameForm = tk.Frame(self.ventana, height=70, bd=20, bg='#ffcc00', relief="solid")
        frameForm.pack(expand=True, fill=tk.BOTH, pady=(self.ventana.winfo_screenheight() - alto) // 2)

        imagen1 = Image.open("./Login/Imagenes/rPersonal.jpg")
        imagen1 = imagen1.resize((150, 150), Image.BICUBIC)
        imagen1 = ImageTk.PhotoImage(imagen1)

        imagen2 = Image.open("./Login/Imagenes/isolino graduado.png")
        imagen2 = imagen2.resize((150, 150), Image.BICUBIC)
        imagen2 = ImageTk.PhotoImage(imagen2)
        imagen3 = Image.open("./Login/Imagenes/asistencia.jpg")
        imagen3 = imagen3.resize((150, 150), Image.BICUBIC)
        imagen3 = ImageTk.PhotoImage(imagen3)
        imagen4 = Image.open("./Login/Imagenes/informes.jpg")
        imagen4 = imagen4.resize((150, 150), Image.BICUBIC)
        imagen4 = ImageTk.PhotoImage(imagen4)
        
        imagen5 = Image.open("./Login/Imagenes/usuario.png")
        imagen5 = imagen5.resize((150, 150), Image.BICUBIC)
        imagen5 = ImageTk.PhotoImage(imagen5)

        boton_imagen1 = ttk.Button(frameForm, image=imagen1, command=self.abrirRmaster)
        boton_imagen1.pack(side=tk.LEFT, padx=10) 

        boton_imagen2 = ttk.Button(frameForm, image=imagen2, command=self.abrirRCapacitacion)
        boton_imagen2.pack(side=tk.LEFT, padx=10) 
        boton_imagen3 = ttk.Button(frameForm, image=imagen3) #command=abrir_segunda_ventana)
        boton_imagen3.pack(side=tk.LEFT, padx=10) 
        boton_imagen4 = ttk.Button(frameForm, image=imagen4) #, command=abrir_segunda_ventana)
        boton_imagen4.pack(side=tk.LEFT, padx=10) 
        
        boton_imagen5 = ttk.Button(frameForm, image=imagen5) #, command=abrir_segunda_ventana)
        boton_imagen5.pack(side=tk.LEFT, padx=10) 
        frameForm2 =tk.Frame(frameForm, height=7000, bd=2, relief=tk.SOLID, bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameForm2.pack(side='top', fill=tk.BOTH) 
        etiqueta = tk.Label(frameForm2, text="Aqui va a ir todas las capacitaciones pendientes por ejecutar: ", font=('Arial', 10, 'bold'),bg='#ffcc00')
        etiqueta.pack(side= 'left')
        self.ventana.mainloop()

# if __name__ == "__main__":
#     app = principal()


# Resto del código sin cambios
