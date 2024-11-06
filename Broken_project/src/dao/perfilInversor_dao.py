import mysql.connector
from model.PerfilInversor import PerfilInversor
from conn.Conexion import Conexiondb

class PerfilInversorDAO:
    def create(self, perfil_inversor):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = """
                INSERT INTO PerfilInversor (usuario_id, tolerancia_riesgo, duracion_inversion)
                VALUES (%s, %s, %s)
            """
            valores = (perfil_inversor.usuario_id, perfil_inversor.tolerancia_riesgo, perfil_inversor.duracion_inversion)
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Perfil de inversor registrado.")
        except mysql.connector.Error as error:
            print("Error al crear perfil de inversor:", error)
        finally:
            cursor.close()
            cone.close()

    def read(self, perfil_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM PerfilInversor WHERE perfil_id = %s"
            cursor.execute(sql, (perfil_id,))
            row = cursor.fetchone()
            if row:
                return PerfilInversor(*row)
            return None
        except mysql.connector.Error as error:
            print("Error al leer perfil de inversor:", error)
        finally:
            cursor.close()
            cone.close()

    def read_all(self):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM PerfilInversor"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [PerfilInversor(*row) for row in rows]
        except mysql.connector.Error as error:
            print("Error al leer todos los perfiles de inversor:", error)
        finally:
            cursor.close()
            cone.close()

    def update(self, perfil_inversor):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = """
                UPDATE PerfilInversor 
                SET tolerancia_riesgo = %s, duracion_inversion = %s
                WHERE perfil_id = %s
            """
            valores = (perfil_inversor.tolerancia_riesgo, perfil_inversor.duracion_inversion, perfil_inversor.perfil_id)
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Perfil de inversor actualizado.")
        except mysql.connector.Error as error:
            print("Error al actualizar perfil de inversor:", error)
        finally:
            cursor.close()
            cone.close()

    def delete(self, perfil_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "DELETE FROM PerfilInversor WHERE perfil_id = %s"
            cursor.execute(sql, (perfil_id,))
            cone.connection.commit()
            print(cursor.rowcount, "Perfil de inversor eliminado.")
        except mysql.connector.Error as error:
            print("Error al eliminar perfil de inversor:", error)
        finally:
            cursor.close()
            cone.close()
