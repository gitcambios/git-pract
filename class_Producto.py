class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, stock, categoria, talles, colores ):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
        self.talles = talles if talles else[]
        self.colores = colores if colores else[]

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    def mostrarDetalles(self):
        return(
            f"Nombre: {self.nombre}\n"
            f"Descripcion: {self.descripcion}\n"
            f"Precio: {self.precio}\n"
            f"Talles Disponibles: {', '.join(self.talles)}\n"
            f"Colores Disponibles: {', '.join(self.colores)}\n"
            f"Stock Disponible: {self.stock}\n"
        )