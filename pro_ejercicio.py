

class Producto:
    def _init_(self, id_producto, nombre, descripcion, precio, stock, categoria):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def actualizarStock(self, cantidad):
        self.stock = self.stock - cantidad

    def mostrarDetalles(self):
        print(self.nombre, "-", self.descripcion, "-", "$", self.precio, "- Stock:", self.stock)


# Lista de productos
productos = [
    Producto(1, "Pantalón", "Pantalón de jean", 30, 15, "Ropa"),
    Producto(2, "Remera", "Remera de algodón", 15, 25, "Ropa"),
    Producto(3, "Abrigo", "Campera de abrigo", 60, 10, "Ropa")
]

# Menú simple
def mostrar_menu():
    print("")
    print("----- MENÚ -----")
    print("1. Ver productos")
    print("2. Ver productos por categoría")
    print("3. Actualizar stock")
    print("4. Salir")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Opción: ")

    if opcion == "1":
        for p in productos:
            p.mostrarDetalles()

    elif opcion == "2":
        categoria = input("Ingrese la categoría: ")
        for p in productos:
            if p.categoria.lower() == categoria.lower():
                p.mostrarDetalles()

    elif opcion == "3":
        id_prod = int(input("ID del producto: "))
        cantidad = int(input("Cantidad vendida: "))
        for p in productos:
            if p.id_producto == id_prod:
                p.actualizarStock(cantidad)
                print("Nuevo stock:", p.stock)

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida.")