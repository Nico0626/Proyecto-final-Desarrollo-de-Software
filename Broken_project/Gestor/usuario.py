class Usuario:
    def __init__(self, id_usuario, nombre, apellido, saldo=1000000.00):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = saldo

    def actualizar_saldo(self, monto):
        self.saldo += monto
        print(f"Nuevo saldo de {self.nombre}: {self.saldo}")
