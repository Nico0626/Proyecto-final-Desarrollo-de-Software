-- Crear la base de datos
CREATE DATABASE ARGBroker;
USE ARGBroker;

-- Tabla Usuarios
CREATE TABLE Usuarios (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    tipo ENUM('individual', 'empresa', 'institucion') NOT NULL,
    saldo DECIMAL(15,2) DEFAULT 1000000.00,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla Empresas
CREATE TABLE Empresas (
    empresa_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_empresa VARCHAR(100) NOT NULL,
    cuit VARCHAR(20) UNIQUE NOT NULL,
    sector VARCHAR(100),
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla Broker
CREATE TABLE Broker (
    broker_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_broker VARCHAR(100) NOT NULL,
    cuit VARCHAR(20) UNIQUE NOT NULL,
    comision DECIMAL(5,2) NOT NULL,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla Acciones
CREATE TABLE Acciones (
    accion_id INT AUTO_INCREMENT PRIMARY KEY,
    simbolo VARCHAR(10) UNIQUE NOT NULL,
    empresa_id INT,
    ultimo_operado DECIMAL(15,2),
    cantidad_compra_diaria INT,
    precio_compra_actual DECIMAL(15,2),
    precio_venta_actual DECIMAL(15,2),
    cantidad_venta_diaria INT,
    apertura DECIMAL(15,2),
    minimo_diario DECIMAL(15,2),
    maximo_diario DECIMAL(15,2),
    ultimo_cierre DECIMAL(15,2),
    fecha_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (empresa_id) REFERENCES Empresas(empresa_id)
);

-- Tabla Transacciones
CREATE TABLE Transacciones (
    transaccion_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    accion_id INT,
    broker_id INT,
    tipo ENUM('compra', 'venta') NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(15,2) NOT NULL,
    comision DECIMAL(15,2) NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id),
    FOREIGN KEY (accion_id) REFERENCES Acciones(accion_id),
    FOREIGN KEY (broker_id) REFERENCES Broker(broker_id)
);

-- Tabla Portafolio
CREATE TABLE Portafolio (
    portafolio_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT UNIQUE,
    fecha_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id)
);

-- Tabla Perfil Inversor
CREATE TABLE PerfilInversor (
    perfil_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT UNIQUE,
    tolerancia_riesgo ENUM('conservador', 'medio', 'agresivo') NOT NULL,
    duracion_inversion ENUM('corta', 'media', 'larga') NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id)
);

-- Tabla Cotizaciones
CREATE TABLE Cotizaciones (
    cotizacion_id INT AUTO_INCREMENT PRIMARY KEY,
    accion_id INT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    precio_compra DECIMAL(15,2),
    precio_venta DECIMAL(15,2),
    cantidad_compra INT,
    cantidad_venta INT,
    minimo_diario DECIMAL(15,2),
    maximo_diario DECIMAL(15,2),
    FOREIGN KEY (accion_id) REFERENCES Acciones(accion_id));
    