CREATE DATABASE Broker; 
use Broker;
create table Usuario
(
id_usuario int primary key auto_increment,
nombre varchar (50) not null,
Apellido varchar (50) not null,
saldo DECIMAL(15,2) DEFAULT 1000000.00
);
create table Portafolio
(
id_portafolio int primary key auto_increment, 
id_usuario INT UNIQUE,
total_invertido DECIMAL(15,2),
saldo_cuenta DECIMAL(15,2),
cantidad int, 
valor DECIMAL(15,2), 
ganancia DECIMAL(15,2),
simbolo varchar(20), 
FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);
create table Broker
(
id_broker INT AUTO_INCREMENT PRIMARY KEY, 
nombre_broker varchar (50) not null,
cuit VARCHAR(20) UNIQUE NOT NULL,
comision DECIMAL(5,2) NOT NULL
);
create table Empresas
(
id_empresa INT AUTO_INCREMENT PRIMARY KEY,
nombre varchar (100) not null,
cuit VARCHAR(25) NOT NULL,
sector varchar(100) not null
);
create table acciones
(
id_accion INT AUTO_INCREMENT PRIMARY KEY, 
id_empresa INT not null,
simbolo VARCHAR(10) NOT NULL,
ultimo_operado DECIMAL(15,2), 
cantidad_compra int, 
precio_compra DECIMAL(15,2),
precio_venta DECIMAL(15,2),
cantidad_venta int, 
apertura DECIMAL(15,2), 
minimo DECIMAL(15,2),
maximo DECIMAL(15,2),
cierre DECIMAL(15,2),
FOREIGN KEY (id_empresa) REFERENCES Empresas(id_empresa)
);
create table cotizacion
(
id_cotizacion INT AUTO_INCREMENT PRIMARY KEY,
id_accion int,
precio_venta DECIMAL(15,2),
precio_compra DECIMAL(15,2), 
cantidad_venta int, 
cantidad_compra int, 
minimo_diario DECIMAL(15,2),
maximo_diario DECIMAL(15,2),
FOREIGN KEY (id_accion) REFERENCES acciones(id_accion)
);
create table Transacciones
(
id_transaccion INT AUTO_INCREMENT PRIMARY KEY,
id_usuario int not null,
id_broker int not null,
id_accion int not null, 
tipo ENUM('compra', 'venta') NOT NULL,
cantidad int not null, 
precio DECIMAL(15,2) NOT NULL, 
comision DECIMAL(15,2) NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
FOREIGN KEY (id_broker) REFERENCES Broker(id_broker),
FOREIGN KEY (id_accion) REFERENCES acciones(id_accion)
);
CREATE TABLE PerfilInversor (
    id_perfil INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT UNIQUE,
    tolerancia_riesgo ENUM('conservador', 'medio', 'agresivo') NOT NULL,
    duracion_inversion ENUM('corta', 'media', 'larga') NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);
CREATE TABLE Inversor (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100), 
correo VARCHAR(50) unique NOT NULL, 
contraseña varchar(50), 
intentos_fallidos INT DEFAULT 0, 
bloqueado BOOLEAN DEFAULT FALSE
);

INSERT INTO Usuario (nombre, apellido) VALUES
("Lionel", "Messi"),
("Angel", "Dimaria"),
("Julian", "Alvarez"), 
("Emiliano", "Martinez"), 
("Roman", "Riquelme"), 
("Lionel", "scaloni"), 
("Angel", "Correa"), 
("Sergio", "Romero"), 
("Lisandro", "Martinez"), 
("Enzo", "Fernandez")
;
INSERT INTO Portafolio (id_usuario, total_invertido, saldo_cuenta, cantidad, valor, ganancia, simbolo) VALUES 
(1, 1000000, 1100000, 5, 1700, 1800, "AAPL"),
(2, 1100000, 900000, 8, 9500, 1200, "BMA"),
(3, 1035000, 1200000, 3, 8500, 97000, "ALUA"), 
(4, 2000000, 500000, 9, 30000, 120000, "YPF"), 
(5, 1800000, 700000, 7, 85000, 50000, "GGAL"),
(6, 1500000, 250000, 12, 50000, 23000, "YPF"),
(7, 1750000, 660000, 15, 85000, 22000, "PAMP"),
(8, 1000000, 130000, 6, 65000, 77000, "TECO"),
(9, 25000000, 700000, 18, 42000, 51000, "PAMP"),
(10, 1230000, 323000, 9, 66000, 130000, "GGAL"); 
INSERT INTO Broker (nombre_broker, cuit, comision) VALUES
("ARG Broker",9762345,1.5 );
INSERT INTO Empresas (nombre, cuit, sector) VALUES
("Apple", 2365458, "tecnologico"),
("Banco Macro", 3367855, "Bancario"),
("Aluar", 44565234, "Industrial"),
("Yacimientos Petrolíferos", 2365458, "Minero"),
("Banco Galicia", 8765458, "Bancario"),
("Yacimientos Petroliferos", 2365458, "Minero"),
("Pampa Energia", 9965458, "Energetico"),
("Telecom", 5275458, "Comunicaciones"),
("Pampa Energia", 9965458, "Energetico"),
("Banco Galicia", 8765458, "Bancario");
Insert INTO Acciones (id_empresa, simbolo, ultimo_operado, cantidad_compra, 
precio_compra, precio_venta, cantidad_venta, apertura, minimo, maximo, cierre)VALUES
(1, "AAPL", 12000, 5, 11000, 10200, 2, 11001, 10421, 11899,12000),
(2, "BMA", 3200, 9, 5800, 6400, 3, 4900, 5011, 6000, 6500), 
(3, "ALUA", 4100, 7, 1000, 1200, 7, 6500, 7800, 8000, 9000),
(4, "YPF", 8100, 8, 1200, 1250, 5, 6500, 7800, 8000, 1000),
(5, "GGAL", 9100, 13, 21000, 22000, 6, 6500, 7800, 8000, 20000),
(6, "YPF", 5600, 4, 18000, 1900, 2, 6500, 7800, 8000, 30000),
(7, "PAMP", 3200, 9, 33000, 3200, 7, 6500, 7800, 8000, 45000),
(8, "TECO", 5600, 5, 56000, 57000, 4, 6500, 7800, 8000, 7000),
(9, "PAMP", 8900, 12, 45000, 44000, 9, 6500, 7800, 8000, 8500),
(10, "GGAL", 5800, 4, 23000, 22000, 2, 6500, 7800, 8000, 9670);

INSERT INTO Cotizacion (id_accion, precio_venta, precio_compra, cantidad_venta,
cantidad_compra, minimo_diario, maximo_diario) VALUES
(1, 12700, 12900, 2, 5, 12120, 12999),
(2, 5600, 5500, 5, 8, 5676, 5480), 
(3, 1200, 1240, 3, 3, 3452, 3312),
(4, 1800, 1740, 7, 4, 4452, 5612),
(5, 3400, 3540, 6, 4, 2452, 4312),
(6, 5600, 5870, 8, 9, 5652, 7812),
(7, 7890, 8000, 3, 5, 9952, 10912),
(8, 5500, 6040, 6, 8, 4563, 6778),
(9, 7600, 8140, 2, 9, 10600, 11200),
(10, 3400, 5040, 1, 3, 4567, 5660);
INSERT INTO Transacciones (id_usuario, id_broker, id_accion, tipo, cantidad, precio, comision)VALUES
(1, 1, 1, "compra", 5, 1200, 1.5),
(2, 1, 2, "compra",7, 1500, 1.5), 
(3, 1, 3, "venta",5, 2300,1.5),
(4, 1, 4, "compra",4, 56000, 1.5),
(5, 1, 5,"venta",3, 8700, 1.5),
(6, 1, 6, "compra",8, 7800, 1.5),
(7, 1, 7, "venta", 7, 4500, 1.5),
(8, 1, 8, "compra", 5, 12000, 1.5),
(9, 1, 9, "compra", 2, 5890, 1.5),
(10, 1, 10,"venta", 9, 15000, 1.5);

UPDATE Usuario SET Nombre= "Lionel Andres", apellido= "Messi Cuccittini" WHERE id_usuario=1;
UPDATE broker SET comision= 2.5 WHERE id_broker= 1;
UPDATE portafolio SET simbolo= "YPF" WHERE id_portafolio=1;
UPDATE acciones SET simbolo= "YPF" WHERE id_accion=1;
UPDATE empresas SET nombre= "Yacimientos Petrolíferos", sector="minero" WHERE id_empresa=1;

SELECT * FROM Usuario WHERE id_usuario > 5;
SELECT simbolo, id_empresa FROM acciones;
SELECT * FROM portafolio Where total_invertido > 1450000;
SELECT * FROM acciones where cantidad_compra < 9;
SELECT minimo_diario, maximo_diario, id_accion FROM cotizacion;

SELECT * FROM usuario
INNER JOIN transacciones ON usuario.id_usuario = transacciones.id_usuario;

SELECT * FROM acciones
LEFT JOIN empresas ON acciones.id_empresa = empresas.id_empresa;

SELECT * FROM acciones
RIGHT JOIN cotizacion ON acciones.id_accion = cotizacion.id_accion;

SELECT transacciones.tipo, usuario.nombre FROM transacciones, usuario 
WHERE transacciones.id_usuario= usuario.id_usuario
