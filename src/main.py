"""Programa principal del Sistema de Inventario."""

from producto import Producto
from busqueda import buscar_producto


def main():
    print("=== Sistema de Inventario ===")
    inventario = [
        Producto("P001", "Teclado", 350, 10),
        Producto("P002", "Mouse", 180, 5),
        Producto("P003", "Monitor", 2800, 3),
    ]

    print(f"\nProductos registrados: {len(inventario)}\n")
    for producto in inventario:
        producto.mostrar_informacion()
        print("-" * 25)

    resultado = buscar_producto(inventario, "mouse")
    print(f"Busqueda 'mouse': {len(resultado)} producto(s) encontrado(s)")
    print(f"Valor total del inventario: {calcular_valor_total(inventario)}")
    print("Sistema ejecutado correctamente.")


if __name__ == "__main__":
    main()
