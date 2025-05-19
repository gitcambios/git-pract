

class Cupon:
    def __init__(self, codigo, porcentaje, cantidad_maxima_usos):
        self.codigo = codigo
        self.porcentaje = porcentaje
        self.es_valido =True
        self.cantidad_maxima_usos = cantidad_maxima_usos
        self.cantidad_usos = 0
        