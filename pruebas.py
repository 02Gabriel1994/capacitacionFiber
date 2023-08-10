import tkinter as tk
from tkcalendar import DateEntry

'''def show_calendar_from():
    cal_from.place(x=10, y=70)

def show_calendar_to():
    cal_to.place(x=10, y=120)

def select_date_from():
    date_from.set(cal_from.get_date())
    cal_from.place_forget()

def select_date_to():
    date_to.set(cal_to.get_date())
    cal_to.place_forget()

root = tk.Tk()
root.title("Selección de Fechas")

# Variables para almacenar las fechas seleccionadas
date_from = tk.StringVar()
date_to = tk.StringVar()

# Etiqueta y Calendario para "Desde"
label_from = tk.Label(root, text="Desde:")
label_from.pack()
cal_from = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
cal_from.pack()
cal_from.place_forget()  # Ocultar el calendario al inicio

# Etiqueta y Calendario para "Hasta"
label_to = tk.Label(root, text="Hasta:")
label_to.pack()
cal_to = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
cal_to.pack()
cal_to.place_forget()  # Ocultar el calendario al inicio

# Asociar eventos a las etiquetas para mostrar los calendarios
label_from.bind("<Button-1>", lambda event: [show_calendar_from(), cal_to.place_forget()])
label_to.bind("<Button-1>", lambda event: [show_calendar_to(), cal_from.place_forget()])

# Loop principal de la interfaz gráfica'''
####################################################

# from tkinter import ttk

# def obtener_hora():
#     hora = spinbox_horas.get()
#     minutos = spinbox_minutos.get()
#     label_resultado.config(text=f"Hora seleccionada: {hora}:{minutos}")

# root = tk.Tk()
# root.title("Selector de Hora")

# # Selector de horas
# spinbox_horas = ttk.Spinbox(root, from_=0, to=23, width=5)
# spinbox_horas.pack(padx=20, pady=10)

# # Selector de minutos
# spinbox_minutos = ttk.Spinbox(root, from_=0, to=59, width=5)
# spinbox_minutos.pack(padx=20, pady=10)

# # Botón para obtener la hora seleccionada
# btn_obtener_hora = ttk.Button(root, text="Obtener Hora", command=obtener_hora)
# btn_obtener_hora.pack()

# # Etiqueta para mostrar el resultado
# label_resultado = ttk.Label(root, text="")
# label_resultado.pack()
###########################
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def abrir_primera_ventana():
    primera_ventana = tk.Toplevel(root)
    primera_ventana.title("Primera Ventana")
    
    label = ttk.Label(primera_ventana, text="¡Primera Ventana!")
    label.pack(padx=20, pady=20)

def abrir_segunda_ventana():
    segunda_ventana = tk.Toplevel(root)
    segunda_ventana.title("Segunda Ventana")
    
    label = ttk.Label(segunda_ventana, text="¡Segunda Ventana!")
    label.pack(padx=20, pady=20)

root = tk.Tk()
root.title("Ventana Principal")

# Cargar imágenes
imagen1 = Image.open("./Login/Imagenes/isolino graduado.png")
imagen1 = imagen1.resize((150, 150), Image.BICUBIC)
imagen1 = ImageTk.PhotoImage(imagen1)

imagen2 = Image.open("./Login/Imagenes/imagen.jpg")
imagen2 = imagen2.resize((150, 150), Image.BICUBIC)
imagen2 = ImageTk.PhotoImage(imagen2)

# Crear botones con las imágenes
boton_imagen1 = ttk.Button(root, image=imagen1, command=abrir_primera_ventana)
boton_imagen1.pack(side=tk.LEFT, padx=20, pady=20)

boton_imagen2 = ttk.Button(root, image=imagen2, command=abrir_segunda_ventana)
boton_imagen2.pack(side=tk.RIGHT, padx=20, pady=20)

root.mainloop()










