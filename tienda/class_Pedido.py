from tienda.class_itemPedido import ItemPedido
from tienda.cliente import Cliente
from tienda.class_Cupon import Cupon
from datetime import date


class Pedido:
    def __init__(self, id_pedido, cliente, metodoPago, envio,cupon):
        self.id_pedido = id_pedido
        self.fecha = date.today()
        self.cliente = cliente
        self.monto_total = 00
        self.metodoPago = metodoPago
        self.envio = envio
        self.items = []
        self.cupon = cupon
    
    def agregarItem(self, item):
        self.items.append(item)

    def calcularTotal(self):
        montoTotal = 0
        for i in self.items:
            subTotal = i.calcularSubtotal()
            montoTotal += subTotal
        self.monto_total = montoTotal
        return montoTotal
    
    def aplicarDescuento(self):
        total = self.calcularTotal()
        
        if self.cupon is not None:
            totalConDescuento = self.cupon.aplicarDescuento(total)
            if total != totalConDescuento:
                self.cupon.registrarUso()
            else:
                return "El cupon no fue aplicado"
            
            self.monto_total = totalConDescuento
        else:
            self.monto_total = total
        
        return self.monto_total

    def realizarPago(self):
        return f"Pedido pagado por {self.cliente.nombre} {self.cliente.apellido} con {self.metodoPago}"
    
    def registrarCompra(self):
        for i in self.items:
            if i.producto.stock >= i.cantidad:
                i.producto.eliminarStock(i.cantidad)
            else:
                return "Stock insuficiente!"

        self.fecha = date.today()

        totalFinal = self.aplicarDescuento()

        self.cliente.historialPedido.append(self)

        return f"Compra registrada el {self.fecha.strftime('%d/%m/%Y')}. Total: ${totalFinal:.2f}"
    
        
    
       
        


    