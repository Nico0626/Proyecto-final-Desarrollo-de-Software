import sys
import os
from datetime import datetime
from decimal import Decimal
from src.dao.usuario_dao import UsuarioDAO
from src.dao.portafolio_dao import PortafolioDAO
from src.dao.accion_dao import AccionDAO
from src.dao.transaccion_dao import TransaccionDAO
from src.model.Usuario import Usuario

# Agregar el directorio raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

def mostrar_menu():
    print("*** Menú Principal ***")
    print("1. Registrar Inversor")
    print("2. Iniciar Sesión")
    print("3. Salir")

def mostrar_menu_usuario():
    print("*** Menú Usuario ***")
    print("1. Mostrar datos de la cuenta")
    print("2. Listar activos del portafolio")
    print("3. Comprar acción")
    print("4. Vender acción")
    print("5. Cerrar sesión")

def registrar_inversor(usuario_dao):
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    cuil = input("Ingrese su CUIL: ")
    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")

    usuario = Usuario(usuario_id=None, nombre=nombre, apellido=apellido, cuil=cuil, email=email, contrasena=contrasena, saldo=Decimal('1000000.00'), fecha_creacion=datetime.now())
    usuario_dao.create(usuario)
    print("Inversor registrado con éxito.")

def iniciar_sesion(usuario_dao):
    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")
    usuario = usuario_dao.read_by_email(email)

    if usuario and usuario.contrasena == contrasena:
        print(f"Bienvenido, {usuario.nombre} {usuario.apellido}")
        return usuario
    else:
        print("Email o contraseña incorrectos.")
        return None

def mostrar_datos_cuenta(usuario):
    print(f"Nombre: {usuario.nombre} {usuario.apellido}")
    print(f"Saldo: {usuario.saldo}")

def listar_activos(portafolio_dao, usuario_id):
    activos = portafolio_dao.read(usuario_id)
    if not activos:
        print("No tienes activos en tu portafolio.")
        return

    for activo in activos:
        print(f"Activos: {activo.nombre} - Cantidad: {activo.cantidad} - Precio Actual: {activo.precio_actual} - Rendimiento: {activo.rendimiento}")

def comprar_accion(usuario, portafolio_dao, accion_dao, transaccion_dao):
    simbolo = input("Ingrese el símbolo de la acción que desea comprar: ")
    cantidad = int(input("Ingrese la cantidad de acciones a comprar: "))
    
    accion = accion_dao.read_by_simbolo(simbolo)

    if accion and usuario.saldo >= accion.precio_compra * cantidad:
       
        transaccion_dao.create(usuario.usuario_id, accion.accion_id, 'compra', cantidad, accion.precio_compra)
        
        
        usuario.saldo -= accion.precio_compra * cantidad
        portafolio_dao.update(usuario.usuario_id, simbolo, cantidad)

        print("Compra realizada con éxito.")
    else:
        print("Fondos insuficientes o acción no encontrada.")

def vender_accion(usuario, portafolio_dao, accion_dao, transaccion_dao):
    simbolo = input("Ingrese el símbolo de la acción que desea vender: ")
    cantidad = int(input("Ingrese la cantidad de acciones a vender: "))
    
  
    activo = portafolio_dao.read_by_simbolo(usuario.usuario_id, simbolo)

    if activo and activo.cantidad >= cantidad:
        accion = accion_dao.read_by_simbolo(simbolo)

        
        transaccion_dao.create(usuario.usuario_id, accion.accion_id, 'venta', cantidad, accion.precio_venta)

       
        usuario.saldo += accion.precio_venta * cantidad
        portafolio_dao.update(usuario.usuario_id, simbolo, -cantidad)

        print("Venta realizada con éxito.")
    else:
        print("No tienes suficientes acciones para vender.")

def main():
    usuario_dao = UsuarioDAO()
    portafolio_dao = PortafolioDAO()
    accion_dao = AccionDAO()
    transaccion_dao = TransaccionDAO()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_inversor(usuario_dao)
        elif opcion == "2":
            usuario = iniciar_sesion(usuario_dao)
            if usuario:
                while True:
                    mostrar_menu_usuario()
                    opcion_usuario = input("Seleccione una opción: ")

                    if opcion_usuario == "1":
                        mostrar_datos_cuenta(usuario)
                    elif opcion_usuario == "2":
                        listar_activos(portafolio_dao, usuario.usuario_id)
                    elif opcion_usuario == "3":
                        comprar_accion(usuario, portafolio_dao, accion_dao, transaccion_dao)
                    elif opcion_usuario == "4":
                        vender_accion(usuario, portafolio_dao, accion_dao, transaccion_dao)
                    elif opcion_usuario == "5":
                        print("Cerrando sesión.")
                        break
                    else:
                        print("Opción no válida.")
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    main()
