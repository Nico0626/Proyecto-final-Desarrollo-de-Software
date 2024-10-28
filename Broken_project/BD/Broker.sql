
CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    contraseña VARCHAR(100) NOT NULL,
    gmail VARCHAR(100) NOT NULL,
    tipo ENUM('individual', 'empresa', 'institucion') NOT NULL,
    saldo DECIMAL(15,2) DEFAULT 1000000.00,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE Portafolio (
    id_portafolio INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT UNIQUE,
    total_invertido DECIMAL(15,2),
    saldo_cuenta DECIMAL(15,2),
    cantidad INT,
    valor DECIMAL(15,2),
    ganancia DECIMAL(15,2),
    simbolo VARCHAR(20),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);


CREATE TABLE Empresas (
    id_empresa INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    cuit VARCHAR(25) NOT NULL UNIQUE,
    sector VARCHAR(100) NOT NULL,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE Broker (
    broker_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_broker VARCHAR(100) NOT NULL,
    cuit VARCHAR(20) UNIQUE NOT NULL,
    comision DECIMAL(5,2) NOT NULL
);


CREATE TABLE Acciones (
    accion_id INT AUTO_INCREMENT PRIMARY KEY,
    simbolo VARCHAR(10) NOT NULL,
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
    FOREIGN KEY (empresa_id) REFERENCES Empresas(id_empresa)
);


CREATE TABLE Transacciones (
    transaccion_id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    accion_id INT,
    broker_id INT,
    tipo ENUM('compra', 'venta') NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(15,2) NOT NULL,
    comision DECIMAL(15,2) NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (accion_id) REFERENCES Acciones(accion_id),
    FOREIGN KEY (broker_id) REFERENCES Broker(broker_id)
);


CREATE TABLE PerfilInversor (
    perfil_id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT UNIQUE,
    tolerancia_riesgo ENUM('conservador', 'medio', 'agresivo') NOT NULL,
    duracion_inversion ENUM('corta', 'media', 'larga') NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);


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
    FOREIGN KEY (accion_id) REFERENCES Acciones(accion_id)
);


