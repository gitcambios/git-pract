
from datetime import datetime

class Envio:
    def __init__(self, direccion):
        self.direccion = direccion
        self.fecha_envio = datetime.now()
        self.estado = "pendiente"
    
    def registrar_pedido(self):
        self.estado = "En camino"

    def marcar_como_entregado(self):
        self.estado = "Entregado"

    def cancelar_envio(self):
        if self.estado not in ["Entregado", "En camino"]:
            self.estado = "Cancelado"

    def mostrar_detalles(self):
        return f"Envio a {self.direccion.calle} {self.direccion.numero} - Estado: {self.estado}"
    