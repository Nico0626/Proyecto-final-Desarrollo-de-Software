class PerfilInversor:
    def __init__(self, id_usuario, tolerancia_riesgo, duracion_inversion):
        self.id_usuario = id_usuario
        self.tolerancia_riesgo = tolerancia_riesgo
        self.duracion_inversion = duracion_inversion

    def mostrar_perfil(self):
        print(f"Perfil del usuario {self.id_usuario}:")
        print(f"Tolerancia al riesgo: {self.tolerancia_riesgo}")
        print(f"Duración de inversión: {self.duracion_inversion}")
