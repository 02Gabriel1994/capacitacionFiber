from passlib.context import CryptContext
import Login.validacion.conexion as conexion
contexto = CryptContext(
    schemes=["pbkdf2_sha256"],
    default = "pbkdf2_sha256"
)

#texto = "motorola"
def validarlogin(passw, usuario):

    encriptado=conexion.validarClave(usuario)
# encriptado= contexto.hash(texto)
    return(contexto.verify(passw,encriptado))

