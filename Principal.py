# Modulo para ejecutar la App
import sys
from utilitarias.Producto import Producto
from utilitarias.BaseDatos import listar_produtos, registrar_produto, actualizar_produto, eliminar_producto

# Implementar las funciones necesarias para la interfaz del usuario
def listar_productos_menu():
    print(f"---- Lsitado de Productos ----")
    productos = listar_produtos()
    if not productos:
        print("[CRUD] No hay productos para listar")
    else:
        for p in productos:
            print(p)

def registrar_producto_bd():
    print(f"---- registro producto ----")
    try:
        n = input("Ingrese el nombre del producto: ")
        c = input("Ingrese la categoria de producto: ")
        m = input("Ingrese la marca del producto: ")
        p = Producto(n,c,m)
        s
        d
        pe =
        fi =
        nuevo_producto = Producto(n,)
    except ValueError:
        print("[ERROR] Los tipos de valores ingresador no corresponden al tipo de valor en la bd MySQL.")