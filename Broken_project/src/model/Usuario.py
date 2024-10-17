from BD.Conexion import *

class usuario:
    def guardarUsuario(usuarioId,nombre,apellido,tipo,saldo,fechaDeCreacion):
        try:
            cone= Conexion.ConexionBaseDeDatos()
            cursor= cone.cursor()
            sql="insert into Usuario values(%s,%s,%s,%s,%s,%s)"
            valores=(usuarioId,nombre,apellido,tipo,saldo,fechaDeCreacion)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Usuario registrado")
            cone.close()


        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos{}".format(error))