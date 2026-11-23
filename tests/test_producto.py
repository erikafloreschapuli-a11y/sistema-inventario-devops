"""Pruebas de la funcionalidad Producto (fase TEST)."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from producto import Producto  # noqa: E402


class TestProducto(unittest.TestCase):

    def setUp(self):
        self.producto = Producto("P001", "Teclado", 350, 10)

    def test_cp01_crear_producto(self):
        self.assertIsInstance(self.producto, Producto)

    def test_cp02_codigo(self):
        self.assertEqual(self.producto.codigo, "P001")

    def test_cp03_nombre(self):
        self.assertEqual(self.producto.nombre, "Teclado")

    def test_cp04_precio(self):
        self.assertEqual(self.producto.precio, 350)

    def test_cp05_existencia(self):
        self.assertEqual(self.producto.existencia, 10)

    def test_cp06_mostrar_informacion_completa(self):
        informacion = self.producto.mostrar_informacion()
        self.assertIn("P001", informacion)
        self.assertIn("Teclado", informacion)
        self.assertIn("350", informacion)
        self.assertIn("10", informacion)

    def test_cp07_segundo_producto(self):
        mouse = Producto("P002", "Mouse", 180, 5)
        self.assertEqual(mouse.codigo, "P002")
        self.assertEqual(mouse.nombre, "Mouse")
        self.assertEqual(mouse.precio, 180)
        self.assertEqual(mouse.existencia, 5)
        self.assertEqual(self.producto.nombre, "Teclado")


if __name__ == "__main__":
    unittest.main(verbosity=2)
