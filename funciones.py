from BD.conexion import DAO
def listarUsuarios(usuarios):
    print("\n===Usuarios===\n")
    contador = 1
    for usu in usuarios:
        datos = "{0}. CodUsu: {1} / Nombre: {2} / Dirección {3} / E-Mail: {4}"
        print (datos.format(contador, usu[0], usu[1], usu[2], usu[3]))
        contador += 1
    print ("=======================")

def leerUsuario():
    dao = DAO()
    codigoCorrecto = False
    while(codigoCorrecto == False):
        codigo = int(input("Codigo de Usuario: "))
        if codigo >0 and codigo < 999999:
            if dao.existeUsuario(codigo):
                print(f"leerUsuario: Ya existe Usuario {codigo}")
                codigoCorrecto = False
            else:
                codigoCorrecto = True
        else:
            print("Ingrese un Codigo >0 y < 999999")
    nombreCorrecto = False
    while(nombreCorrecto == False):
        nombre = input("Nombre Usuario: ")
        if len(nombre) >0 and len(nombre)  < 100:
            nombreCorrecto = True
        else:
            print("Ingrese un Codigo >0 y < 999999")

        dire = input("Direccion Usuario:")
        email = input("Email Usuario: ")
        usuario = (codigo, nombre, dire, email)
        return usuario

def pedirUsuarioEliminar(usuarios):
    listarUsuarios(usuarios)
    existeUsuario = False
    usuarioEliminar = int(input("Ingrese el Codigo del Usuario a Eliminar"))
    for usu in usuarios:
        if usu[0] == usuarioEliminar:
            existeUsuario = True
            break
    if not existeUsuario:
        usuarioEliminar = ""
    return usuarioEliminar
