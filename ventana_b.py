import tkinter as tk

class VentanaB:
    def __init__(self, root, ventana_a):
        self.root = tk.Toplevel(root)
        self.ventana_a = ventana_a  # Mantener una referencia a la ventana A
        self.root.title("Ventana B")
        
        self.btn_regresar_a = tk.Button(self.root, text="Regresar a Ventana A", command=self.regresar_ventana_a)
        self.btn_regresar_a.pack()

    def regresar_ventana_a(self):
        self.ventana_a.root.deiconify()  # Mostrar la ventana A nuevamente
        self.root.destroy()  # Destruir la ventana B

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaB(root)
    root.mainloop()














