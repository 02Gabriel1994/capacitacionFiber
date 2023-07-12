import tkinter as tk
from tkinter.font import BOLD
import Login.utilidades.generic as utl



class masterPanel:
    
    def __init__(self) :
        self.ventana = tk.Tk() # crea una instancia de la clase Tk de la biblioteca Tkinter y se asigna a self.ventana. Esto crea una ventana principal para la aplicación.
        self.ventana.title('Capaciteichon') # Aquí se establece el título de la ventana como "master panel" utilizando el método .title().
        w,h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        #w,h = self.ventana.winfo_screenmmwidth(),self.ventana.winfo_screenheight() # En esta línea, se obtiene el ancho (w) y la altura (h) de la pantalla en la que se ejecuta la ventana utilizando los métodos .winfo_screenwidth() y .winfo_screenheight() respectivamente.
        self.ventana.geometry("%dx%d+0+0" % (w,h)) # se establece la geometría de la ventana utilizando el método .geometry(). %dx%d se utiliza como una cadena de formato para especificar el tamaño de la ventana como ancho (w) y altura (h). El +0+0 indica que la ventana se ubicará en la posición superior izquierda de la pantalla.
        self.ventana.config(bg='#fcfcfc') # se configura el color de fondo de la ventana como '#fcfcfc' utilizando el método .config(). El código de color '#fcfcfc' representa un tono de gris claro.
        self.ventana.resizable(width=0, height=0) # Aquí se establece la capacidad de redimensionamiento de la ventana a width=0 y height=0, lo que significa que la ventana no se podrá redimensionar en ancho ni en alto. Esto evita que el usuario pueda cambiar el tamaño de la ventana manualmente.
        logo  = utl.leerImagen("./Login/Imagenes/isolino graduado.png",(200,200))
        label = tk.Label(self.ventana, image=logo, bg='#3a7ff6')
        label.place(x=0,y=0,relwidth=1,relheight=1)
        self.ventana.mainloop()
        
        
        
