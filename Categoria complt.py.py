class Categoria:
    def __ini__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar(self):
        print(f"{self.nombre} - ${int(self.precio)} - Categoria:{self.categoria.nombre}")


remera = Categoria(1, "Remera")
pantalon = Categoria(2,"Pantalon")
abrigo = Categoria(3, "Abrigo")

productos = [
   Producto("Rermera Blanca", 2000, remera),
   Producto("Pantalon Jeans", 5000, pantalon),
   Producto("Campera", 7000, abrigo)
]

while True:

    print("\n---MENU---")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Salir")

    opcion = input("Opcion:")

    if opcion == "1":
        for i,p in enumerate(productos):
            print(f"{i+1}.", end =""); p.mostrar()


    elif opcion == "2":
        nombre = input("Nombre:")
        precio = float(input("precio:"))
        cat = input("Categoria (1=Remera, 2=Pantalon, 3=Abrigo):")
        

    if cat == "1":
        productos.append(Producto(nombre, precio, remera))
    elif cat == "2:":
        productos.append(Producto(nombre, precio, pantalon))
    elif cat == "3":
        productos.append(Producto(nombre, precio, abrigo))
    else:
        print("Categoria invalida.")
     
    elif opcion == "3":
    for i, p in enumerate(productos):
        print(f"{i+1}. ", end=""); p.mostrar()
        i=int(input("Número a eliminar: ")) - 1
    if 0 <= i < len(productos):
        productos.pop(i)
        print("Eliminado.")
    else:
        print("Número inválido.")  
