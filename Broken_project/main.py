from Finanzas.acciones import Accion
from Gestor.usuario import Usuario
from Gestor.transacciones import Transaccion
from Gestor.portafolio import Portafolio
from Registro.perfil_inversor import PerfilInversor

# Crear un usuario
usuario1 = Usuario(1, "José", "Tiranti", 10000.00)

# Crear una acción
accion1 = Accion(1, 1, "AAPL", 150.00, 100, 140.00, 150.00)

# Crear un portafolio y agregar acciones
portafolio1 = Portafolio(usuario1.id_usuario)
portafolio1.agregar_accion("AAPL", 10)

# Ejecutar una transacción de compra
transaccion1 = Transaccion(1, usuario1.id_usuario, 1, 1, "compra", 5, 150.00, 10.00)
transaccion1.ejecutar(usuario1, accion1)

# Mostrar portafolio
portafolio1.mostrar_portafolio()

# Crear y mostrar un perfil inversor
perfil1 = PerfilInversor(usuario1.id_usuario, "medio", "larga")
perfil1.mostrar_perfil()
