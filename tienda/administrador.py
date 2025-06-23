
from tienda.usuario import Usuario
from tienda.usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombre, apellido, email, contraseña):
        super().__init__(nombre, apellido, email, contraseña)

    def agregarProducto(self, producto, lista_productos):
        lista_productos.append(producto)
        return f"Producto '{producto.nombre}' agregado correctamente."

    def eliminarProducto(self, producto, lista_productos):
        if producto in lista_productos:
            lista_productos.remove(producto)
            return f"Producto '{producto.nombre}' eliminado correctamente."
        else:
            return "Producto no encontrado."

    def modificarPrecioProducto(self, producto, nuevo_precio):
        producto.precio = nuevo_precio
        return f"Precio de '{producto.nombre}' actualizado a ${nuevo_precio}."

    def modificarStockProducto(self, producto, nuevo_stock):
        producto.stock = nuevo_stock
        return f"Stock de '{producto.nombre}' actualizado a {nuevo_stock} unidades."



