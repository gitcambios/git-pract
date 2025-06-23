from tienda.producto import Producto

class ItemCarrito:
    def __init__(self, producto, cantidad):
        if cantidad <= 0 :
            raise ValueError("La cantidad debe ser mayor a 0")
        self.producto = producto
        self.cantidad = cantidad

    def mostrarItem(self):
        return (
            f"Producto: {self.producto}\n"
            f"Cantidad: {self.cantidad}\n"
        )
    
    def subTotal(self):
        return self.producto.precio * self.cantidad
         
    def __str__(self):
        return self.mostrarItem()
