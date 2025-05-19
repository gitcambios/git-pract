
class ItemPedido:
    def __init__(self, producto, cantidad, precio_unitario):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def calcular_subtoral(self):
        return self.cantidad * self.precio_unitario
    