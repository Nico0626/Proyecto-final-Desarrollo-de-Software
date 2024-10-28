from decimal import Decimal
import datetime

class Accion:
    def __init__(self, accion_id=None, simbolo="", empresa_id=None, ultimo_operado=Decimal('0.00'), cantidad_compra_diaria=0, 
                 precio_compra_actual=Decimal('0.00'), precio_venta_actual=Decimal('0.00'), cantidad_venta_diaria=0, 
                 apertura=Decimal('0.00'), minimo_diario=Decimal('0.00'), maximo_diario=Decimal('0.00'), 
                 ultimo_cierre=Decimal('0.00'), fecha_actualizacion=None):
        self.__accion_id = accion_id
        self.__simbolo = simbolo
        self.__empresa_id = empresa_id
        self.__ultimo_operado = ultimo_operado
        self.__cantidad_compra_diaria = cantidad_compra_diaria
        self.__precio_compra_actual = precio_compra_actual
        self.__precio_venta_actual = precio_venta_actual
        self.__cantidad_venta_diaria = cantidad_venta_diaria
        self.__apertura = apertura
        self.__minimo_diario = minimo_diario
        self.__maximo_diario = maximo_diario
        self.__ultimo_cierre = ultimo_cierre
        self.__fecha_actualizacion = fecha_actualizacion if fecha_actualizacion is not None else datetime.now()

    @property
    def accion_id(self):
        return self.__accion_id

    @property
    def simbolo(self):
        return self.__simbolo

    @simbolo.setter
    def simbolo(self, valor):
        self.__simbolo = valor

    @property
    def empresa_id(self):
        return self.__empresa_id

    @property
    def ultimo_operado(self):
        return self.__ultimo_operado

    @ultimo_operado.setter
    def ultimo_operado(self, valor):
        self.__ultimo_operado = valor

    @property
    def cantidad_compra_diaria(self):
        return self.__cantidad_compra_diaria

    @property
    def precio_compra_actual(self):
        return self.__precio_compra_actual

    @property
    def precio_venta_actual(self):
        return self.__precio_venta_actual

    @property
    def cantidad_venta_diaria(self):
        return self.__cantidad_venta_diaria

    @property
    def apertura(self):
        return self.__apertura

    @property
    def minimo_diario(self):
        return self.__minimo_diario

    @property
    def maximo_diario(self):
        return self.__maximo_diario

    @property
    def ultimo_cierre(self):
        return self.__ultimo_cierre

    @property
    def fecha_actualizacion(self):
        return self.__fecha_actualizacion

    def __repr__(self):
        return f"({self.accion_id}, '{self.simbolo}', {self.empresa_id}, {self.ultimo_operado}, {self.precio_compra_actual}, {self.precio_venta_actual}, '{self.fecha_actualizacion}')"
