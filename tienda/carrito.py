from tienda.itemCarrito import ItemCarrito
from tienda.producto import Producto

class Carrito:
    def __init__(self, id_carrito, cliente):
        self.id_carrito = id_carrito
        self.cliente = cliente
        self.items = []

    def agregarItem(self, item):
        self.items.append(item)
    
    def eliminarItem(self, itemEliminar):
        for i in self.items:
            if i.producto.id_producto == itemEliminar:
                self.items.remove(i)
                break
            
    def vaciarCarrito(self):
        self.items.clear()

    def verResumen(self):
        resumen = ""
        total = 0

        for i in self.items:
            resumen += str(i) + f"Subtotal: ${i.subTotal()}\n\n"
            total += i.subTotal()

        resumen += f"Total: ${total}"
        return resumen

    