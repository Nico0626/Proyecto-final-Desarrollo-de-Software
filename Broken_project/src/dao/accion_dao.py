# src/dao/AccionDAO.py
import mysql.connector
from src.model.Accion import Accion
from src.conn.Conexion import Conexiondb

class AccionDAO:
    def create(self, accion):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = """
                INSERT INTO Acciones (simbolo, empresa_id, ultimo_operado, cantidad_compra_diaria, 
                                      precio_compra_actual, precio_venta_actual, cantidad_venta_diaria, 
                                      apertura, minimo_diario, maximo_diario, ultimo_cierre, fecha_actualizacion)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                accion.simbolo,
                accion.empresa_id,
                accion.ultimo_operado,
                accion.cantidad_compra_diaria,
                accion.precio_compra_actual,
                accion.precio_venta_actual,
                accion.cantidad_venta_diaria,
                accion.apertura,
                accion.minimo_diario,
                accion.maximo_diario,
                accion.ultimo_cierre,
                accion.fecha_actualizacion
            )
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Acción registrada.")
        except mysql.connector.Error as error:
            print("Error al crear acción:", error)
        finally:
            cursor.close()
            cone.close()

    def read(self, accion_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Acciones WHERE accion_id = %s"
            cursor.execute(sql, (accion_id,))
            row = cursor.fetchone()
            if row:
                return Accion(*row)
            return None
        except mysql.connector.Error as error:
            print("Error al leer acción:", error)
        finally:
            cursor.close()
            cone.close()

    def read_all(self):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "SELECT * FROM Acciones"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [Accion(*row) for row in rows]
        except mysql.connector.Error as error:
            print("Error al leer todas las acciones:", error)
        finally:
            cursor.close()
            cone.close()

    def update(self, accion):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = """
                UPDATE Acciones 
                SET simbolo = %s, empresa_id = %s, ultimo_operado = %s, cantidad_compra_diaria = %s,
                    precio_compra_actual = %s, precio_venta_actual = %s, cantidad_venta_diaria = %s, 
                    apertura = %s, minimo_diario = %s, maximo_diario = %s, ultimo_cierre = %s, 
                    fecha_actualizacion = %s
                WHERE accion_id = %s
            """
            valores = (
                accion.simbolo,
                accion.empresa_id,
                accion.ultimo_operado,
                accion.cantidad_compra_diaria,
                accion.precio_compra_actual,
                accion.precio_venta_actual,
                accion.cantidad_venta_diaria,
                accion.apertura,
                accion.minimo_diario,
                accion.maximo_diario,
                accion.ultimo_cierre,
                accion.fecha_actualizacion,
                accion.accion_id
            )
            cursor.execute(sql, valores)
            cone.connection.commit()
            print(cursor.rowcount, "Acción actualizada.")
        except mysql.connector.Error as error:
            print("Error al actualizar acción:", error)
        finally:
            cursor.close()
            cone.close()

    def delete(self, accion_id):
        try:
            cone = Conexiondb('localhost', 'root', 'NM260621', 'ARGBroker')
            cone.conectar()
            cursor = cone.connection.cursor()
            sql = "DELETE FROM Acciones WHERE accion_id = %s"
            cursor.execute(sql, (accion_id,))
            cone.connection.commit()
            print(cursor.rowcount, "Acción eliminada.")
        except mysql.connector.Error as error:
            print("Error al eliminar acción:", error)
        finally:
            cursor.close()
            cone.close()
