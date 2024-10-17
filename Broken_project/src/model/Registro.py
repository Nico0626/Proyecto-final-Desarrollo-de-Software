from ..BD.Conexion import *
import time

def registro():
    nombre=input("Ingrese su nombre ")
    apellido=input("Ingrese su apellido")
    usuario_id=input("Ingrese su nombre de usuario")
    tipo=""
    while True:
        respuesta=int(input("""---Ingrese el numero que corresponda a su respuesta---\n
                        Usted es:\n 
                        1.Persona individual \n 
                        2.Empresa \n
                        3.Institucion """))
        if respuesta!=1 or 2 or 3:
            print("ERROR:ingrese un valor valido")
            return False 
    if respuesta==1:
        tipo="individual"
    elif respuesta==2:
        tipo="empresa"
    elif respuesta==3:
        tipo="institucion"

    fechaDeCreacion=time.localtime()
    guardarUsuario(usuario_id,nombre,apellido,tipo,fechaDeCreacion)



def guardarUsuario(usuarioId,nombre,apellido,tipo,fechaDeCreacion):
    try:
        cone= Conexion.ConexionBaseDeDatos()
        cursor= cone.cursor()
        sql="insert into Usuario values(%s,%s,%s,null,%s,%s)"
        valores=(usuarioId,nombre,apellido,tipo,fechaDeCreacion)
        cursor.execute(sql,valores)
        cone.commit()
        print(cursor.rowcount,"Usuario registrado")
        cone.close()


    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos{}".format(error))

