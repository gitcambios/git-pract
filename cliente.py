
from usuario import Usuario
from direccion import Direccion

class Cliente(Usuario):
    def __init__(self, nombre, apellido, email, contraseña, telefono, direccion):
        super().__init__(nombre, apellido, email, contraseña)
        self.telefono = telefono
        self.direccion  = direccion
        self.historial_pedido =[]
        self.carrito = []
      
    