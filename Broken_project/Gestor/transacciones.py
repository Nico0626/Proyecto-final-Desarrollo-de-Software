class Transaccion:
    def __init__(self, id_transaccion, id_usuario, id_broker, id_accion, tipo, cantidad, precio, comision):
        self.id_transaccion = id_transaccion
        self.id_usuario = id_usuario
        self.id_broker = id_broker
        self.id_accion = id_accion
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio = precio
        self.comision = comision

    def ejecutar(self, usuario, accion):
        total = (self.cantidad * self.precio) + self.comision
        if usuario.saldo >= total:
            usuario.actualizar_saldo(-total)
            print(f"Transacción {self.tipo} realizada: {self.cantidad} acciones de {accion.simbolo}")
        else:
            print("Fondos insuficientes")
