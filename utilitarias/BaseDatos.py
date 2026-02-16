# Este modulo contendra lo relacionado a la Conexion BD - MySQL
# Importar el controlador (drive) de MySQL, Error y Producto
import mysql.connector
from mysql.connector import Error
from .Producto import Producto

# Crear la funcion conectar () para conectarme a MySQL
def conectar():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin123",
            database="Ejercicio_BD",
            port= 3306
        )
        print("[MySQL] Conectado")
    except Error as e:
        print(f"[ERROR] Conexion FAllida a MySQL: {e}")
    return con

# Crear la Funcion para listar Productos
def listar_produtos():
    con = conectar()
    lista_produtos = []
    try:
        sql = "SELECT * FROM Producto;"
        cursor = con.cursor() #permite obtener un objeto que puede ejecutar sentencias SQL
        resultado = cursor.fetchall()

        # Recorremos el resultado que contiene todos los registros (filas) de la BD
        for registro in resultado:
            producto = Producto(
                id = registro['ProductoID'],
                nombre = registro['nombre'],
                descripcion = registro['descripcion'],


            )

    except Error as e:
        print(f"[ERROR] Conexion Fallida contenido tabla de productor: {e}")


def registrar_produto(producto):
    con = conectar()
    try:
        # Esto en Python se llama consulta SQL Parametrizadas, para evitar inyecciones SQL
        #Se crea la consulta SQL priemro y despues pasa a los valores.
        sql = f"INSERT INTO Producto (Nombre, Categoria, Marca, Precio, Stock, Descuento, Peso, FechaIngreso)"
        f"VALUES(%s, %s, %s, %s, %s, %s, %s, %s);")
        valores = (
            producto.get_nombre(),
            producto.get_categoria(),
            producto.get_marca(),
            producto.get_precio(),
            producto.get_stock(),
            producto.get_descuento(),
            producto.get_peso(),
            producto.get_fecha_ingreso()
        )
        cursor = con.cursor()
        # Aca pasan 2 cosas. 1) Al ejecutar el metodo execute() esto gatilla en MySQL el comando START TRANSACTION;
        #2) El string 'sql' (valores parametrizados) es rellenado con valores (tupla 'valores') en el metodo execute()
        cursor.execute(sql, valores)

        #aplicamos el COMIT (principios ACID)
        con.commit()
        print("[MySQL] Producto registrado exitosamente")
    except Error as e:
        con.rollback()
        print(f"[ERROR] No se pudo registrar producto: {e}")
    finally:
        if (con.is_conected()):
            cursor.close()
            con.close()
