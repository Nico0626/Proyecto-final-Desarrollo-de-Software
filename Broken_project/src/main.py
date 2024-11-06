from datetime import datetime
from decimal import Decimal
from dao.usuario_dao import UsuarioDAO
from dao.portafolio_dao import PortafolioDAO
from dao.accion_dao import AccionDAO
from dao.transaccion_dao import TransaccionDAO
from model.Usuario import Usuario

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Registrar Inversor")
    print("2. Iniciar Sesión")
    print("3. Salir")

def mostrar_menu_usuario():
    print("\n--- Menú Usuario ---")
    print("1. Mostrar datos de la cuenta")
    print("2. Listar activos del portafolio")
    print("3. Comprar acción")
    print("4. Vender acción")
    print("5. Cerrar sesión")

def registrar_inversor(usuario_dao):
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    documento = input("Ingrese Documento: ")
    mail = input("Ingrese Mail: ")
    contraseña = input("Ingrese contraseña: ")
    usuario = Usuario(usuario_id=None, nombre=nombre, apellido=apellido, documento=documento, mail=mail, contraseña=contraseña, saldo=Decimal('1000000.00'), fecha_creacion=datetime.now())
    usuario_dao.create(usuario)
    print("Inversor registrado con éxito.")

def iniciar_sesion(usuario_dao):
    mail = input("Ingrese su mail: ")
    contraseña = input("Ingrese su contraseña: ")   
    usuario = usuario_dao.read_por_mail(mail)   
    if usuario and usuario.contraseña == contraseña:
        print(f"\nBienvenido, {usuario.nombre} {usuario.apellido}")
        return usuario
    else:
        print("Mail o contraseña incorrectos.")
        return None

def mostrar_datos_cuenta(usuarios):
    print(f" \n Nombre: {usuarios.nombre} \n Apellido: {usuarios.apellido} \n Documento: {usuarios.documento} \n Saldo: {usuarios.saldo} \n Correo: {usuarios.mail} \n Fecha creacion: {usuarios.fecha_creacion}")

def listar_activos(portafolio_dao, usuario_id):
    activos = portafolio_dao.read(usuario_id)
    if not activos:
        print("No tienes activos en tu portafolio.")
        return
    for activo in activos:
        print(f"\nSimbolo: {activo.simbolo}\nCantidad: {activo.cantidad} ")

def comprar_accion(usuario, portafolio_dao, accion_dao, transaccion_dao):
    simbolo = input("Ingrese el símbolo de la acción que desea comprar: ")
    cantidad = int(input("Ingrese la cantidad de acciones a comprar: "))
    comision = 1.5
    accion = accion_dao.read_by_simbolo(simbolo)
    if accion is None:
        print("La acción con ese símbolo no existe.")
        return    
    total_precio = accion.precio_compra_actual * cantidad
    if usuario.saldo >= total_precio:
        transaccion_dao.create(usuario.usuario_id, accion.accion_id, 'compra', cantidad, accion.precio_compra_actual, comision)       
        usuario.saldo -= total_precio
        portafolio_id = portafolio_dao.get_portafolio_id(usuario.usuario_id, simbolo)     
        if portafolio_id:
            portafolio_dao.update(usuario.usuario_id, portafolio_id, simbolo, cantidad)
            print("Portafolio actualizado con éxito.")
        else:
            portafolio_dao.create(usuario.usuario_id, simbolo, cantidad)
            print("Portafolio creado con éxito.")
        print(f"Compra realizada con éxito. Se han comprado {cantidad} acciones de {simbolo}.")
    else:
        print("Fondos insuficientes para completar la compra.")

def vender_accion(usuario, portafolio_dao, accion_dao, transaccion_dao):
    simbolo = input("Ingrese el símbolo de la acción que desea vender: ")
    cantidad = int(input("Ingrese la cantidad de acciones a vender: "))
    comision = 1.5  
    activo = portafolio_dao.read_by_simbolo(usuario.usuario_id, simbolo)
    if activo and activo.cantidad >= cantidad:
        accion = accion_dao.read_by_simbolo(simbolo)    
        transaccion_dao.create(usuario.usuario_id, accion.accion_id, 'venta', cantidad, accion.precio_venta_actual, comision)      
        usuario.saldo += accion.precio_venta_actual * cantidad
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