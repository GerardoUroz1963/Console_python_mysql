from os import system, name
from pickle import FALSE, TRUE
from mysql.connector import Error
from BD.conexion import DAO
import funciones 

def menuPrincipal():
    #Limpiar Pantalla
    # for windows
    """if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    """
    continuar = TRUE
    while (continuar):
        opcionCorrecta = False
        while (not opcionCorrecta):
            print("\n===== MENÚ PRINCIPAL=====\n")
            print("1.- Listado Usuarios")
            print("2.- Nuevo Usuario")
            print("3.- Actualizar Usuario")
            print("4.- Eliminar Usuario")
            print("5.- Salir")
            print("==============================")
            opcion = 0
            opcion = int(input("Selecciones una Opcion: "))

            if opcion <1 or opcion >5:
                print("Opción incorrecta, elija entre 1 y 5  ...")
            elif opcion == 5:
                continuar = False
                print("Gracias por usar el Sistema ")
                break
            else:
                #print("Opcion Correcta")
                ejecutarOpcion(opcion)
                
def ejecutarOpcion(opcion):
    # Instanciar las funciones de Acceso a Datos
    dao = DAO()
    if opcion == 1:
       # Listado de Usuarios
        try:
            usuarios = dao.listaUsuarios()
            if len(usuarios) > 0:
                funciones.listarUsuarios(usuarios)
            else:
                print("No se encontraron Usuarios")
        except Error as ex:
            print(f"Ocurrio un error Listar Usuarios ... {ex}")
    elif opcion == 2:
        #Agregar un Usuario
        usuario = funciones.leerUsuario()
        try:
            dao.grabarUsuario(usuario)
        except Error as ex:
            print("Ocurrio un Error al grabar (1): {0}".format(ex))
    elif opcion == 3:
        #Modificar Usuario
        print("Modificar")
    elif opcion == 4:
        #Eliminar Usuario
        try:
            usuarios = dao.listaUsuarios()
            if len(usuarios) > 0:
                usuarioEliminar = funciones.pedirUsuarioEliminar(usuarios)
                if not(usuarioEliminar == ""):
                    dao.eliminarUsuario(usuarioEliminar)
                else:
                    print("Codigo Usuario no encontrado")
            else:
                print("No se Encontraron Usuarios")
        except Error as ex:
            print("Ocurrio un Error al grabar (1): {0}".format(ex))
        print("Eliminar")
    else:
        print("opcion incorrecta")
    return

menuPrincipal()