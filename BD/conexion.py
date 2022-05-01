
import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'sistema'
            )

        except Error as ex:
                   print("Error al intentar la conexion: {0}".format(ex))

    def listaUsuarios(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM usuarios ORDER BY codUsu asc")
                resultados=cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        else:
            print("No se Conecto 1")
    
    def grabarUsuario(self, usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO usuarios (codUsu, nombreUsu, dirUsu, email) VALUES ({0},'{1}','{2}','{3}')"
                cursor.execute(sql.format(usuario[0],usuario[1], usuario[2], usuario[3]))
                self.conexion.commit()
                print("Usuario Grabado")        
            except Error as ex:
                print("Error al grabar Usuario(2): {0}".format(ex))

    def eliminarUsuario(self, usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM usuarios WHERE codUsu = {0}"
                cursor.execute(sql.format(usuario))
                self.conexion.commit()
                print("Usuario Eliminado")        
            except Error as ex:
                print("Error al grabar Usuario(2): {0}".format(ex))
    
    def existeUsuario(self,usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT (codUsu) FROM usuarios WHERE codUsu = " + str(usuario) +";"
                print(f"SQL= {sql}")
                cursor.execute(sql)
                data = cursor.fetchall()
                if len(data) > 0:
                    print("existeUsuario: Ya existe usuario")     
                    # Imprimir los Datos del Usuario
                    return True
                else:
                    print("existeUsuario: no hay datos")
                    return False
            except Error as ex:
                print("Error al grabar Usuario(2): {0}".format(ex))