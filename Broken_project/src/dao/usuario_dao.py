import mysql.connector
from mysql.connector import errorcode
from interfaz_dao import dataAccessDAO
from conn import Conexion
from model.Usuario import Usuario


class UsuarioDAO(dataAccessDAO):

    cone= Conexion.Conexion.ConexionBaseDeDatos()

    def create(self, usuario):
        try:
            cone= Conexion.ConexionBaseDeDatos()
            cursor= cone.cursor()
            sql="INSERT INTO Usuario values(%s,%s,%s,null,%s,%s)"
            valores=(usuarioId,nombre,apellido,tipo,fechaDeCreacion)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Usuario registrado")
            cone.close()


        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos{}".format(error))

    def read(self, usuario_id):
        try:
            cone= Conexion.ConexionBaseDeDatos()
            cursor= cone.cursor()
            sql="SELECT * FROM Usuarios WHERE usuario_id= %s"
            cursor.execute(sql,usuario_id)
            cone.commit()
            row = cursor.fetchone() 
            cursor.close()
            if row:
                return Usuario(*row)  
            return None

        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos{}".format(error))

    def read_all(self):
        try:
            cone=Conexion.ConexionBAseDeDatos()
            cursor=cone.cursor()
            sql="SELECT * Usuario"
            cursor.execute(sql)
            cone.commit()
            row = cursor.fetchone() 
            cursor.close()
            if row:
                return Usuario(*row)  
            return None

        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos{}".format(error))



    def update(self, usuario):
        sql = "UPDATE Usuarios SET nombre = ?, apellido = ?, tipo = ?, saldo = ? WHERE usuario_id = ?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (usuario.nombre, usuario.apellido, usuario.tipo, usuario.saldo, usuario.usuario_id))
        self.connection.commit()
        try:
            cone=Conexion.ConexionBAseDeDatos()
            cursor=cone.cursor()
            sql="UPDATE Usuarios SET nombre = ?, apellido = ?, tipo = ?, saldo = ? WHERE usuario_id = ?"
            cursor.execute(sql)
            cone.commit()
            row = cursor.fetchone() 
            cursor.close()
            if row:
                return usuario(*row)  
            return None

        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos{}".format(error))




    def delete(self, usuario_id):
        sql = "DELETE FROM Usuarios WHERE usuario_id = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (usuario_id,))
        self.connection.commit()