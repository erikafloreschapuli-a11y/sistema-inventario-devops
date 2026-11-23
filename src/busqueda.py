"""Funciones de busqueda de productos del Sistema de Inventario."""


def buscar_producto(productos, texto):
    """Devuelve los productos cuyo codigo o nombre contienen el texto buscado."""
    texto = texto.lower()
    return [
        producto
        for producto in productos
        if texto in producto.codigo.lower() or texto in producto.nombre.lower()
    ]
