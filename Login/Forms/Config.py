
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import Login.utilidades.generic as utl
from tkinter import ttk, messagebox

class config:
    
    
    def cambiarDireccionBdRrhh(self,direccion):
        resultado = messagebox.askquestion("ALERTA", "¿Quieres cambiar la ruta?")
        if resultado == "yes":
            direccion = direccion.replace("\\","/")
            nombre_archivo = './Login/utilidades/AppSetings.txt'
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
            lineas[0] = f'{{"Ruta bd RRHH": "{direccion}"}}\n'
            with open(nombre_archivo, 'w') as archivo:
                archivo.writelines(lineas)
                messagebox.showinfo("EXITO", "Se modifico correctamente la ruta")
        else:
            messagebox.showinfo("Sin Cambios", "no se modifico nada")
        self.ventana.destroy()
        
    def __init__(self) :
        self.ventana = tk.Tk() 
        self.ventana.title('Configuración del sistema')  
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        ancho = int(w * 0.4) 
        alto = int(h * 0.2)
        x = (w - ancho) // 2
        y = (h - alto) // 2

        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.ventana.config(bg='#ffcc00') 
        self.ventana.resizable(width=10, height=10) 
        self.ventana.iconbitmap("./Login/Imagenes/sombrero-de-graduacion.ico")
        frameForm =tk.Frame(self.ventana, height=700, bd=30, relief=tk.FLAT, bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameForm.columnconfigure([0,1], weight=1)
        frameForm.pack(side='top', fill=tk.BOTH) 
        etiquetaRuta = tk.Label(frameForm, text="Ruta BD rrhh: ", font=('Arial', 10, 'bold'),bg='#ffcc00')
        etiquetaRuta.grid(row=0, column=0)
        textoRuta = tk.Entry(frameForm, font=("Arial", 10), width=70)
        textoRuta.grid(row=0, column=1)
        textoRuta.insert(0, utl.LeerArchivoRrhh())
        frameForm1 =tk.Frame(self.ventana, height=70, bd=20,  bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameForm1.pack(side='bottom', fill=tk.X) 
        #Boton Guardar      
        guardar = tk.Button(frameForm1, text="Cambiar", font=("Arial", 14), bg= "#000000", bd=0, fg="#fff", command=lambda: self.cambiarDireccionBdRrhh(textoRuta.get()))
        guardar.pack(side= 'bottom', padx=20)
        
        
        
        
            
        self.ventana.mainloop()