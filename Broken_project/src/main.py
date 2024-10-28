import sys
import os
from datetime import datetime
from decimal import Decimal

# Agregar el directorio src al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from dao.usuario_dao import UsuarioDAO
from dao.accion_dao import AccionDAO
from dao.transaccion_dao import TransaccionDAO
from dao.portafolio_dao import PortafolioDAO
from model.Usuario import Usuario
from model.Accion import Accion

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    cuil = input("Ingrese su CUIL: ")
    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")
    
    nuevo_usuario = Usuario(usuario_id=None, nombre=nombre, apellido=apellido, tipo='individual', 
                            cuil=cuil, email=email, contrasena=contrasena,  # Asegúrate de agregar la contraseña
                            saldo=Decimal('1000000.00'), fecha_creacion=datetime.now())
    
    usuario_dao = UsuarioDAO()
    usuario_dao.create(nuevo_usuario)
    print("Usuario registrado con éxito.")

def iniciar_sesion():
    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")
    
    usuario_dao = UsuarioDAO()  # Crear instancia de UsuarioDAO
    usuario = usuario_dao.autenticar(email, contrasena)
    
    if usuario:
        print(f"Bienvenido, {usuario.nombre}.")
        return usuario
    else:
        print("Credenciales incorrectas.")
        return None

def mostrar_datos_cuenta(usuario):
    print(f"Saldo: {usuario.saldo}")
    # Aquí puedes agregar lógica para mostrar el total invertido y el rendimiento total.

def listar_activos(usuario):
    portafolio_dao = PortafolioDAO()
    acciones = portafolio_dao.read(usuario.usuario_id)
    
    for accion in acciones:
        print(f"Nombre: {accion.simbolo}, Cantidad: {accion.cantidad}, Precio Actual: {accion.precio_compra_actual}")

def comprar_acciones(usuario):
    simbolo = input("Ingrese el símbolo de la acción a comprar: ")
    cantidad = int(input("Ingrese la cantidad de acciones a comprar: "))
    
    accion_dao = AccionDAO()
    accion = accion_dao.read(simbolo)
    
    if accion and cantidad > 0:
        total_precio = cantidad * accion.precio_compra_actual
        if usuario.saldo >= total_precio:
            usuario.saldo -= total_precio
            transaccion_dao = TransaccionDAO()
            transaccion_dao.create(usuario.usuario_id, accion.accion_id, 'compra', cantidad, accion.precio_compra_actual)
            print("Compra realizada con éxito.")
        else:
            print("No tienes suficiente saldo.")
    else:
        print("Acción no encontrada o cantidad no válida.")

def menu_principal():
    while True:
        print("*** Menú Principal ***")
        print("1. Registrar Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            usuario = iniciar_sesion()
            if usuario:
                while True:
                    print("*** Menú de Usuario ***")
                    print("1. Mostrar Datos de Cuenta")
                    print("2. Listar Activos del Portafolio")
                    print("3. Comprar Acciones")
                    print("4. Salir")

                    opcion_usuario = input("Seleccione una opción: ")
                    if opcion_usuario == "1":
                        mostrar_datos_cuenta(usuario)
                    elif opcion_usuario == "2":
                        listar_activos(usuario)
                    elif opcion_usuario == "3":
                        comprar_acciones(usuario)
                    elif opcion_usuario == "4":
                        break
                    else:
                        print("Opción no válida.")
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    menu_principal()
