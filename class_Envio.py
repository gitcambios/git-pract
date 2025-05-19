
from datetime import datetime

class Envio:
    def __init__(self, direccion):
        self.direccion = direccion
        self.fecha_envio = datetime.now()
        self.estado = "pendiente"
    
    def registrar_pedido(self):
        self.estado = "en camino"

    def marcar_como_entregado(self):
        self.estado = "Entregado"

    def cancelar_envio(self):
        self.estado = "Cancelado"

    def mostrar_detalles(self):
        return f"Envio a {self.direccion.calle} {self.direccion.numero} - Estado: {self.estado}"
    