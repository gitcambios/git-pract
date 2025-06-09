
class Direccion:
    def __init__(self, calle, numero, ciudad, codigo_postal, provincia):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.provincia  = provincia

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.ciudad}, CP {self.codigo_postal}, {self.provincia}"