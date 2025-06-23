import unittest
from datetime import date
from tienda.class_itemPedido import ItemPedido
from tienda.class_Producto import Producto
from tienda.class_Pedido import Pedido
from tienda.class_Cupon import Cupon
from tienda.class_Carrito import Carrito
from tienda.cliente import Cliente

class TestPedido(unittest.TestCase):
    def setUp(self):
        # Producto de prueba
        self.producto = Producto(
            id_producto=1,
            nombre="Camisa",
            descripcion="Camisa blanca de algodón",
            precio=100,
            stock=10,
            categoria="Ropa",
            talles=["S", "M", "L"],
            colores=["Blanco", "Negro"]
        )

        # Cupon de prueba
        self.cupon = Cupon("DES10", 10, 5)

        # Cliente y carrito
        self.cliente = Cliente("Juan", "Perez", "juan@mail.com", "1234", "123456789", None, None)
        self.carrito = Carrito(id_carrito=1, cliente=self.cliente)
        self.cliente.carrito = self.carrito  # conectar ambos
        self.item = ItemPedido(self.producto, 2, self.producto.precio)

        # Pedido de prueba
        self.pedido = Pedido(1, self.cliente, "Tarjeta", "Envio a domicilio", self.cupon)

    def test_agregar_item(self):
        self.pedido.agregarItem(self.item)
        self.assertEqual(len(self.pedido.items), 1)

    def test_calcular_total(self):
        self.pedido.agregarItem(self.item)
        total = self.pedido.calcularTotal()
        self.assertEqual(total, 200)

    def test_aplicar_descuento_con_cupon(self):
        self.pedido.agregarItem(self.item)
        total_con_descuento = self.pedido.aplicarDescuento()
        self.assertEqual(total_con_descuento, 180)

    def test_aplicar_descuento_sin_cupon(self):
        self.pedido.cupon = None
        self.pedido.agregarItem(self.item)
        total_sin_descuento = self.pedido.aplicarDescuento()
        self.assertEqual(total_sin_descuento, 200)

    def test_realizar_pago(self):
        resultado = self.pedido.realizarPago()
        self.assertIn("Pedido pagado por Juan Perez", resultado)

    def test_realizar_compra_exitosa(self):
        self.pedido.agregarItem(self.item)
        mensaje = self.pedido.registrarCompra()
        self.assertIn("Compra registrada el", mensaje)
        self.assertIn(self.pedido, self.cliente.historialPedido)

    def test_registrar_compra_con_stock_insuficiente(self):
        item_agotado = ItemPedido(self.producto, 1000, self.producto.precio)
        self.pedido.agregarItem(item_agotado)
        resultado = self.pedido.registrarCompra()
        self.assertEqual(resultado, "Stock insuficiente!")

if __name__ == '__main__':
    unittest.main()

        
