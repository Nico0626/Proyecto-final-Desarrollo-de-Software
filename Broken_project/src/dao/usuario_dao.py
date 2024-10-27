import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


import mysql.connector
from mysql.connector import errorcode
from src.dao.interfaz_dao import dataAccessDAO
from src.model.Usuario import Usuario
from src.conn.Conexion import Conexiondb


class UsuarioDAO(dataAccessDAO):

    def create(self, usuario):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ArgBroker')  # Asegúrate de pasar los parámetros necesarios
            cone.conectar()  # Debe devolver la conexión
            cursor = cone.connection.cursor()
            sql = "INSERT INTO Usuario VALUES (null, %s, %s, %s,%s, null, %s)"
            valores = (usuario.nombre, usuario.apellido,usuario.gmail, usuario.tipo, usuario.fechaDeCreacion)
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Usuario registrado")
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            if cone.connection:
                cone.close()

    def read(self, usuario_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Usuario WHERE usuario_id = %s"
            cursor.execute(sql, (usuario_id,))
            row = cursor.fetchone()
            if row:
                return Usuario(*row)
            return None
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            if cone.connection:
                cone.close()

    def read_all(self):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Usuario"
            cursor.execute(sql)
            rows = cursor.fetchall()
            usuarios = [Usuario(*row) for row in rows]  # Crear lista de objetos Usuario
            return usuarios
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            if cone.connection:
                cone.close()

    def update(self, usuario):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = """
                UPDATE Usuario 
                SET nombre = %s, apellido = %s, tipo = %s, saldo = %s 
                WHERE usuario_id = %s
            """
            valores = (usuario.nombre, usuario.apellido, usuario.tipo, usuario.saldo, usuario.usuario_id)
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Usuario actualizado")
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            if cone.connection:
                cone.close()

    def delete(self, usuario_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "DELETE FROM Usuario WHERE usuario_id = %s"
            cursor.execute(sql, (usuario_id,))
            cone.connection.commit()
            print(cursor.rowcount, "Usuario eliminado")
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            if cone.connection:
                cone.close()