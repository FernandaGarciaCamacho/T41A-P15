CREATE OR REPLACE FUNCTION calcular_descuento(precio_original NUMERIC, porcentaje_descuento NUMERIC)
RETURNS NUMERIC AS $$
BEGIN
    RETURN precio_original - (precio_original * porcentaje_descuento);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION validar_correo(correo TEXT)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN POSITION('@' IN correo) > 0;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION productos_bajo_stock(cantidad_minima INT)
RETURNS TABLE(id INT, nombre TEXT, stock INT) AS $$
BEGIN
    RETURN QUERY
    SELECT id, nombre, stock
    FROM productos
    WHERE stock < cantidad_minima;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION obtener_dia_semana(fecha DATE)
RETURNS TEXT AS $$
BEGIN
    RETURN TO_CHAR(fecha, 'Day');
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION contar_empleados_departamento(dep_id INT)
RETURNS INT AS $$
BEGIN
    RETURN (SELECT COUNT(*) FROM empleados WHERE departamento_id = dep_id);
END;
$$ LANGUAGE plpgsql;


