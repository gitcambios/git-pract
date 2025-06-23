import unittest
from tienda.producto import Producto
from tienda.categoria import Categoria

class TestProducto (unittest.TestCase):

    def setUp(self):
        categoria = Categoria (1, "Remeras")
        self.producto = Producto(
            id_producto = 1,
            nombre = "Remera",
            descripcion = "Remera de algodon suave",
            precio = 1000,
            stock = 10,
            categoria = categoria,
            talles = ["S", "M", "L"],
            colores = ["Rojo", "Negro"]
        )
    
    def test_agregarStock(self):
        self.producto.agregarStock(5)
        self.assertEqual(self.producto.stock, 15)

    def test_eliminarStock_valido(self):
        self.producto.eliminarStock(3)
        self.assertEqual(self.producto.stock, 7)

    def test_eliminarStock_invalido(self):
        with self.assertRaises(ValueError):
            self.producto.eliminarStock(20)


if __name__ == '__main__':
    unittest.main()