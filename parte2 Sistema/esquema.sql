-- Tabla Usuario
CREATE TABLE Usuario (
    id_usuario INT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

-- Tabla Producto
CREATE TABLE Producto (
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10, 2)
);

-- Tabla Carrito
CREATE TABLE Carrito (
    id_carrito INT PRIMARY KEY,
    id_usuario INT,
    total DECIMAL(10, 2),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

-- Tabla Orden
CREATE TABLE Orden (
    id_orden INT PRIMARY KEY,
    id_carrito INT,
    fecha DATE,
    total DECIMAL(10, 2),
    estado VARCHAR(50),
    FOREIGN KEY (id_carrito) REFERENCES Carrito(id_carrito)
);

-- Tabla Pago
CREATE TABLE Pago (
    id_orden INT PRIMARY KEY,
    fecha DATE,
    total DECIMAL(10, 2),
    estado VARCHAR(50),
    FOREIGN KEY (id_orden) REFERENCES Orden(id_orden)
);


CREATE TABLE Carrito_Producto (
    id_carrito INT,
    id_producto INT,
    cantidad INT,
    PRIMARY KEY (id_carrito, id_producto),
    FOREIGN KEY (id_carrito) REFERENCES Carrito(id_carrito),
    FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);
