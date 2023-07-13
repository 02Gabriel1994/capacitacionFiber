import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import Login.utilidades.generic as utl
from Login.Forms.master import masterPanel
import Login.validacion.cifrado  as validar

class app:
    
    def verificar (self):
        usu = self.usuario.get()
        password = self.passw.get()
        ingresar = validar.validarlogin(password, usu)
        if (ingresar == True):
            self.ventana.destroy()
            masterPanel()
        else:
            messagebox.showerror(message="Contraseña incorrecta", title= "Mensaje")
    
    def __init__(self):
        #crea la ventana
       self.ventana =tk.Tk()
       self.ventana.title('Inicio de Sesion')
       self.ventana.geometry('800x500')
       self.ventana.config(bg='#fcfcfc')
       self.ventana.resizable(width=0,height=0)
       utl.centrarVentana(self.ventana, 800,500)
       #crea la imagen al lado izq
       logo  = utl.leerImagen("./Login/Imagenes/isolino graduado.png",(200,200)) # cargar la imagen desde el archivo "./Login/Imagenes/isolino graduado.png" y redimensionarla a un tamaño de 200x200 píxeles. El resultado se asigna a la variable logo.
       frameLogo = tk.Frame (self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')# Se crea un marco (frame) dentro de la ventana principal self.ventana. El parámetro bd=0 establece el ancho del borde en cero, width=300 establece el ancho del marco en 300 píxeles, relief=tk.SOLID define el estilo del borde como sólido, padx=10 y pady=10 especifican los rellenos internos del marco, y bg='#3a7ff6' establece el color de fondo del marco en un tono azul.
       frameLogo.pack(side="left", expand=tk.NO, fill=tk.BOTH)# coloca el marco en la ventana principal utilizando el método pack(). El parámetro side="left" indica que el marco se colocará a la izquierda de otros elementos (si los hay). expand=tk.YES y fill=tk.BOTH permiten que el marco se expanda tanto horizontal como verticalmente para ocupar todo el espacio disponible en el lado izquierdo de la ventana.
       label = tk.Label(frameLogo, image=logo, bg = '#3a7ff6')
       label.place(x=0, y=0, relwidth=1, relheight=1)
       self.ventana.iconbitmap("./Login/Imagenes/sombrero-de-graduacion.ico")
       # crea el contenedor al lado dere
       frameForm = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
       frameForm.pack(side ="right", expand=tk.YES, fill=tk.BOTH)
       # titulo de la ventana 
       frameFormTop =tk.Frame(frameForm, height=50, bd=0, relief=tk.SOLID, bg='black')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
       frameFormTop.pack(side='top', fill=tk.X) #El parámetro side='top' indica que el marco se coloque en la parte superior de otros elementos (si los hay), y fill=tk.X permite que el marco se expanda horizontalmente para ocupar todo el ancho disponible.
       title = tk.Label(frameFormTop, text="CAPACITEICHON", font=('Arial', 40), fg="#666a88", bg="#fcfcfc", padx=50)# Se crea una etiqueta (Label) de Tkinter dentro del marco frameFormTop. La etiqueta muestra el texto "CAPACITEICHON" y tiene una fuente de tamaño 40 en Arial. Los parámetros fg="#666a88" y bg="#fcfcfc" establecen los colores del texto y del fondo, respectivamente. El parámetro padx=50 agrega un relleno interno horizontal de 50 píxeles a la etiqueta.
       title.pack(expand=tk.NO, fill=tk.BOTH) # Aquí se empaqueta (coloca) la etiqueta title dentro del marco frameFormTop. El parámetro expand=tk.NO indica que la etiqueta no debe expandirse para llenar todo el espacio disponible, y fill=tk.BOTH permite que la etiqueta se expanda tanto horizontal como verticalmente para llenar el espacio disponible.
       title2 = tk.Label(frameFormTop, text="Inicio de Sesion", font=('Arial', 30), fg="#666a88", bg="#fcfcfc", padx=50)
       title2.pack(expand=tk.YES, fill=tk.BOTH)
       framellenado = tk.Frame(frameForm, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
       framellenado.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
       
       #etiqueta para usuario
       etiquetaUsuario = tk.Label(framellenado, text="Usuario", font=('Arial', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
       etiquetaUsuario.pack(fill=tk.X, padx=20, pady=5)
       self.usuario = ttk.Entry(framellenado, font=("Arial", 14))
       self.usuario.pack(fill=tk.X, padx=20, pady=10)
       #etiqueta contraseña
       etiquetaPass = tk.Label(framellenado, text="Contraseña", font=('Arial', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
       etiquetaPass.pack(fill=tk.X, padx=20, pady=5)
       self.passw = ttk.Entry(framellenado, font=("Arial", 14))
       self.passw.pack(fill=tk.X, padx=20, pady=10)
       self.passw.config(show="*")
       #boton
       inicio = tk.Button(framellenado, text="Ingresar", font=("Arial", 14, BOLD), bg= "#3a7ff6", bd=0, fg="#fff", command=self.verificar)
       inicio.pack(fill=tk.X, padx=20, pady=20)
       inicio.bind("<Return>",(lambda event:self.verificar))
       
       
       #self.usuario.insert(0,"Holas")
       self.ventana.mainloop()
       
  