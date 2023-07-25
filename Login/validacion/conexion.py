import pyodbc
from tkinter import messagebox
import openpyxl
import Login.Forms.master as ms
def conexionsql():
    try:
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-26G83K4\SQLEXPRESS;DATABASE=CAPACITACION;UID=sa;PWD=Motorola')
        return  conexion
        # cursor =conexion.cursor()
        # cursor.execute("Select * from usuarios;")
        # row = cursor.fetchone()
        # print(row)
    except Exception as Ex:
        print(Ex)

def validarClave(user):
    try:
        con = conexionsql()
        cursor =con.cursor()
        cursor.execute(f"Select contraseña from usuarios where usuario = '{user}' ;")
        row = cursor.fetchone()
        for i in row:
            
            return i
        con.close
    except Exception as Ex:
        print(Ex)


validarClave("misterio")

def buscar_Datos(sgid, cedula):
    if not sgid == "":
        buscar = sgid
    else:
        if not cedula == "":
           buscar  = int(cedula)
        else: 
            messagebox.showinfo("Información", "Debe ingresar un dato para buscar")
            return
    encontrado = False

    try:
        libro_excel = openpyxl.load_workbook("F:/Documentos/PROYECTOS/pruebas/Nuevo Hoja de cálculo de Microsoft Excel.xlsx")
        hoja = libro_excel.active
     

        for fila in hoja.iter_rows(min_row=2, values_only=True):
            
            if fila[0] == buscar:
                encontrado = True
                return fila
                

        if not encontrado:
            messagebox.showinfo("Información", f"No se encontró la cédula {buscar} en el archivo.")
        print(encontrado)
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al abrir el archivo: {e}")