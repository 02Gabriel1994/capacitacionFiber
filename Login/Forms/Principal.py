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

class principal:
    
    def __init__(self) :
        self.ventana = tk.Tk() 
        self.ventana.title('MENU PRINCIPAL') 
        
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        ancho = int(w * 0.8) 
        alto = int(h * 0.8)
        x = (w - ancho) // 2
        y = (h - alto) // 2

        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.ventana.config(bg='#ffcc00') 
        self.ventana.resizable(width=10, height=10) 
        self.ventana.iconbitmap("./Login/Imagenes/sombrero-de-graduacion.ico")
        
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

        boton_imagen1 = ttk.Button(frameForm, image=imagen1, command=abrir_primera_ventana)
        boton_imagen1.pack(side=tk.LEFT, padx=10) 

        boton_imagen2 = ttk.Button(frameForm, image=imagen2, command=abrir_segunda_ventana)
        boton_imagen2.pack(side=tk.LEFT, padx=10) 
        boton_imagen3 = ttk.Button(frameForm, image=imagen3, command=abrir_segunda_ventana)
        boton_imagen3.pack(side=tk.RIGHT, padx=10) 

        self.ventana.mainloop()

if __name__ == "__main__":
    app = principal()


# Resto del código sin cambios
