import mysql.connector
from mysql.connector import errorcode
from dao.interfaz_dao import dataAccessDAO
from model.Usuario import Usuario
from conn.Conexion import Conexiondb

class UsuarioDAO(dataAccessDAO):

    def create(self, usuario):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ArgBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "INSERT INTO Usuarios VALUES (null, %s, %s, %s,%s, %s, %s, %s)"
            valores = (usuario.nombre, usuario.apellido,usuario.documento, usuario.mail,usuario.contraseña,usuario.saldo, usuario.fecha_creacion)
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
            sql = "SELECT * FROM Usuarios WHERE usuario_id = %s"
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

    def read_por_mail(self, mail):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Usuarios WHERE mail = %s"
            cursor.execute(sql, (mail,))
            row = cursor.fetchone()
            if row:
                return Usuario(
                usuario_id=row[0],
                nombre=row[1],
                apellido=row[2],
                documento=row[3],
                mail=row[4],
                contraseña=row[5],
                saldo=row[6],
                fecha_creacion=row[7]
            )
            return  None
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
            sql = "SELECT * FROM Usuarios"
            cursor.execute(sql)
            rows = cursor.fetchall()
            usuarios = [Usuario(*row) for row in rows]
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
                UPDATE Usuarios 
                SET nombre = %s, apellido = %s, saldo = %s 
                WHERE usuario_id = %s
            """
            valores = (usuario.nombre, usuario.apellido, usuario.saldo, usuario.usuario_id)
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
            sql = "DELETE FROM Usuarios WHERE usuario_id = %s"
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

    def autenticar(self, mail, contrasena):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Usuarios WHERE mail = %s AND contrasena = %s"
            cursor.execute(sql, (mail, contrasena))
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