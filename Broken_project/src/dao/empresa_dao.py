import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


import mysql.connector
from mysql.connector import errorcode
from src.dao.interfaz_dao import dataAccessDAO
from src.model.Empresa import empresa
from src.conn.Conexion import Conexiondb


class UsuarioDAO(dataAccessDAO):

    def create(self, empresa):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ArgBroker')  # Asegúrate de pasar los parámetros necesarios
            cone.conectar()  # Debe devolver la conexión
            cursor = cone.connection.cursor()
            sql = "INSERT INTO Empresas VALUES (null, %s, %s, %s, null, %s)"
            valores = (empresa.nombre, empresa.cuit, empresa.sector, empresa.fecha_de_creacion)
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

    def read(self, empresa_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Empresas WHERE empresa_id = %s"
            cursor.execute(sql, (empresa_id,))
            row = cursor.fetchone()
            if row:
                return empresa(*row)
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
            empresas = [empresa(*row) for row in rows]  # Crear lista de objetos Usuario
            return empresas
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            if cone.connection:
                cone.close()

    def update(self, empresa):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = """
                UPDATE Usuario 
                SET nombre_empresa = %s,sector= %s
                WHERE empresa_id = %s
            """
            valores = (empresa.nombre, empresa.sector, empresa.empresa_id)
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

    def delete(self, empresa_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "DELETE FROM Empresas WHERE empresa_id = %s"
            cursor.execute(sql, (empresa_id,))
            cone.connection.commit()
            print(cursor.rowcount, "Empresa eliminado")
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))
        finally:
            if cursor:
                cursor.close()
            if cone.connection:
                cone.close()