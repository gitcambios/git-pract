
class ItemPedido:
    def __init__(self, producto, cantidad, precio_unitario):
        if cantidad <= 0:
            raise ValueError ("Ingrese una cantidad mayor a 0")

        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def calcularSubtotal(self):
        return self.cantidad * self.precio_unitario
    
    def __str__(self):
        return (
            f"{self.producto}\n"
            f"Cantidad: {self.cantidad}\n"
            f"SubTotal: {self.calcularSubtotal()}\n"
        )
    