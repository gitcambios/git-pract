

import unittest
from datetime import date
from tienda.class_itemPedido import ItemPedido
from tienda.cliente import Cliente
from tienda.class_Cupon import Cupon
from tienda.class_Producto import Producto
from.tienda.class_Pedido import Pedido


class TestPedido(unittest.TestCase):
    def setUp(self):
        self.producto = Producto("Camisa", 100, 10)
        self.item = ItemPedido(self.producto,2)
        self.cliente = Cliente("Juan", "Perez")
        self.cupon = Cupon("DES10", 10, 5)
        self.pedido = Pedido(1, self.cliente, "Tarjeta" "Envio a domicilio", self.cupon)

    def test_agregar_item(self):
        self.pedido.agregar.Item(self.item)
        self.assertEqual(len(self.pedido.items), 1)
        
    def test_calculat_total(self):
        self.pedido.agregarItem(self.item)
        total = self.pedido.calcularTotal()
        self.assertEqual(total,200)

    def test_aplicar_descuento_con_cupon(self):
        self.pedido.agregarItem(self.item)
        total_con_decuento = self.pedido.aplicarDescuento()
        self.assertEqual(total_con_decuento, 180)

    def test_aplicar_descuento_sin_cupon(self):
        self.pedido.cupon = None
        total_sin_decuento = self.pedido.aplicarDescuento()
        self.assertEqual(total_sin_decuento, 200)

    def test_realizar_pago(self):
        resultado = self.pedido.realizarPago()
        self.assertln("Pedido pagado por Juan Perez,  resultado")

    def test_realizar_compra_exitosa(self):
        self.pedido.agregar.Item(self.item)
        mensaje = self.pedido.registrarCompra()
        self.assertln("Compra registrada el",mensaje)
        self.assertln(self.pedido, self.cliente.historialPedido)

    def test_registrar_compra_con_stock_insuficiente(self):
        item_agotado = ItemPedido(self.producto, 1000)
        self.pedido.agregarItem(item_agotado)
        resultado = self.pedido.registrarCompra()
        self.assertEqual(resultado, "Stock insuficiente")

if__name__=="__main__":
unittest.main()



        
