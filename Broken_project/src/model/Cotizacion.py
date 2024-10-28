


class Cotizacion:
    def __init__(self, cotizacion_id, accion_id, fecha, precio_compra, precio_venta, 
                 cantidad_compra, cantidad_venta, minimo_diario, maximo_diario):
        self.__cotizacion_id = cotizacion_id
        self.__accion_id = accion_id
        self.fecha = fecha
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.cantidad_compra = cantidad_compra
        self.cantidad_venta = cantidad_venta
        self.minimo_diario = minimo_diario
        self.maximo_diario = maximo_diario

    @property
    def cotizacion_id(self):
        return self.__cotizacion_id

    @property
    def accion_id(self):
        return self.__accion_id


    @accion_id.setter
    def accion_id(self, valor):
        self.__accion_id = valor

    def __repr__(self):
        return (f"Cotizacion({self.cotizacion_id}, {self.accion_id}, {self.fecha}, {self.precio_compra}, "
                f"{self.precio_venta}, {self.cantidad_compra}, {self.cantidad_venta}, "
                f"{self.minimo_diario}, {self.maximo_diario})")
