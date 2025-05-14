

from datetime import date


class Pedido:
    def __ini__(self, id_pedido, cliente, envio):
        self.id_pedido = id_pedido
        self.fecha = date.today()
        self.monto_total = 00
        self.cliente = cliente
        self.pago = None
        self.envio = envio
        self.lista_items = []
        self.cupon = None


            
            
