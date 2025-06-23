from tienda.class_Carrito import Carrito
from tienda.class_ItemCarrito import ItemCarrito
from tienda.usuario import Usuario
from tienda.direccion import Direccion

class Cliente(Usuario):
    def __init__(self, nombre, apellido, email, contraseña, telefono, direccion, carrito):
        super().__init__(nombre, apellido, email, contraseña)
        self.telefono = telefono
        self.direccion  = direccion
        self.historialPedido = []
        self.carrito = carrito

    def verHistoriaPedidos(self):
        contPedido = 0
        if not self.historialPedido:
            return "No hay pedidos registrados"

        for p in self.historiaPedido:
            contPedido = contPedido + 1
            historial += f"Pedido #{p.id_pedido} - Fecha: {p.fecha.strftime('%d/%m/%Y')} - Total: ${p.monto_total:.2f}\n"
        return historial
    
    def agregarAlCarrito(self, producto, cantidad):

        if producto.stock < cantidad:
            return "No hay stock suficiente"
        
        item = ItemCarrito(self, producto, cantidad)

        self.carrito.agregarItem(item)
        return f"Producto {producto.nombre} se ha agregado al carrito (x{cantidad}) "
