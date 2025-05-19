class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, stock, categoria ):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def actualizarStock(self, cantidad):
        self.stock -= cantidad
    def mostrarDetalles(self):
        return f"{self.nombre} - {self.descripcion} - {self.precio}"
    