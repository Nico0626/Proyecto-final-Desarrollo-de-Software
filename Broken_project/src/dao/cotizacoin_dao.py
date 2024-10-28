# src/dao/CotizacionDAO.py
import mysql.connector
from src.model.Cotizacion import Cotizacion
from src.conn.Conexion import Conexiondb

class CotizacionDAO:
    def create(self, cotizacion):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = """
                INSERT INTO Cotizaciones 
                (accion_id, fecha, precio_compra, precio_venta, cantidad_compra, cantidad_venta, minimo_diario, maximo_diario) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (cotizacion.accion_id, cotizacion.fecha, cotizacion.precio_compra, 
                       cotizacion.precio_venta, cotizacion.cantidad_compra, 
                       cotizacion.cantidad_venta, cotizacion.minimo_diario, cotizacion.maximo_diario)
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Cotización registrada.")
        except mysql.connector.Error as error:
            print("Error al crear cotización:", error)
        finally:
            cursor.close()
            cone.close()

    def read(self, cotizacion_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Cotizaciones WHERE cotizacion_id = %s"
            cursor.execute(sql, (cotizacion_id,))
            row = cursor.fetchone()
            if row:
                return Cotizacion(*row)
            return None
        except mysql.connector.Error as error:
            print("Error al leer cotización:", error)
        finally:
            cursor.close()
            cone.close()

    def read_all(self):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Cotizaciones"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [Cotizacion(*row) for row in rows]
        except mysql.connector.Error as error:
            print("Error al leer todas las cotizaciones:", error)
        finally:
            cursor.close()
            cone.close()

    def update(self, cotizacion):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = """
                UPDATE Cotizaciones 
                SET accion_id = %s, fecha = %s, precio_compra = %s, precio_venta = %s, 
                    cantidad_compra = %s, cantidad_venta = %s, minimo_diario = %s, maximo_diario = %s
                WHERE cotizacion_id = %s
            """
            valores = (cotizacion.accion_id, cotizacion.fecha, cotizacion.precio_compra, 
                       cotizacion.precio_venta, cotizacion.cantidad_compra, cotizacion.cantidad_venta, 
                       cotizacion.minimo_diario, cotizacion.maximo_diario, cotizacion.cotizacion_id)
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Cotización actualizada.")
        except mysql.connector.Error as error:
            print("Error al actualizar cotización:", error)
        finally:
            cursor.close()
            cone.close()

    def delete(self, cotizacion_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "DELETE FROM Cotizaciones WHERE cotizacion_id = %s"
            cursor.execute(sql, (cotizacion_id,))
            cone.connection.commit()
            print(cursor.rowcount, "Cotización eliminada.")
        except mysql.connector.Error as error:
            print("Error al eliminar cotización:", error)
        finally:
            cursor.close()
            cone.close()
