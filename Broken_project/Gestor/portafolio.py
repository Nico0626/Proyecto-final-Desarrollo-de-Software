class Portafolio:
    def __init__(self, id_usuario):
        self.id_usuario = id_usuario
        self.acciones = {}  # Diccionario {simbolo: cantidad}

    def agregar_accion(self, simbolo, cantidad):
        if simbolo in self.acciones:
            self.acciones[simbolo] += cantidad
        else:
            self.acciones[simbolo] = cantidad
        print(f"{cantidad} acciones de {simbolo} agregadas al portafolio.")

    def mostrar_portafolio(self):
        print(f"Portafolio del usuario {self.id_usuario}:")
        for simbolo, cantidad in self.acciones.items():
            print(f"{simbolo}: {cantidad} acciones")
