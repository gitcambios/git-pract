class Cupon:
    def __init__(self, codigo, porcentaje, cantMaxUso):
        self.codigo = codigo
        self.porcentaje = porcentaje
        self.es_valido = True
        self.cantMaxUso = cantMaxUso
        self.cantUsos = 0
        
    def esValido(self):
        if self.cantMaxUso >= self.cantUsos and self.es_valido == True:
            return True
        else:
            return False
    
    def aplicarDescuento(self, montoTotal):
        if self.esValido():
            return montoTotal * (1 - self.porcentaje)
        else:
            return montoTotal

    def registrarUso(self):
        if self.esValido():
            self.cantUsos += 1
            if self.cantUsos >= self.cantMaxUso:
                self.es_valido = False
