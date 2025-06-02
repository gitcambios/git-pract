from class_Producto import Producto
from Class_Categoria import Categoria

# Crear categorías
categorias = [
    Categoria(1, "Remeras"),
    Categoria(2, "Pantalones"),
    Categoria(3, "Camperas")
]

# Crear productos 
productos = [
    Producto(1, "Remera blanca", "Remera de algodón", 2500, 10, categorias[0], ["S", "M", "L"], ["Blanco", "Negro"]),
    Producto(2, "Pantalon jean", "Jean denim", 5000, 5, categorias[1], ["38", "40", "42", "44"], ["Azul", "Gris", "Negro"]),
    Producto(3, "Campera rompeviento", "Campera liviana para el viento", 7000, 3, categorias[2], ["M", "L"], ["Marron Chocolate", "Azul Marino"])
]

#Scrum 9 
def verDetalleProducto(productoSeleccionado): 
    print("\nDetalles de producto:") 
    print(productoSeleccionado.mostrarDetalles())   
    print("-----------------------------")         

#Scrum 3 y 9
def verProductoCategoria(productos, categorias):

    while True: 
        try:
            opcion = int(input("Elegir una categoria: \n1.Remeras\n2.Pantalones \n3.Camperas \n0.Salir \n"))
        except ValueError:
            print("Ingrese un numero valido!")
            continue

        # opcion para salir del while
        if opcion == 0:
            print("Salio del menu categoria")
            break
        #Bandera para ver si hay producto en x categoria
        productoEncontrado = False
        for c in categorias:
            if opcion == c.id_categoria:
                for p in productos:
                    if p.categoria.id_categoria == c.id_categoria:
                        print(p)
                        productoEncontrado = True

        if not productoEncontrado:
            print("No se encontraron productos en esa categoria")
        
        # Preguntamos si quiere ver un producto en especifico
        if productoEncontrado:
            verDetalle = input("Desea ver el detalle de algun producto? (s/n)")
            if verDetalle == "s":
                nombreProducto = input("Ingrese el nombre exacto del producto").strip().lower()
                encontrado = False
                for p in productos:
                    if p.nombre.lower() == nombreProducto:
                        verDetalleProducto(p)
                        encontrado = True
                        break
                
                if not encontrado:
                    print("El producto no se encontro!")


verProductoCategoria(productos, categorias)

