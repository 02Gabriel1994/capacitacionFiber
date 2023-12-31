import tkinter as tk
from tkinter.font import BOLD
from tkinter import ttk
import Login.utilidades.generic as utl
import Login.validacion.conexion as con
from datetime import datetime
from tkinter import *
from Login.utilidades.generic import acercaDe
from PIL import Image, ImageTk

class masterPanel:
    def cerrarSesion(self):
        self.ventana.destroy()
    def regresar_principal(self):
        self.principal.ventana.deiconify()  # Mostrar la ventana A nuevamente
        self.ventana.destroy()
    def __init__(self,root, principal) :
        self.ventana = tk.Toplevel(root) # crea una instancia de la clase Tk de la biblioteca Tkinter y se asigna a self.ventana. Esto crea una ventana principal para la aplicación.
        self.principal = principal
        self.ventana.title('Capaciteichon') # Aquí se establece el título de la ventana como "master panel" utilizando el método .title().
        w,h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight() # calcula el tamaño de la pantalla del usuario
        # reduce al 0.8 el tamaño
        ancho = int(w * 0.8) 
        alto = int(h * 0.8)
        # se calcula coordenadas para centrar
        x = (w - ancho) // 2
        y = (h - alto) // 2
        menu = Menu (self.ventana)
        #w,h = self.ventana.winfo_screenmmwidth(),self.ventana.winfo_screenheight() # En esta línea, se obtiene el ancho (w) y la altura (h) de la pantalla en la que se ejecuta la ventana utilizando los métodos .winfo_screenwidth() y .winfo_screenheight() respectivamente.
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}") #con las coordenadas hallas anteriormente se calcula el tamaño de la ventana y se centra.
        self.ventana.config(bg='#ffcc00',  menu=menu) # se configura el color de fondo de la ventana como '#fcfcfc' utilizando el método .config(). El código de color '#fcfcfc' representa un tono de gris claro.
        self.ventana.resizable(width=10, height=10) # Aquí se establece la capacidad de redimensionamiento de la ventana a width=0 y height=0, lo que significa que la ventana no se podrá redimensionar en ancho ni en alto. Esto evita que el usuario pueda cambiar el tamaño de la ventana manualmente.
        #logo  = utl.leerImagen("./Login/Imagenes/isolino graduado.png",(200,200))
        #label = tk.Label(self.ventana, image=logo, bg='#ffcc00')
        self.ventana.iconbitmap("./Login/Imagenes/sombrero-de-graduacion.ico")
        #label.place(x=0,y=0,relwidth=1,relheight=1)
        title = tk.Label(self.ventana, text="Registro de empleados Fiberglass", font=('Arial', 40), fg="#666a88", bg="#fcfcfc", padx=50)# Se crea una etiqueta (Label) de Tkinter dentro del marco frameFormTop. La etiqueta muestra el texto "CAPACITEICHON" y tiene una fuente de tamaño 40 en Arial. Los parámetros fg="#666a88" y bg="#fcfcfc" establecen los colores del texto y del fondo, respectivamente. El parámetro padx=50 agrega un relleno interno horizontal de 50 píxeles a la etiqueta.
        title.pack(expand=tk.NO, fill=tk.BOTH) # Aquí se empaqueta (coloca) la etiqueta title dentro del marco frameFormTop. El parámetro expand=tk.NO indica que la etiqueta no debe expandirse para llenar todo el espacio disponible, y fill=tk.BOTH permite que la etiqueta se expanda tanto horizontal como verticalmente para llenar el espacio disponible.
        # Menu desplegable para la configuracion de la conexion. 
        
        sesion= Menu (menu, tearoff=0)
        sesion.add_command(label="Cerrar Sesión", command=self.cerrarSesion)
        sesion.add_separator()
        sesion.add_command(label="Acerca de", command=lambda: acercaDe())
        menu.add_cascade(label="Sesión", menu= sesion)
        
        frameFormTop =tk.Frame(self.ventana, height=70, bd=2, relief=tk.SOLID, bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameFormTop.pack(side='top', fill=tk.X, pady=20, padx= 100) #El parámetro side='top' indica que el marco se coloque en la parte superior de otros elementos (si los hay), y fill=tk.X permite que el marco se expanda horizontalmente para ocupar todo el ancho disponible.
        #Etiqueta y cuadro para Cedula
        etiquetaCedula = tk.Label(frameFormTop, text="Cedula:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaCedula.pack(side= 'left', padx=(10,2))
        textoCedula = tk.Entry(frameFormTop, font=("Arial", 10))
        textoCedula.pack(side= 'left', padx=(1,20))
        # boton para buscar
        buscar = tk.Button(frameFormTop, text="Buscar", font=("Arial", 14), bg= "#000000", bd=0, fg="#fff", command=lambda: llenarInformacion(textoCedula.get()))
        buscar.pack(side= 'left', padx=20)
               
        #--------------
        #Segundo frame
        #-----------
        frameForm =tk.Frame(self.ventana, height=7000, bd=0, relief=tk.SOLID, bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameForm.columnconfigure([0,1,2,3], weight=1)
        frameForm.pack(side='top', fill=tk.BOTH)    
        #Etiqueta y cuadro para Nombre
        etiquetaNombre = tk.Label(frameForm, text="Nombre: ", font=('Arial', 10, 'bold'),bg='#ffcc00')
        etiquetaNombre.grid(row=0, column=0, pady=20)
        textoNombre = tk.Entry(frameForm, font=("Arial", 10), width=40, state="disabled")
        textoNombre.grid(row=0, column=1, padx=(3,20))
         #Etiqueta y cuadro para genero
        etiquetaGenero = tk.Label(frameForm, text="Genero: ", font=('Arial', 10, 'bold'),bg='#ffcc00')
        etiquetaGenero.grid(row=0, column=2, padx=(0,3))
        textoGenero = tk.Entry(frameForm, font=("Arial", 10), width=15, state="disabled")
        textoGenero.grid(row=0, column=3, padx=(1,20))
         #Etiqueta y cuadro para fecha de ingreso
        etiquetafecha = tk.Label(frameForm, text="Fecha de ingreso: ", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetafecha.grid(row=1, column=0, pady=20)
        textofecha = tk.Entry(frameForm, font=("Arial", 10), width=20, state="disabled")
        textofecha.grid(row=1, column=1, padx=(1,20))
        
        #Etiqueta y centro de costos
        etiquetaCc = tk.Label(frameForm, text="CC:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaCc.grid(row=1, column=2, padx=(0))
        textoCc = tk.Entry(frameForm, font=("Arial", 10), state="disabled",width=5)
        textoCc.grid(row=1, column=3, padx=(0))
        #Etiqueta y texto para Area
        etiquetaArea = tk.Label(frameForm, text="Area:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaArea.grid(row=2, column=0, pady=20)
        textoArea = tk.Entry(frameForm, font=("Arial", 10), state="disabled", width=35)
        textoArea.grid(row=2, column=1, padx=(0)) 
         #Etiqueta y texto para Cargo
        etiquetaCargo = tk.Label(frameForm, text="Cargo:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaCargo.grid(row=2, column=2, padx=(0))
        textoCargo = tk.Entry(frameForm, font=("Arial", 10), state="disabled", width=35)
        textoCargo.grid(row=2, column=3, padx=(0))   
        
          #Etiqueta y texto para tipo empleado
        etiquetaEmpleado = tk.Label(frameForm, text="Tipo Empleado:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaEmpleado.grid(row=3, column=0, pady=20)
        textoEmpleado = tk.Entry(frameForm, font=("Arial", 10), state="disabled", width=35)
        textoEmpleado.grid(row=3, column=1) 
         #Etiqueta y texto para Empleado SG
        combo_varSG = tk.StringVar()
        etiquetaSG = tk.Label(frameForm, text="Empleado SG:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaSG.grid(row=3, column=2)
        textoSG = ttk.Combobox(frameForm, font=("Arial", 10), textvariable=combo_varSG, width=20, state="readonly" )
        elementossg = ["CUADRO", "EMPLEADO", "OBRERO"]
        textoSG['values'] = elementossg
        textoSG.set("Seleccionar elemento")
        textoSG.grid(row=3, column=3) 
         #Etiqueta y texto para capacitacion a asignar
        combo_var = tk.StringVar()
        etiquetaCapacitacion = tk.Label(frameForm, text="Nombre Capacitacion:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaCapacitacion.grid(row=4, column=0, pady=20)
        textoCapacitacion = ttk.Combobox(frameForm, font=("Arial", 10), textvariable=combo_var, width=35, state="readonly" )
        elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
        textoCapacitacion['values'] = elementos
        textoCapacitacion.set("Seleccionar elemento")
        textoCapacitacion.grid(row=4, column=1)   
       
         #--------------
        #cuarto frame
        #----------- 
       
        frameForm5 =tk.Frame(self.ventana, height=70, bd=20,  bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameForm5.columnconfigure([0,1,2,3], weight=1)
        frameForm5.pack(side='bottom', fill=tk.X) 
        imagen = Image.open("./Login/Imagenes/inicio.png")
        imagen = imagen.resize((10, 10), Image.BICUBIC)
        imagen = ImageTk.PhotoImage(imagen)
        #Boton Guardar      
        guardar = tk.Button(frameForm5, text="Guardar", font=("Arial", 14), bg= "#000000", bd=0, fg="#fff")
        guardar.pack(side= 'bottom', padx=20)
        # boton de inicio
        imagenInicio = Image.open("./Login/Imagenes/inicio.png")
        imagenInicio = imagenInicio.resize((50, 50), Image.BICUBIC)
        imagenInicio = ImageTk.PhotoImage(imagenInicio)
        
        botonInicio = ttk.Button(frameForm5, image=imagenInicio,  command=self.regresar_principal) #, command=abrir_segunda_ventana)
        
        botonInicio.pack(side=tk.RIGHT) 
        
        
        def llenarInformacion( cedulav):
          resultado = con.buscar_Datos(cedulav) 
          print (resultado)   
          textoNombre.config(state=tk.NORMAL)
          textoNombre.delete(0, tk.END)
          textoNombre.insert(0, resultado[6])
          textoNombre.config(state=tk.DISABLED)
          #
          textoGenero.config(state=tk.NORMAL)
          textoGenero.delete(0, tk.END)
          textoGenero.insert(0, resultado[9])
          textoGenero.config(state=tk.DISABLED)
          #
          textofecha.config(state=tk.NORMAL)
          textofecha.delete(0, tk.END)
          fecha = resultado[15]
          textofecha.insert(0, fecha.date())
          textofecha.config(state=tk.DISABLED)
          #
          textoCc.config(state=tk.NORMAL)
          textoCc.delete(0, tk.END)
          textoCc.insert(0, resultado[3])
          textoCc.config(state=tk.DISABLED)
          #
          textoArea.config(state=tk.NORMAL)
          textoArea.delete(0, tk.END)
          textoArea.insert(0, resultado[4])
          textoArea.config(state=tk.DISABLED)
          #
          textoCargo.config(state=tk.NORMAL)
          textoCargo.delete(0, tk.END)
          textoCargo.insert(0, resultado[21])
          textoCargo.config(state=tk.DISABLED)
          #
          
          textoEmpleado.config(state=tk.NORMAL)
          textoEmpleado.delete(0, tk.END)
          textoEmpleado.insert(0, resultado[20])
          textoEmpleado.config(state=tk.DISABLED)
        self.ventana.mainloop()
        
        
        
        


