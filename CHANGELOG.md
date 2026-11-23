# Historial de versiones

## v1.0.0
- Primera versión del Sistema de Inventario.
- Incorporación de la funcionalidad Producto (código, nombre, precio y existencia).
- Función de búsqueda de productos.
- Implementación de pruebas automatizadas (CP01 a CP07).
- Workflows de build, pruebas y liberación en GitHub Actions.

## v1.0.1 (no publicada)
- Se intentó liberar con un error en el precio mostrado.
- Las pruebas fallaron (CP06) y el workflow detuvo la publicación.

## v1.0.2
- Corrección del error detectado durante las pruebas.
- Validación satisfactoria de la funcionalidad Producto.

## v1.1.0
- Se agregó el cálculo del valor total del inventario.
- Al desplegarla, el programa falló (NameError) y el workflow de despliegue recuperó automáticamente la v1.0.2.
- El cambio defectuoso se revirtió en la rama main.
