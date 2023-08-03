import tkinter as tk
from tkcalendar import DateEntry

def show_calendar_from():
    cal_from.place(x=10, y=70)
'''
def show_calendar_to():
    cal_to.place(x=10, y=120)'''

def select_date_from():
    date_from.set(cal_from.get_date())
    cal_from.place_forget()
''''
def select_date_to():
    date_to.set(cal_to.get_date())
    cal_to.place_forget()'''

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
''''
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
root.mainloop()


