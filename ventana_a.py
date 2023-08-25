import tkinter as tk
from ventana_b import VentanaB

class VentanaA:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana A")
        
        self.btn_abrir_b = tk.Button(self.root, text="Abrir Ventana B", command=self.abrir_ventana_b)
        self.btn_abrir_b.pack()

    def abrir_ventana_b(self):
        self.root.withdraw()  # Ocultar la ventana A
        self.ventana_b = VentanaB(self.root, self)

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaA(root)
    root.mainloop()





