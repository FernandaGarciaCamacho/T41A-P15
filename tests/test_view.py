import psycopg2
import pytest
from pathlib import Path
from decimal import Decimal

DB_CONFIG = {
    "dbname": "test_db",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": 5432
}

@pytest.fixture(scope="module")
def db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    yield conn
    conn.close()

def test_calcular_descuento(db_connection):
    with db_connection.cursor() as cur:
        precio_original = Decimal('1000.00')
        descuento = Decimal('0.10')

        cur.execute("SELECT calcular_descuento(%s, %s);", (precio_original, descuento))
        precio_final = cur.fetchone()[0]
        assert round(precio_final, 2) == round(precio_original * (1 - descuento), 2)

def test_validar_correo(db_connection):
    with db_connection.cursor() as cur:
        cur.execute("SELECT validar_correo(%s);", ('juan.perez@ejemplo.com',))
        resultado = cur.fetchone()[0]
        assert resultado is True

        cur.execute("SELECT validar_correo(%s);", ('juan.perezejemplo.com',))
        resultado = cur.fetchone()[0]
        assert resultado is False

def test_productos_bajo_stock(db_connection):
    with db_connection.cursor() as cur:
        cur.execute("SELECT * FROM productos_bajo_stock(%s);", (10,))
        productos = cur.fetchall()

        for producto in productos:
            assert producto[2] < 10 

def test_obtener_dia_semana(db_connection):
    with db_connection.cursor() as cur:
        cur.execute("SELECT obtener_dia_semana(%s);", ('2025-11-10',))
        dia_semana = cur.fetchone()[0]

        assert dia_semana.strip() == 'Monday'

def test_contar_empleados_departamento(db_connection):
    with db_connection.cursor() as cur:
        cur.execute("SELECT contar_empleados_departamento(%s);", (1,))
        empleados_count = cur.fetchone()[0]
        assert empleados_count == 2 

        cur.execute("SELECT contar_empleados_departamento(%s);", (2,))
        empleados_count = cur.fetchone()[0]
        assert empleados_count == 2
