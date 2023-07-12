import pyodbc

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
    except Exception as Ex:
        print(Ex)


validarClave("misterio")