import tkinter as tk
from tkinter.font import BOLD
import Login.utilidades.generic as utl



class masterPanel:
    
    def __init__(self) :
        self.ventana = tk.Tk() # crea una instancia de la clase Tk de la biblioteca Tkinter y se asigna a self.ventana. Esto crea una ventana principal para la aplicación.
        self.ventana.title('Capaciteichon') # Aquí se establece el título de la ventana como "master panel" utilizando el método .title().
        w,h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight() # calcula el tamaño de la pantalla del usuario
        # reduce al 0.8 el tamaño
        ancho = int(w * 0.8) 
        alto = int(h * 0.8)
        # se calcula coordenadas para centrar
        x = (w - ancho) // 2
        y = (h - alto) // 2
        #w,h = self.ventana.winfo_screenmmwidth(),self.ventana.winfo_screenheight() # En esta línea, se obtiene el ancho (w) y la altura (h) de la pantalla en la que se ejecuta la ventana utilizando los métodos .winfo_screenwidth() y .winfo_screenheight() respectivamente.
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}") #con las coordenadas hallas anteriormente se calcula el tamaño de la ventana y se centra.
        self.ventana.config(bg='#ffcc00') # se configura el color de fondo de la ventana como '#fcfcfc' utilizando el método .config(). El código de color '#fcfcfc' representa un tono de gris claro.
        self.ventana.resizable(width=0, height=0) # Aquí se establece la capacidad de redimensionamiento de la ventana a width=0 y height=0, lo que significa que la ventana no se podrá redimensionar en ancho ni en alto. Esto evita que el usuario pueda cambiar el tamaño de la ventana manualmente.
        logo  = utl.leerImagen("./Login/Imagenes/isolino graduado.png",(200,200))
        label = tk.Label(self.ventana, image=logo, bg='#ffcc00')
        self.ventana.iconbitmap("./Login/Imagenes/sombrero-de-graduacion.ico")
        label.place(x=0,y=0,relwidth=1,relheight=1)
        title = tk.Label(self.ventana, text="Formacion de empleados Fiberglass", font=('Arial', 40), fg="#666a88", bg="#fcfcfc", padx=50)# Se crea una etiqueta (Label) de Tkinter dentro del marco frameFormTop. La etiqueta muestra el texto "CAPACITEICHON" y tiene una fuente de tamaño 40 en Arial. Los parámetros fg="#666a88" y bg="#fcfcfc" establecen los colores del texto y del fondo, respectivamente. El parámetro padx=50 agrega un relleno interno horizontal de 50 píxeles a la etiqueta.
        title.pack(expand=tk.NO, fill=tk.BOTH) # Aquí se empaqueta (coloca) la etiqueta title dentro del marco frameFormTop. El parámetro expand=tk.NO indica que la etiqueta no debe expandirse para llenar todo el espacio disponible, y fill=tk.BOTH permite que la etiqueta se expanda tanto horizontal como verticalmente para llenar el espacio disponible.
        #Etiqueta y cuadro para sgid
        etiqueta = tk.Label(self.ventana, text="Sgid: ", font=('Arial', 10),bg='#ffcc00')
        etiqueta.place(x=20, y=100, anchor="nw")
        textoSgid = tk.Entry(self.ventana, font=("Arial", 10))
        textoSgid.place(x=80, y=100, anchor="nw")
        #Etiqueta y cuadro para Nombre
        etiquetaNombre = tk.Label(self.ventana, text="Nombre: ", font=('Arial', 10),bg='#ffcc00')
        etiquetaNombre.place(x=320, y=100, anchor="n")
        textoNombre = tk.Entry(self.ventana, font=("Arial", 10), width=40, state="disabled")
        textoNombre.place(x=500, y=100, anchor="n")
         #Etiqueta y cuadro para genero
        etiquetaGenero = tk.Label(self.ventana, text="Genero: ", font=('Arial', 10),bg='#ffcc00')
        etiquetaGenero.place(x=770, y=100, anchor="ne")
        textoGenero = tk.Entry(self.ventana, font=("Arial", 10), width=10, state="disabled")
        textoGenero.place(x=850, y=100, anchor="ne")
         #Etiqueta y cuadro para fecha de ingreso
        etiquetafecha = tk.Label(self.ventana, text="fecha de ingreso: ", font=('Arial', 10), bg='#ffcc00')
        etiquetafecha.place(x=900, y=100 )
        textofecha = tk.Entry(self.ventana, font=("Arial", 10), width=10, state="disabled")
        textofecha.place(x=1020, y=100)
        self.ventana.mainloop()
        
        
        
