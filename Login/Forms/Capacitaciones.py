import tkinter as tk
from tkinter.font import BOLD
from tkinter import ttk
import Login.utilidades.generic as utl
import Login.validacion.conexion as con
from datetime import datetime
from tkinter import messagebox
from tkcalendar import DateEntry

class RCapacitacion:
    
    def __init__(self) :
        self.ventana = tk.Tk() # crea una instancia de la clase Tk de la biblioteca Tkinter y se asigna a self.ventana. Esto crea una ventana principal para la aplicación.
        self.ventana.title('Registro de capacitación') # Aquí se establece el título de la ventana como "master panel" utilizando el método .title().
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
        self.ventana.iconbitmap("./Login/Imagenes/sombrero-de-graduacion.ico")
        title = tk.Label(self.ventana, text="Formacion de empleados Fiberglass", font=('Arial', 40), fg="#666a88", bg="#fcfcfc", padx=50)# Se crea una etiqueta (Label) de Tkinter dentro del marco frameFormTop. La etiqueta muestra el texto "CAPACITEICHON" y tiene una fuente de tamaño 40 en Arial. Los parámetros fg="#666a88" y bg="#fcfcfc" establecen los colores del texto y del fondo, respectivamente. El parámetro padx=50 agrega un relleno interno horizontal de 50 píxeles a la etiqueta.
        title.pack(expand=tk.NO, fill=tk.BOTH) # Aquí se empaqueta (coloca) la etiqueta title dentro del marco frameFormTop. El parámetro expand=tk.NO indica que la etiqueta no debe expandirse para llenar todo el espacio disponible, y fill=tk.BOTH permite que la etiqueta se expanda tanto horizontal como verticalmente para llenar el espacio disponible.
        frameForm = tk.Frame(self.ventana, bg='black', bd=0)
        frameForm.pack(side='top', fill=tk.X, pady=40)
        
        frameFormTop =tk.Frame(frameForm, height=10, relief=tk.SOLID, bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameFormTop.pack(side='top', fill=tk.X) #El parámetro side='top' indica que el marco se coloque en la parte superior de otros elementos (si los hay), y fill=tk.X permite que el marco se expanda horizontalmente para ocupar todo el ancho disponible.
        #Etiqueta y cuadro para Cedula
        Valor = 1
        combo_varCapa = tk.StringVar()
        etiqueIDCapa = tk.Label(frameFormTop, text=f"{Valor}", font=('Arial', 10, 'bold'), bg='#ffcc00', relief=tk.SOLID, bd=2)
        etiqueIDCapa.pack(side= 'left', padx=(10,2))
        #TODO: falta hacer una consulta SQL
        etiquetanNomCapa = tk.Label(frameFormTop, text="Nombre capacitacion:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetanNomCapa.pack(side= 'left', padx=(10,2))
        textoCapacitacion = ttk.Combobox(frameFormTop, font=("Arial", 10), textvariable=combo_varCapa, width=35 )
        elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
        textoCapacitacion['values'] = elementos
        textoCapacitacion.pack(side= 'left', padx=20)  
        # boton para buscar
        buscar = tk.Button(frameFormTop, text="Buscar", font=("Arial", 14), bg= "#000000", bd=0, fg="#fff")
        buscar.pack(side= 'left', padx=20)
               
        #--------------
        #Segundo frame
        #-----------
        frameForm2 =tk.Frame(self.ventana, height=70, bd=0, relief=tk.SOLID, bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameForm2.columnconfigure([0,1,2,3,4,5,6,7], weight=1)
        frameForm2.pack(side='top', fill=tk.X)
        frameForm2.pack_configure(padx=100)    
        
        #Etiqueta y cuadro para solicitante
        solicitante = tk.StringVar()
        etiquetaNombre = tk.Label(frameForm2, text="Solicitante: ", font=('Arial', 10, 'bold'),bg='#ffcc00')
        etiquetaNombre.grid(row=0, column=0, padx=(20,1))
        textoSolicitante = ttk.Combobox(frameForm2, font=("Arial", 10), textvariable=solicitante, width=35, state="readonly" )
        elementos = ["Gerente de area", "Jefes", "Supervisores"]
        textoSolicitante['values'] = elementos
        textoSolicitante.grid(row=0, column=1, padx=(1,20))
        
         #Etiqueta y cuadro de fecha para desde
        label_from = tk.Label(frameForm2, text="Fecha solicitada:" , font=('Arial', 10, 'bold'),bg='#ffcc00')
        label_from.grid(row=0, column=2, padx=(0,3))
        cal_from = DateEntry(frameForm2, width=12,  background='black', foreground='#ffcc00', borderwidth=2, state="readonly")
        cal_from.grid(row=0, column=3)
        cal_from.place_forget() 
        
         #Etiqueta y cuadro de fecha para hasta
        label_from = tk.Label(frameForm2, text="Fecha planeada:" , font=('Arial', 10, 'bold'),bg='#ffcc00')
        label_from.grid(row=0, column=4, padx=(0,3))
        cal_from = DateEntry(frameForm2, width=12,  background='black', foreground='#ffcc00', borderwidth=2, state="readonly")
        cal_from.grid(row=0, column=5)
        cal_from.place_forget() 
       
          #--------------
        #Tercer frame
        #-----------
        frameForm3 =tk.Frame(self.ventana, height=70, bd=20,  bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameForm3.columnconfigure([0,1,2,3,4,5], weight=1)
        frameForm3.pack(side='top', fill=tk.X)
        # Etiqueta para Fecha ejecutada
        label_from = tk.Label(frameForm3, text="Fecha ejecutada:" , font=('Arial', 10, 'bold'),bg='#ffcc00')
        label_from.grid(row=0, column=0, padx=(0,3))
        cal_from = DateEntry(frameForm3, width=12,  background='black', foreground='#ffcc00', borderwidth=2, state="readonly")
        cal_from.grid(row=0, column=1)
        cal_from.place_forget() 
        #Etiqueta y texto para Tema
        etiquetaTema = tk.Label(frameForm3, text="Tema:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaTema.grid(row=0, column=2, padx=(0))
        textoTema = tk.Text(frameForm3, font=("Arial", 10), width=60, height=2)
        textoTema.grid(row=0, column=3, padx=(0)) 
     
        #--------------
        #cuarto frame
        #-----------
        frameForm4 =tk.Frame(self.ventana, height=70, bd=20,  bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameForm4.columnconfigure([0,1,2,3], weight=1)
        frameForm4.pack(side='top', fill=tk.X)     
          #Etiqueta y texto para tipo empleado
        etiquetaObjetivo = tk.Label(frameForm4, text="Objetivo:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaObjetivo.grid(row=0, column=0, padx=(0))
        textoObjetivo = tk.Text(frameForm4, font=("Arial", 10), width=60, height=2)
        textoObjetivo.grid(row=0, column=1, padx=(0)) 
         #Etiqueta y texto para proveedor
        etiquetaEmpleado = tk.Label(frameForm4, text="Proveedor:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaEmpleado.grid(row=0, column=2)
        textoEmpleado = tk.Entry(frameForm4, font=("Arial", 10), width=35)
        textoEmpleado.grid(row=0, column=3)  
        
         #--------------
        #5 frame
        #----------- 
        frameForm5 =tk.Frame(self.ventana, height=70, bd=20,  bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameForm5.columnconfigure([0,1,2,3,4,5], weight=1)
        frameForm5.pack(side='top', fill=tk.X) 
        
      #Etiqueta y texto para ciudad
        etiquetaEmpleado = tk.Label(frameForm5, text="Ciudad:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaEmpleado.grid(row=0, column=0)
        textoEmpleado = tk.Entry(frameForm5, font=("Arial", 10), width=35)
        textoEmpleado.grid(row=0, column=1) 
        # otro frame para hora y mn 
        frameForm5_1 =tk.Frame(frameForm5, height=70, bd=20,  bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameForm5_1.columnconfigure([0,1,2,3], weight=1)
        frameForm5_1.grid(row=0, column=2)
        #horas
        etiquetaHora = tk.Label(frameForm5_1, text="Duración:", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaHora.grid(row=0, column=0)
        spinbox_horas = ttk.Spinbox(frameForm5_1, from_=0, to=23, width=5)
        spinbox_horas.grid(row=0, column=1)
        # Selector de minutos
        etiquetaHora = tk.Label(frameForm5_1, text=":", font=('Arial', 10, 'bold'), bg='#ffcc00')
        etiquetaHora.grid(row=0, column=2)
        spinbox_minutos = ttk.Spinbox(frameForm5_1, from_=0, to=59, width=5)
        spinbox_minutos.grid(row=0, column=3)
        #Etiqueta y cuadro para categoria
        categoria = tk.StringVar()
        etiquetaCategoria = tk.Label(frameForm5, text="Categoria : ", font=('Arial', 10, 'bold'),bg='#ffcc00')
        etiquetaCategoria.grid(row=0, column=3, padx=(20,1))
        textoSolicitante = ttk.Combobox(frameForm5, font=("Arial", 10), textvariable=categoria, width=35, state="readonly" )
        elementos = ["Entrenaminto Tecnico vinculado al cargo", "seguridad", "Liderazgo","OEA","EHS","SISTEMAS DE GESTION ISO 9001 14001" ,"CONTROL INTERNO","SAGRILAF","OTRO"]
        textoSolicitante['values'] = elementos
        textoSolicitante.grid(row=0, column=4, padx=(1,20))
          #--------------
        #6 frame
        #----------- 
        frameForm6 =tk.Frame(self.ventana, height=70, bd=20,  bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameForm6.columnconfigure([0,1,2,3,4,5], weight=1)
        frameForm6.pack(side='top', fill=tk.X) 
         #Etiqueta y cuadro para tipo capacitacion
        categoria = tk.StringVar()
        etiquetaCategoria = tk.Label(frameForm5, text="Categoria : ", font=('Arial', 10, 'bold'),bg='#ffcc00')
        etiquetaCategoria.grid(row=0, column=0, padx=(20,1))
        textoSolicitante = ttk.Combobox(frameForm5, font=("Arial", 10), textvariable=categoria, width=35, state="readonly" )
        elementos = ["Virtual", "Presencial"]
        textoSolicitante['values'] = elementos
        textoSolicitante.grid(row=0, column=1, padx=(1,20))
        #Etiqueta y cuadro para prioridad
        prioridad = tk.StringVar()
        etiquetaCategoria = tk.Label(frameForm6, text="Prioridad : ", font=('Arial', 10, 'bold'),bg='#ffcc00')
        etiquetaCategoria.grid(row=0, column=2, padx=(20,1))
        textoSolicitante = ttk.Combobox(frameForm6, font=("Arial", 10), textvariable=prioridad, width=35, state="readonly" )
        elementos = ["A", "B","C"]
        textoSolicitante['values'] = elementos
        textoSolicitante.grid(row=0, column=3, padx=(1,20))
        #Etiqueta y cuadro para Evaluacion
        evaluacion = tk.StringVar()
        etiquetaCategoria = tk.Label(frameForm6, text="Evaluacion? : ", font=('Arial', 10, 'bold'),bg='#ffcc00')
        etiquetaCategoria.grid(row=0, column=4, padx=(20,1))
        textoSolicitante = ttk.Combobox(frameForm6, font=("Arial", 10), textvariable=evaluacion, width=35, state="readonly" )
        elementos = ["SI", "NO"]
        textoSolicitante['values'] = elementos
        textoSolicitante.grid(row=0, column=5, padx=(1,20))
         #--------------
        #n frame
        #-----------
        frameFormn =tk.Frame(self.ventana, height=70, bd=20,  bg='#ffcc00')#crea un marco frameFormTop dentro de otro marco llamado frameForm. El parámetro height=50 establece la altura del marco en 50 píxeles, bd=0 establece el ancho del borde en cero, relief=tk.SOLID define el estilo del borde como sólido y bg='black' establece el color de fondo del marco en negro.
        frameFormn.columnconfigure([0,1,2,3], weight=1)
        frameFormn.pack(side='bottom', fill=tk.X) 
        
        
        #Boton Guardar      
        guardar = tk.Button(frameFormn, text="Guardar", font=("Arial", 14), bg= "#000000", bd=0, fg="#fff")
        guardar.pack(side= 'bottom', padx=20)
        def funcion():
          messagebox.showinfo("Información", f"esto muestra {combo_varCapa.get()}")
        self.ventana.mainloop()