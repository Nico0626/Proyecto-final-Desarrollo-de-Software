
INSERT INTO Usuario (nombre, apellido, contraseña, gmail, tipo) VALUES
("Lionel", "Messi", "password123", "lmessi@gmail.com", "individual"),
("Angel", "Dimaria", "password123", "adimaria@gmail.com", "individual"),
("Julian", "Alvarez", "password123", "jalvarez@gmail.com", "individual"),
("Emiliano", "Martinez", "password123", "emartinez@gmail.com", "individual"),
("Roman", "Riquelme", "password123", "rriquelme@gmail.com", "individual"),
("Lionel", "Scaloni", "password123", "lscaloni@gmail.com", "individual"),
("Angel", "Correa", "password123", "acorrea@gmail.com", "individual"),
("Sergio", "Romero", "password123", "sromero@gmail.com", "individual"),
("Lisandro", "Martinez", "password123", "lmartinez@gmail.com", "individual"),
("Enzo", "Fernandez", "password123", "efernandez@gmail.com", "individual");

INSERT INTO Empresas (nombre, cuit, sector) VALUES
("Apple", '2365458A', "tecnologico"),
("Banco Macro", '3367855B', "bancario"),
("Aluar", '44565234C', "industrial"),
("Yacimientos Petrolíferos", '8765458D', "minero"),
("Banco Galicia", '8765458E', "bancario"),
("Pampa Energia", '9965458F', "energetico"),
("Telecom", '5275458G', "comunicaciones");

INSERT INTO Acciones (empresa_id, simbolo, ultimo_operado, cantidad_compra_diaria, precio_compra_actual, precio_venta_actual, cantidad_venta_diaria, apertura, minimo_diario, maximo_diario, ultimo_cierre) VALUES
(1, "AAPL", 12000, 5, 11000, 10200, 2, 11001, 10421, 11899, 12000),
(2, "BMA", 3200, 9, 5800, 6400, 3, 4900, 5011, 6000, 6500),
(3, "ALUA", 4100, 7, 1000, 1200, 7, 6500, 7800, 8000, 9000),
(4, "YPF", 8100, 8, 1200, 1250, 5, 6500, 7800, 8000, 1000),
(5, "GGAL", 9100, 13, 21000, 22000, 6, 6500, 7800, 8000, 20000);


UPDATE Usuario SET nombre = "Lionel Andres", apellido = "Messi Cuccittini" WHERE id_usuario = 1;
UPDATE Broker SET comision = 2.5 WHERE broker_id = 1;
UPDATE Portafolio SET simbolo = "YPF" WHERE id_portafolio = 1;
UPDATE Acciones SET simbolo = "YPF" WHERE accion_id = 1;
UPDATE Empresas SET nombre = "Yacimientos Petrolíferos", sector = "minero" WHERE id_empresa = 1;

SELECT * FROM Usuario WHERE id_usuario > 5;
SELECT * FROM Acciones;
SELECT * FROM Portafolio WHERE total_invertido > 1450000;
SELECT * FROM Acciones WHERE cantidad_compra_diaria < 9;
SELECT * FROM Cotizaciones;

SELECT * 
FROM Usuario 
INNER JOIN Transacciones ON Usuario.id_usuario = Transacciones.id_usuario;

SELECT * 
FROM Acciones 
LEFT JOIN Empresas ON Acciones.empresa_id = Empresas.id_empresa;

SELECT * 
FROM Acciones 
RIGHT JOIN Cotizaciones ON Acciones.accion_id = Cotizaciones.accion_id;

SELECT Transacciones.tipo, Usuario.nombre,