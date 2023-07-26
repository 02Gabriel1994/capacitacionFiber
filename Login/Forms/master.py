import tkinter as tk
from tkinter.font import BOLD
from tkinter import ttk
import Login.utilidades.generic as utl
import Login.validacion.conexion as con


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
        self.ventana.resizable(width=10, height=10) # Aquí se establece la capacidad de redimensionamiento de la ventana a width=0 y height=0, lo que significa que la ventana no se podrá redimensionar en ancho ni en alto. Esto evita que el usuario pueda cambiar el tamaño de la ventana manualmente.
        logo  = utl.leerImagen("./Login/Imagenes/isolino graduado.png",(200,200))
        label = tk.Label(self.ventana, image=logo, bg='#ffcc00')
        self.ventana.iconbitmap("./Login/Imagenes/sombrero-de-graduacion.ico")
        label.place(x=0,y=0,relwidth=1,relheight=1)
        title = tk.Label(self.ventana, text="Formacion de empleados Fiberglass", font=('Arial', 40), fg="#666a88", bg="#fcfcfc", padx=50)# Se crea una etiqueta (Label) de Tkinter dentro del marco frameFormTop. La etiqueta muestra el texto "CAPACITEICHON" y tiene una fuente de tamaño 40 en Arial. Los parámetros fg="#666a88" y bg="#fcfcfc" establecen los colores del texto y del fondo, respectivamente. El parámetro padx=50 agrega un relleno interno horizontal de 50 píxeles a la etiqueta.
        title.pack(expand=tk.NO, fill=tk.BOTH) # Aquí se empaqueta (coloca) la etiqueta title dentro del marco frameFormTop. El parámetro expand=tk.NO indica que la etiqueta no debe expandirse para llenar todo el espacio disponible, y fill=tk.BOTH permite que la etiqueta se expanda tanto horizontal como verticalmente para llenar el espacio disponible.
        
        # frameFormTop =tk.Frame(self.ventana, height=70, bd=0, relief=tk.SOLID, bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        # frameFormTop.pack(side='top', fill=tk.X) #El parámetro side='top' indica que el marco se coloque en la parte superior de otros elementos (si los hay), y fill=tk.X permite que el marco se expanda horizontalmente para ocupar todo el ancho disponible.
        # #Etiqueta y cuadro para sgid
        # etiqueta = tk.Label(frameFormTop, text="Sgid: ", font=('Arial', 10, 'bold'),bg='#ffcc00')
        # etiqueta.pack(side= 'left', padx=(50, 3), pady=50 )
        # textoSgid = tk.Entry(frameFormTop, font=("Arial", 10))
        # textoSgid.pack(side= 'left', padx=(1,20), pady=50 )
        # #Etiqueta y cuadro para Cedula
        # etiquetaCedula = tk.Label(frameFormTop, text="Cedula:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        # etiquetaCedula.pack(side= 'left', padx=(10,2))
        # textoCedula = tk.Entry(frameFormTop, font=("Arial", 10))
        # textoCedula.pack(side= 'left', padx=(1,20))
        # # boton para buscar
        # buscar = tk.Button(frameFormTop, text="Buscar", font=("Arial", 14), bg= "#000000", bd=0, fg="#fff", command=lambda: llenarInformacion(textoSgid.get(), textoCedula.get()))
        # buscar.pack(side= 'left', padx=20)
               
        # #--------------
        # #Segundo frame
        # #-----------
        # frameForm2 =tk.Frame(self.ventana, height=70, bd=0, relief=tk.SOLID, bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        # frameForm2.columnconfigure([0,1,2,3,4,5], weight=1)
        # frameForm2.pack(side='top', fill=tk.X)    
        # #Etiqueta y cuadro para Nombre
        # etiquetaNombre = tk.Label(frameForm2, text="Nombre: ", font=('Arial', 10, 'bold'),bg='#ffcc00')
        # etiquetaNombre.grid(row=0, column=0, padx=(20,1))
        # textoNombre = tk.Entry(frameForm2, font=("Arial", 10), width=40, state="disabled")
        # textoNombre.grid(row=0, column=1, padx=(3,20))
        #  #Etiqueta y cuadro para genero
        # etiquetaGenero = tk.Label(frameForm2, text="Genero: ", font=('Arial', 10, 'bold'),bg='#ffcc00')
        # etiquetaGenero.grid(row=0, column=2, padx=(0,3))
        # textoGenero = tk.Entry(frameForm2, font=("Arial", 10), width=10, state="disabled")
        # textoGenero.grid(row=0, column=3, padx=(1,20))
        #  #Etiqueta y cuadro para fecha de ingreso
        # etiquetafecha = tk.Label(frameForm2, text="Fecha de ingreso: ", font=('Arial', 10, 'bold'), bg='#ffcc00')
        # etiquetafecha.grid(row=0, column=4, padx=(0,3))
        # textofecha = tk.Entry(frameForm2, font=("Arial", 10), width=20, state="disabled")
        # textofecha.grid(row=0, column=5, padx=(1,20))
        #   #--------------
        # #Tercer frame
        # #-----------
        # frameForm3 =tk.Frame(self.ventana, height=70, bd=20,  bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        # frameForm3.columnconfigure([0,1,2,3,4,5], weight=1)
        # frameForm3.pack(side='top', fill=tk.X)
        # #Etiqueta y centro de costos
        # etiquetaCc = tk.Label(frameForm3, text="CC:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        # etiquetaCc.grid(row=0, column=0, padx=(0))
        # textoCc = tk.Entry(frameForm3, font=("Arial", 10), state="disabled",width=5)
        # textoCc.grid(row=0, column=1, padx=(0))
        # #Etiqueta y texto para Area
        # etiquetaArea = tk.Label(frameForm3, text="Area:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        # etiquetaArea.grid(row=0, column=2, padx=(0))
        # textoArea = tk.Entry(frameForm3, font=("Arial", 10), state="disabled", width=35)
        # textoArea.grid(row=0, column=3, padx=(0)) 
        #  #Etiqueta y texto para Cargo
        # etiquetaCargo = tk.Label(frameForm3, text="Cargo:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        # etiquetaCargo.grid(row=0, column=4, padx=(0))
        # textoCargo = tk.Entry(frameForm3, font=("Arial", 10), state="disabled", width=35)
        # textoCargo.grid(row=0, column=5, padx=(0))   
        # #--------------
        # #cuarto frame
        # #-----------
        # frameForm4 =tk.Frame(self.ventana, height=70, bd=20,  bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        # frameForm4.columnconfigure([0,1,2,3], weight=1)
        # frameForm4.pack(side='top', fill=tk.X)     
        #   #Etiqueta y texto para tipo empleado
        # etiquetaEmpleado = tk.Label(frameForm4, text="Tipo Empleado:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        # etiquetaEmpleado.grid(row=0, column=0)
        # textoEmpleado = tk.Entry(frameForm4, font=("Arial", 10), state="disabled", width=35)
        # textoEmpleado.grid(row=0, column=1)  
        #  #Etiqueta y texto para tipo empleado
        # combo_var = tk.StringVar()
        # etiquetaCapacitacion = tk.Label(frameForm4, text="Nombre Capacitacion:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        # etiquetaCapacitacion.grid(row=0, column=2)
        # textoCapacitacion = ttk.Combobox(frameForm4, font=("Arial", 10), textvariable=combo_var, width=35, state="readonly" )
        # elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
        # textoCapacitacion['values'] = elementos
        # textoCapacitacion.set("Seleccionar elemento")
        # textoCapacitacion.grid(row=0, column=3)   
       
        #  #--------------
        # #cuarto frame
        # #----------- 
       
        # frameForm5 =tk.Frame(self.ventana, height=70, bd=20,  bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        # frameForm5.columnconfigure([0,1,2,3], weight=1)
        # frameForm5.pack(side='bottom', fill=tk.X) 
        # #Boton Guardar      
        # guardar = tk.Button(frameForm5, text="Guardar", font=("Arial", 14), bg= "#000000", bd=0, fg="#fff")
        # guardar.pack(side= 'bottom', padx=20)
        # ... (código anterior sigue sin cambios)

        # Marco 1 (frameFormTop)
        # ... (código anterior sigue sin cambios)

        # Marco 1 (frameFormTop)
        # ... (código anterior sigue sin cambios)

        # Marco 1 (frameFormTop)
                # ... (código anterior sin cambios)

        # Marco 1 (frameFormTop)
        frameFormTop = tk.Frame(self.ventana, height=70, bd=0, relief=tk.SOLID, bg='#ffcc00')
        frameFormTop.pack(side='top', fill=tk.X)

        etiqueta = tk.Label(frameFormTop, text="Sgid: ", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiqueta.pack(side='left', padx=(50, 3), pady=50)
        textoSgid = tk.Entry(frameFormTop, font=("Arial", 10))
        textoSgid.pack(side='left', padx=(1, 20), pady=50)

        etiquetaCedula = tk.Label(frameFormTop, text="Cédula:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaCedula.pack(side='left', padx=(10, 2))
        textoCedula = tk.Entry(frameFormTop, font=("Arial", 10))
        textoCedula.pack(side='left', padx=(1, 20))

        buscar = tk.Button(frameFormTop, text="Buscar", font=("Arial", 14), bg="#000000", bd=0, fg="#fff", command=lambda: llenarInformacion(textoSgid.get(), textoCedula.get()))
        buscar.pack(side='left', padx=20)

        # Marco 2 (frameForm2)
        frameForm2 = tk.Frame(self.ventana, height=70, bd=0, relief=tk.SOLID, bg='#ffcc00')
        frameForm2.pack(side='top', fill=tk.X)

        etiquetaNombre = tk.Label(frameForm2, text="Nombre: ", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaNombre.pack(side='left', padx=(20, 2))
        textoNombre = tk.Entry(frameForm2, font=("Arial", 10), width=40, state="disabled")
        textoNombre.pack(side='left', padx=(3, 20))

        etiquetaGenero = tk.Label(frameForm2, text="Género: ", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaGenero.pack(side='left', padx=(0, 3))
        textoGenero = tk.Entry(frameForm2, font=("Arial", 10), width=10, state="disabled")
        textoGenero.pack(side='left', padx=(1, 20))

        etiquetafecha = tk.Label(frameForm2, text="Fecha de ingreso: ", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetafecha.pack(side='left', padx=(0, 3))
        textofecha = tk.Entry(frameForm2, font=("Arial", 10), width=20, state="disabled")
        textofecha.pack(side='left', padx=(1, 20))

        # Marco 3 (frameForm3)
        frameForm3 = tk.Frame(self.ventana, height=70, bd=20, bg='#ffcc00')
        frameForm3.pack(side='top', fill=tk.X)

        etiquetaCc = tk.Label(frameForm3, text="CC:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaCc.pack(side='left', padx=(10, 2))
        textoCc = tk.Entry(frameForm3, font=("Arial", 10), state="disabled", width=5)
        textoCc.pack(side='left', padx=(2, 15))

        etiquetaArea = tk.Label(frameForm3, text="Área:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaArea.pack(side='left', padx=(5, 2))
        textoArea = tk.Entry(frameForm3, font=("Arial", 10), state="disabled", width=35)
        textoArea.pack(side='left', padx=(2,15))

        etiquetaCargo = tk.Label(frameForm3, text="Cargo:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaCargo.pack(side='left', padx=(5,2))
        textoCargo = tk.Entry(frameForm3, font=("Arial", 10), state="disabled", width=35)
        textoCargo.pack(side='left', padx=(2,15))

      

        # Marco 4 (frameForm4)
        frameForm4 = tk.Frame(self.ventana, height=70, bd=20, bg='#ffcc00')
        frameForm4.pack(side='top', fill=tk.X)

        etiquetaEmpleado = tk.Label(frameForm4, text="Tipo Empleado:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaEmpleado.pack(side='left', padx=(5,2))
        textoEmpleado = tk.Entry(frameForm4, font=("Arial", 10), state="disabled", width=35)
        textoEmpleado.pack(side='left', padx=(2,15))

        combo_var = tk.StringVar()
        etiquetaCapacitacion = tk.Label(frameForm4, text="Nombre Capacitación:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaCapacitacion.pack(side='left', padx=(5,2))
        textoCapacitacion = ttk.Combobox(frameForm4, font=("Arial", 10), textvariable=combo_var, width=35, state="readonly" )
        elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
        textoCapacitacion['values'] = elementos
        textoCapacitacion.set("Seleccionar elemento")
        textoCapacitacion.pack(side='left', padx=(2,15))

    



        def llenarInformacion(sgidv, cedulav):
          resultado = con.buscar_Datos(sgidv, cedulav)    
          textoNombre.config(state=tk.NORMAL)
          textoNombre.delete(0, tk.END)
          textoNombre.insert(0, resultado[1])
          textoNombre.config(state=tk.DISABLED)
        self.ventana.mainloop()
        
        
        


