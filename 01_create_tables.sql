CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    stock INT NOT NULL
);

CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    departamento_id INT NOT NULL
);

CREATE TABLE departamentos (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL
);

