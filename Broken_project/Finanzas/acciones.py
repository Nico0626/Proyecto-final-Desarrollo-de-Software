class Accion:
    def __init__(self, id_accion, id_empresa, simbolo, ultimo_operado, cantidad_compra, precio_compra, precio_venta):
        self.id_accion = id_accion
        self.id_empresa = id_empresa
        self.simbolo = simbolo
        self.ultimo_operado = ultimo_operado
        self.cantidad_compra = cantidad_compra
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta

    def actualizar_precio(self, nuevo_precio):
        self.ultimo_operado = nuevo_precio
        print(f"El precio de {self.simbolo} ha sido actualizado a {nuevo_precio}")
