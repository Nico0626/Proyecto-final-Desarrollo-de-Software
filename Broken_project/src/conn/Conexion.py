import mysql.connector 

class Conexion:

    def ConexionBaseDeDatos():
        try:
            conexion=mysql.connector.connect(
                usuer='root',
                password='NM2606',
                host='127.0.0.1',                
                database='ARGBroke',
                port='3306'
            )
            print("conxecion correcta")
            return conexion
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos {}".format(error))
            return conexion
