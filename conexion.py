import mysql.connector
from mysql.connector import Error
def conectar():
    try:
        conexion = mysql.connector.connect(port='3306',user='root',password='sql24jmm*',database='broker',host='localhost')

        if conexion.is_connected():
            print("se ha conectado con la base de datos broker")
            return conexion
    except Error as error:
        print(f"error al intentar conectar con la base de datos: {error}")
        return None
if __name__ == "__main__":
    conexion = conectar()
    if conexion:
        conexion.close()
        print("Conexión cerrada")

def seleccion_datos():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre FROM Usuario")
            resultados = cursor.fetchall()
            for fila in resultados:
                print(fila)
        except Error as e:
            print(f"Error al seleccionar datos: {e}")
        finally:
            cursor.close()
            conexion.close()

def agregar_usuario(id_usuario,nombre,apellido,saldo):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "INSERT INTO Usuario (id_usuario, nombre, apellido,saldo) VALUES (%s, %s,%s, %s)"
            cursor.execute(query,(id_usuario,nombre,apellido,saldo))
            conexion.commit()
            print("se ha agregado un nuevo cliente")
        except Error as error:
            print(f"ha habido un error{error}")
        finally:
            cursor.close()
            conexion.close()

def actualizar_datos(id_empresa, nombre, cuit, sector):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "UPDATE empresas SET nombre = %s, cuit = %s, sector = %s WHERE id_empresa = %s"
            cursor.execute(query, (nombre, cuit, sector, id_empresa))
            conexion.commit()
            print("Se han actualizado los datos")
        except Error as error:
            print(f"Ha habido un error: {error}")
        finally:
            cursor.close()
            conexion.close()

def eliminar_dato(id_usuario):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "DELETE FROM Usuario WHERE id_usuario = %s"
            cursor.execute(query, (id_usuario,))
            conexion.commit()
            print("se ha eliminado un usuario")
        except Error as error:
            print(f"Error al eliminar cliente: {error}")
        finally:
            cursor.close()
            conexion.close()

if __name__ == "__main__":
    seleccion_datos()
    eliminar_dato(8)
    agregar_usuario('123','juan','machado','100000')
    actualizar_datos("12","Oracle",12345,"tecnologico")

