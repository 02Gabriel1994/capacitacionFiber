 #"PIL" permite abrir, manipular y guardar imágenes en
 # diferentes formatos, mientras que "ImageTk" proporciona enlaces entre las imágenes de "PIL" y los widgets de imagen
 # de Tkinter. Juntas, estas librerías permiten cargar y mostrar imágenes en una interfaz gráfica de usuario, 
 # realizar operaciones de imagen y manejar eventos relacionados con las imágenes.
 #https://youtu.be/fDyO2vKrSfw
from PIL import ImageTk, Image

def leerImagen(path,size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.BICUBIC)) # esta función carga una imagen, la redimensiona y la convierte en un objeto de imagen compatible con Tkinter utilizando las bibliotecas PIL y ImageTk. Esto es útil para mostrar imágenes en una aplicación de interfaz gráfica de usuario (GUI) de Tkinter

#esta función toma una ventana de Tkinter,
# el ancho y el largo de una aplicación, y centra la ventana en 
# la pantalla utilizando la geometría de la ventana. Esto asegura que la 
# ventana de la aplicación aparezca centrada en la pantalla del usuario.

def centrarVentana(ventana,aplicacionAncho, aplicacionLargo):
    pantallaAncho = ventana.winfo_screenwidth()
    pantallaLargo = ventana.winfo_screenheight()
    x = int((pantallaAncho/2)-(aplicacionAncho/2))
    y = int((pantallaLargo/2)-(aplicacionLargo/2))
    return ventana.geometry(f"{aplicacionAncho}x{aplicacionLargo}+{x}+{y}")