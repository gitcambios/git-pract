from tienda.class_Producto import Producto
from tienda.Class_Categoria import Categoria


#Scrum 3 y 9
def verProductoCategoria(productos, id_categoria):
    productosEncontrados  = []

    for p in productos:
        if p.categoria.id_categoria == id_categoria:
            productosEncontrados.append(p)

        if len(productosEncontrados) == 0:
            return f"Categoria no encontrada"
        
    return productosEncontrados

def buscador(productos, palabraBuscada):
    resultados = []
    
    for p in productos:
        if palabraBuscada in p.nombre.lower() or palabraBuscada in p.descripcion.lower():
            resultados.append(p)
    
    if not resultados:
        return f"No se encontraron resultados"
    
    return resultados 

