"""Modulo Producto del Sistema de Inventario."""


class Producto:
    """Representa un producto dentro del inventario."""

    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar_informacion(self):
        """Devuelve y muestra en pantalla la informacion del producto."""
        informacion = (
            f"Codigo: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Precio: {self.precio}\n"
            f"Existencia: {self.existencia}"
        )
        print(informacion)
        return informacion


if __name__ == "__main__":
    producto = Producto("P001", "Teclado", 350, 10)
    producto.mostrar_informacion()
    print("Producto disponible")
